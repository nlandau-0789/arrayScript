from base_compiler import tokens, literals, operators, types, consts_types, funcs
import extra_compile_data
from pprint import pprint

def isAttrAlpha(s, attr, exceptions = []):
    if not getattr(s, attr, None):
        return False
    t = getattr(s, attr)
    t = "".join(filter(lambda x: not x in exceptions, t))
    return all(map(str.isalpha, t))

def format_operator_def(op):
    return \
f"""
def p_{op.__name__}(p):
    '''
    expr : {op.pattern}
    '''
    # print("{op.symbol}", p.lexer.lineno)
    {op.return_value}

"""
def format_types():
    return "\n         | ".join(x.__name__ for x in types)

def format_operators():
    return "\n         | ".join(x.__name__ for x in operators)

def format_func_ret_val():
    return "\n               | ".join(map(lambda x : f"{x.__name__} '(' arguments ')'", types+funcs))

def format_consts_types():
    return "\n              | ".join(x.__name__ for x in consts_types)

def format_types_and_funcs_as_args():
    return "\n              | ".join(x.__name__ for x in types+funcs)

def format_decl_stmt():
    return "\n                     | ".join(f"{x.__name__} comma_separated_names" for x in types)

def format_precedence():
    from itertools import groupby
    groups = list(map(lambda x : (x[0], list(map(lambda x: x.__name__, x[1]))), groupby(sorted(operators, key=lambda x: x.priority), key=lambda x: x.priority)))
    groups = list(map(lambda x : ("left", *x[1]), groups))
    # pprint(groups)
    return f"""precedence = (("left", "="), {", ".join(map(str, groups))})"""

def get_parser(code):
    operators.extend(extra_compile_data.get_new_operators(code))
    operators_dict = {op.symbol : op.__name__ for op in operators}
    types.extend(extra_compile_data.get_new_structs(code))
    return \
f"""
{format_precedence()}

def get_operator_name(symbol):
    return {operators_dict}[symbol]

start = 'program'

def p_program(p):
    '''
    program : stmts
    '''
    # pprint(p[1], indent=4)
    # p[0] = p[1]
    run(p[1])

def p_program2(p):
    '''
    program : newline stmts
            | newline stmts newline
    '''
    # pprint(p[2], indent=4)
    # p[0] = p[2]
    run(p[2])

def p_newline(p):
    '''
    newline : NEWLINE
    '''
    p[0] = p[1]

def p_newlines(p):
    '''
    newline : NEWLINE newline 
    '''
    p[0] = p[1]

def p_single_stmts(p):
    '''
    stmts : stmt
    '''
    p[0] = [p[1]]

def p_stmts(p):
    '''
    stmts : stmts newline stmt
    '''
    # pprint(("stmts", p[1]+[p[3]]), indent=4)
    p[0] = p[1]+[p[3]]

def p_stmts_after_bloc(p):
    '''
    stmts : block_stmt stmts
    '''
    # pprint(("stmts", p[1]+[p[3]]), indent=4)
    p[0] = [p[1]]+p[2]

def p_stmt(p):
    '''
    stmt : line_stmt
         | block_stmt
    '''
    # pprint(p[1], indent=4)
    p[0] = p[1]

def p_TYPE(p):
    '''
    TYPE : {format_types()}
    '''
    p[0] = ("type", p[1])

def p_line_stmt(p):
    '''
    line_stmt : return_stmt
              | expr
              | word_stmt
              | del_stmt
              | declaration_stmt
              | assign_stmt
    '''
    # print(p[1])
    p[0] = p[1]

def p_item(p):
    '''
    item : expr '[' expr ']'
    '''
    # print(("item", p[1], p[3]))
    p[0] = ("call", "item", [p[1], p[3]])

def p_simple_slice(p):
    '''
    simple_slice : expr '[' expr ':' expr ']'
    '''
    p[0] = ("call", "simple_slice", [p[1], p[3], p[5]])

def p_full_slice(p):
    '''
    full_slice : expr '[' expr ':' expr ':' expr ']'
    '''
    p[0] = ("call", "full_slice", [p[1], p[3], p[5], p[7]])

def p_listop(p):
    '''
    expr : item
         | simple_slice
         | full_slice
    '''
    # pprint(p[1], indent=4)
    p[0] = p[1]

def p_lambda_decl(p):
    '''
    lambda_decl : lambda comma_separated_names ':' expr
    '''
    p[0] = ("lambda", p[2], p[4])
    
def p_return_stmt(p):
    '''
    return_stmt : return expr
    '''
    # print("return statement at line", p.lexer.lineno)
    p[0] = ("return", p[2])

def p_del_stmt(p):
    '''
    del_stmt : del expr
    '''
    p[0] = ("del", p[2])

def p_assign_stmt(p):
    '''
    assign_stmt : comma_separated_names '=' expr
                | item '=' expr
                | simple_slice '=' expr
                | full_slice '=' expr
    '''
    # print("=", p[1], p[3])
    p[0] = ("assign", p[1], p[3])

def p_declaration_stmt(p):
    '''
    declaration_stmt : TYPE comma_separated_names
    '''
    p[0] = ("declaration", p[1], p[2])

def p_comma_separated_name(p):
    '''
    comma_separated_names : VAR
    '''
    p[0] = [("var", p[1])]

def p_comma_separated_names(p):
    '''
    comma_separated_names : VAR ',' comma_separated_names 
    '''
    p[0] = [("var", p[1])]+p[3]

def p_block_stmt(p):
    '''
    block_stmt : block_decl '{{' stmts '}}'
    '''
    p[0] = tuple(list(p[1])+[p[3]])

def p_word_stmt(p):
    '''
    word_stmt : break
              | return
              | continue
              | pass
    '''
    p[0] = (p[1],)

def p_block_stmt_empty(p):
    '''
    block_stmt : block_decl '{{' '}}'
               | block_decl '{{' newline '}}'
    '''
    p[0] = (*p[1], [])

def p_block_decl(p):
    '''
    block_decl : for_decl
               | if_decl
               | else_decl
               | elif_decl
               | operator_decl
               | struct_decl
               | while_decl
               | func_decl
    '''
    p[0] = p[1]

def p_for_decl(p):
    '''
    for_decl : for comma_separated_names operator_contains expr
    '''
    # print(("for", p[2], p[4]))
    p[0] = ("for", p[2], p[4])

def p_if_decl(p):
    '''
    if_decl : if expr
    '''
    p[0] = ("if", p[2])

def p_elif_decl(p):
    '''
    elif_decl : elif expr
    '''
    p[0] = ("elif", p[2])

def p_else_decl(p):
    '''
    else_decl : else
    '''
    p[0] = ("else",)

def p_operator_decl(p):
    '''
    operator_decl : operator '(' arguments ')'
    '''
    p[0] = ("operator", p[3])

def p_struct_decl(p):
    '''
    struct_decl : struct TYPE
    '''
    p[0] = ("struct", p[2])

def p_while_decl(p):
    '''
    while_decl : while expr
    '''
    p[0] = ("while", p[2])

def p_func_decl(p):
    '''
    func_decl : func VAR '(' def_arguments ')'
    '''
    p[0] = ("func", p[2], p[4])

def p_def_argument(p):
    '''
    def_arguments : declaration_stmt
    '''
    p[0] = [p[1]]

def p_def_argument_empty(p):
    '''
    def_arguments : empty
    '''
    p[0] = []

def p_def_arguments(p):
    '''
    def_arguments : declaration_stmt ';' def_arguments
    '''
    p[0] = [p[1]]+p[3]
    
def p_const_val(p):
    '''
    const_val : {format_consts_types()}
    '''
    # print(("const", p[1]))
    p[0] = ("const", p[1])

def p_paren_expr(p):
    '''
    expr : '(' expr ')'
    '''
    # print("parens", p.lexer.lineno)
    p[0] = p[2]

{"".join(map(format_operator_def, operators))}

def p_var(p):
    '''
    expr : VAR
    '''
    # print("var", p[1], p.lexer.lineno)
    p[0] = ("var", p[1])

def p_return_val(p):
    '''
    return_val : {format_func_ret_val()}
               | VAR '(' arguments ')'
    '''
    # print("return value", p.lexer.lineno)
    p[0] = ("call", p[1], p[3])

def p_expr(p):
    '''
    expr : const_val 
         | return_val
         | lambda_decl
    '''
    # print(p[1], p.lexer.lineno)
    p[0] = p[1]

def p_expr2(p):
    '''
    expr : TYPE
    '''
    # print(p[1], p.lexer.lineno)
    p[0] = ("var", "make_"+p[1][1])

def p_empty(p):
    'empty :'
    pass

def p_argument(p):
    '''
    arguments : expr
    '''
            #   | {"format_types_and_funcs_as_args()"}
    # print("argument :", p[1])
    p[0] = [p[1]]

def p_arguments(p):
    '''
    arguments : arguments ',' arguments
    '''
    # print("arguments :", p[1]+p[3])
    p[0] = p[1]+p[3]


def p_noarg(p):
    '''
    arguments : empty
    '''
    # print("noarg")
    p[0] = []
    
# def p_string(p):
#     '''
#     STRING : STRING_3SQ
#            | STRING_3DQ
#            | STRING_SQ
#            | STRING_DQ
#     '''
#     p[0] = p[1]

def p_OPERATOR(p):
    '''
    OPERATOR : {format_operators()}
    '''
    p[0] = ("var", get_operator_name(p[1]))

def p_error(p):
    if p:
        print("Syntax error at token", p.type, ":", repr(p.value), "at line", p.lexer.lineno)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(debug=True)

"""
