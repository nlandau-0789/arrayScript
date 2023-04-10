from ply import *
from pprint import pprint
import json

tokens = ('FLOAT', 'NUM', 'STRING_3SQ', 'STRING_3DQ', 'STRING_SQ', 'STRING_DQ', 'true', 'Null', 'false', 'for', 'while', 'if', 'else', 'elif', 'func', 'struct', 'operator', 'return', 'break', 'continue', 'del', 'lambda', 'pass', 'operator_add', 'operator_sub', 'operator_mul', 'operator_div', 'operator_trudiv', 'operator_pow', 'operator_join', 'operator_split', 'operator_scan', 'operator_reduc', 'operator_bitand', 'operator_bitor', 'operator_bitxor', 'operator_bitshiftleft', 'operator_bitshiftright', 'operator_and', 'operator_or', 'operator_xor', 'operator_contains', 'operator_bitnot', 'operator_not', 'operator_incr', 'operator_decr', 'operator_outer', 'operator_inner', 'operator_reverse', 'operator_rotate', 'operator_apply', 'operator_compose', 'operator_over', 'operator_map', 'operator_sorted_incr', 'operator_sorted_decr', 'operator_less_than', 'operator_less_than_equals', 'operator_greater_than', 'operator_greater_than_equals', 'operator_equals', 'operator_not_equals', 'operator_smallest', 'operator_greatest', 'type_type', 'type_num', 'type_bool', 'type_any', 'type_u64', 'type_u32', 'type_u16', 'type_u8', 'type_i64', 'type_i32', 'type_i16', 'type_i8', 'type_f32', 'type_f64', 'type_str', 'type_list', 'type_tuple', 'type_array', 'type_vector', 'type_dict', 'type_generator', 'type_linked_list', 'type_doubly_linked_list', 'type_deque', 'type_heap', 'type_fibonacci_heap', 'type_tree', 'type_trie', 'type_stack', 'type_queue', 'type_binary_search_tree', 'type_bitset', 'type_set', 'type_map', 'type_range', 'type_bad_struct', 'type_bad_struct2', 'operator_goodname', 'operator_s_combinator', 'operator_s_combinator_2', 'operator_goodname2', 'VAR', 'NEWLINE')

def t_FLOAT(t):
    r"-?\d+\.\d+"
    t.value = float(t.value)
    return t

def t_NUM(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

def t_STRING_3SQ(t):
    r"""\'\'\'([^\\\n]|(\\.))*?\'\'\'"""
    t.value = json.dumps(eval(t.value))
    return t

def t_STRING_3DQ(t):
    r'''\"\"\"([^\\\n]|(\\.))*?\"\"\"'''
    t.value = json.dumps(eval(t.value))
    return t

def t_STRING_SQ(t):
    r"""\'([^\\\n]|(\\.))*?\'"""
    t.value = json.dumps(eval(t.value))
    return t

def t_STRING_DQ(t):
    r"""\"([^\\\n]|(\\.))*?\""""
    t.value = json.dumps(eval(t.value))
    return t
t_true = r'''true'''

def t_Null(t):
    r"""Null"""
    t.value = "NULL"
    return t
t_false = r'''false'''
t_for = r'''for'''
t_while = r'''while'''
t_if = r'''if'''
t_else = r'''else'''
t_elif = r'''elif'''
t_func = r'''func'''
t_struct = r'''struct'''
t_operator = r'''operator'''
t_return = r'''return'''
t_break = r'''break'''
t_continue = r'''continue'''
t_del = r'''del'''
t_lambda = r'''lambda'''
t_pass = r'''pass'''
t_operator_add = r'''\+'''
t_operator_sub = r'''\-'''
t_operator_mul = r'''\*'''
t_operator_div = r'''//'''
t_operator_trudiv = r'''/'''
t_operator_pow = r'''\*\*'''
t_operator_join = r'''\-\+\-'''
t_operator_split = r'''\-\|\-'''
t_operator_scan = r'''\->'''
t_operator_reduc = r'''/>'''
t_operator_bitand = r'''\&\&'''
t_operator_bitor = r'''\|\|'''
t_operator_bitxor = r'''\^'''
t_operator_bitshiftleft = r'''<<'''
t_operator_bitshiftright = r'''>>'''
t_operator_and = r'''and'''
t_operator_or = r'''or'''
t_operator_xor = r'''xor'''
t_operator_contains = r'''in'''
t_operator_bitnot = r'''\~'''
t_operator_not = r'''not'''
t_operator_incr = r'''\+\+'''
t_operator_decr = r'''\-\-'''
t_operator_outer = r'''\+\.'''
t_operator_inner = r'''\-\.'''
t_operator_reverse = r'''<\|>'''
t_operator_rotate = r'''\-o\-'''
t_operator_apply = r'''\.'''
t_operator_compose = r'''::'''
t_operator_over = r'''\.\.'''
t_operator_map = r'''\[\]'''
t_operator_sorted_incr = r'''>_>'''
t_operator_sorted_decr = r'''<_<'''
t_operator_less_than = r'''<'''
t_operator_less_than_equals = r'''<='''
t_operator_greater_than = r'''>'''
t_operator_greater_than_equals = r'''>='''
t_operator_equals = r'''=='''
t_operator_not_equals = r'''!='''
t_operator_smallest = r'''<\?'''
t_operator_greatest = r'''>\?'''
t_type_type = r'''type'''
t_type_num = r'''num'''
t_type_bool = r'''bool'''
t_type_any = r'''any'''
t_type_u64 = r'''u64'''
t_type_u32 = r'''u32'''
t_type_u16 = r'''u16'''
t_type_u8 = r'''u8'''
t_type_i64 = r'''i64'''
t_type_i32 = r'''i32'''
t_type_i16 = r'''i16'''
t_type_i8 = r'''i8'''
t_type_f32 = r'''f32'''
t_type_f64 = r'''f64'''
t_type_str = r'''str'''
t_type_list = r'''list'''
t_type_tuple = r'''tuple'''
t_type_array = r'''array'''
t_type_vector = r'''vector'''
t_type_dict = r'''dict'''
t_type_generator = r'''generator'''
t_type_linked_list = r'''linked_list'''
t_type_doubly_linked_list = r'''doubly_linked_list'''
t_type_deque = r'''deque'''
t_type_heap = r'''heap'''
t_type_fibonacci_heap = r'''fibonacci_heap'''
t_type_tree = r'''tree'''
t_type_trie = r'''trie'''
t_type_stack = r'''stack'''
t_type_queue = r'''queue'''
t_type_binary_search_tree = r'''binary_search_tree'''
t_type_bitset = r'''bitset'''
t_type_set = r'''set'''
t_type_map = r'''map'''
t_type_range = r'''range'''
t_type_bad_struct = r'''bad_struct'''
t_type_bad_struct2 = r'''bad_struct2'''
t_operator_goodname = r'''op'''
t_operator_s_combinator = r'''S'''
t_operator_s_combinator_2 = r'''S'''
t_operator_goodname2 = r'''op2'''

reserved = {'true': 'true', 'false': 'false', 'for': 'for', 'while': 'while', 'if': 'if', 'else': 'else', 'elif': 'elif', 'func': 'func', 'struct': 'struct', 'operator': 'operator', 'return': 'return', 'break': 'break', 'continue': 'continue', 'del': 'del', 'lambda': 'lambda', 'pass': 'pass', 'and': 'operator_and', 'or': 'operator_or', 'xor': 'operator_xor', 'in': 'operator_contains', 'not': 'operator_not', 'type': 'type_type', 'num': 'type_num', 'bool': 'type_bool', 'any': 'type_any', 'u64': 'type_u64', 'u32': 'type_u32', 'u16': 'type_u16', 'u8': 'type_u8', 'i64': 'type_i64', 'i32': 'type_i32', 'i16': 'type_i16', 'i8': 'type_i8', 'f32': 'type_f32', 'f64': 'type_f64', 'str': 'type_str', 'list': 'type_list', 'tuple': 'type_tuple', 'array': 'type_array', 'vector': 'type_vector', 'dict': 'type_dict', 'generator': 'type_generator', 'linked_list': 'type_linked_list', 'doubly_linked_list': 'type_doubly_linked_list', 'deque': 'type_deque', 'heap': 'type_heap', 'fibonacci_heap': 'type_fibonacci_heap', 'tree': 'type_tree', 'trie': 'type_trie', 'stack': 'type_stack', 'queue': 'type_queue', 'binary_search_tree': 'type_binary_search_tree', 'bitset': 'type_bitset', 'set': 'type_set', 'map': 'type_map', 'range': 'type_range', 'bad_struct': 'type_bad_struct', 'bad_struct2': 'type_bad_struct2', 'op': 'operator_goodname', 'S': 'operator_s_combinator', 'S': 'operator_s_combinator_2', 'op2': 'operator_goodname2'}

def t_VAR(t):
   r'[a-zA-Z_][a-zA-Z_\d]*'
   t.type = reserved.get(t.value,'VAR')
   return t

literals = ',()[]{}:=;'

def t_comment(t):
        r'(/\*(.|\n)*?\*/)|(\#.*)'
        t.lexer.lineno += t.value.count('\n')



def t_lbrace(t):
    r'\{\n*'
    t.type = '{'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_rbrace(t):
    r'(\n|\ )*\}'
    t.type = '}'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# while True:
#     inp = input(">>> ")
#     if inp in {"exit", "quit", "kill"}:
#         break
#     lex.input(inp)
#     pprint(list(lexer))


precedence = (("left", "="), ('left', 'operator_and', 'operator_or', 'operator_xor', 'operator_contains', 'operator_not', 'operator_less_than', 'operator_less_than_equals', 'operator_greater_than', 'operator_greater_than_equals', 'operator_equals', 'operator_not_equals', 'operator_smallest', 'operator_greatest', 'operator_s_combinator', 'operator_s_combinator_2'), ('left', 'operator_add', 'operator_sub', 'operator_join', 'operator_split', 'operator_bitand', 'operator_bitor', 'operator_bitxor', 'operator_bitshiftleft', 'operator_bitshiftright', 'operator_outer', 'operator_inner'), ('left', 'operator_mul', 'operator_div', 'operator_trudiv'), ('left', 'operator_pow'), ('left', 'operator_scan', 'operator_reduc', 'operator_rotate', 'operator_apply'), ('left', 'operator_bitnot', 'operator_incr', 'operator_decr', 'operator_reverse', 'operator_sorted_incr', 'operator_sorted_decr', 'operator_goodname'), ('left', 'operator_map'), ('left', 'operator_over'), ('left', 'operator_compose'), ('left', 'operator_goodname2'))

def get_operator_name(symbol):
    return {'+': 'operator_add', '-': 'operator_sub', '*': 'operator_mul', '//': 'operator_div', '/': 'operator_trudiv', '**': 'operator_pow', '-+-': 'operator_join', '-|-': 'operator_split', '->': 'operator_scan', '/>': 'operator_reduc', '&&': 'operator_bitand', '||': 'operator_bitor', '^': 'operator_bitxor', '<<': 'operator_bitshiftleft', '>>': 'operator_bitshiftright', 'and': 'operator_and', 'or': 'operator_or', 'xor': 'operator_xor', 'in': 'operator_contains', '~': 'operator_bitnot', 'not': 'operator_not', '++': 'operator_incr', '--': 'operator_decr', '+.': 'operator_outer', '-.': 'operator_inner', '<|>': 'operator_reverse', '-o-': 'operator_rotate', '.': 'operator_apply', '::': 'operator_compose', '..': 'operator_over', '[]': 'operator_map', '>_>': 'operator_sorted_incr', '<_<': 'operator_sorted_decr', '<': 'operator_less_than', '<=': 'operator_less_than_equals', '>': 'operator_greater_than', '>=': 'operator_greater_than_equals', '==': 'operator_equals', '!=': 'operator_not_equals', '<?': 'operator_smallest', '>?': 'operator_greatest', 'op': 'operator_goodname', 'S': 'operator_s_combinator_2', 'op2': 'operator_goodname2'}[symbol]

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
    TYPE : type_type
         | type_num
         | type_bool
         | type_any
         | type_u64
         | type_u32
         | type_u16
         | type_u8
         | type_i64
         | type_i32
         | type_i16
         | type_i8
         | type_f32
         | type_f64
         | type_str
         | type_list
         | type_tuple
         | type_array
         | type_vector
         | type_dict
         | type_generator
         | type_linked_list
         | type_doubly_linked_list
         | type_deque
         | type_heap
         | type_fibonacci_heap
         | type_tree
         | type_trie
         | type_stack
         | type_queue
         | type_binary_search_tree
         | type_bitset
         | type_set
         | type_map
         | type_range
         | type_bad_struct
         | type_bad_struct2
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
    block_stmt : block_decl '{' stmts '}'
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
    block_stmt : block_decl '{' '}'
               | block_decl '{' newline '}'
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
    const_val : FLOAT
              | NUM
              | STRING_3SQ
              | STRING_3DQ
              | STRING_SQ
              | STRING_DQ
              | true
              | Null
              | false
    '''
    # print(("const", p[1]))
    p[0] = ("const", p[1])

def p_paren_expr(p):
    '''
    expr : '(' expr ')'
    '''
    # print("parens", p.lexer.lineno)
    p[0] = p[2]


def p_operator_add(p):
    '''
    expr : expr operator_add expr
    '''
    # print("+", p.lexer.lineno)
    p[0] = ('call', 'operator_add', [p[1], p[3]])


def p_operator_sub(p):
    '''
    expr : expr operator_sub expr
    '''
    # print("-", p.lexer.lineno)
    p[0] = ('call', 'operator_sub', [p[1], p[3]])


def p_operator_mul(p):
    '''
    expr : expr operator_mul expr
    '''
    # print("*", p.lexer.lineno)
    p[0] = ('call', 'operator_mul', [p[1], p[3]])


def p_operator_div(p):
    '''
    expr : expr operator_div expr
    '''
    # print("//", p.lexer.lineno)
    p[0] = ('call', 'operator_div', [p[1], p[3]])


def p_operator_trudiv(p):
    '''
    expr : expr operator_trudiv expr
    '''
    # print("/", p.lexer.lineno)
    p[0] = ('call', 'operator_trudiv', [p[1], p[3]])


def p_operator_pow(p):
    '''
    expr : expr operator_pow expr
    '''
    # print("**", p.lexer.lineno)
    p[0] = ('call', 'operator_pow', [p[1], p[3]])


def p_operator_join(p):
    '''
    expr : expr operator_join expr
    '''
    # print("-+-", p.lexer.lineno)
    p[0] = ('call', 'operator_join', [p[1], p[3]])


def p_operator_split(p):
    '''
    expr : expr operator_split expr
    '''
    # print("-|-", p.lexer.lineno)
    p[0] = ('call', 'operator_split', [p[1], p[3]])


def p_operator_scan(p):
    '''
    expr : OPERATOR operator_scan expr
    '''
    # print("->", p.lexer.lineno)
    p[0] = ('call', 'operator_scan', [p[1], p[3]])


def p_operator_reduc(p):
    '''
    expr : OPERATOR operator_reduc expr
    '''
    # print("/>", p.lexer.lineno)
    p[0] = ('call', 'operator_reduc', [p[1], p[3]])


def p_operator_bitand(p):
    '''
    expr : expr operator_bitand expr
    '''
    # print("&&", p.lexer.lineno)
    p[0] = ('call', 'operator_bitand', [p[1], p[3]])


def p_operator_bitor(p):
    '''
    expr : expr operator_bitor expr
    '''
    # print("||", p.lexer.lineno)
    p[0] = ('call', 'operator_bitor', [p[1], p[3]])


def p_operator_bitxor(p):
    '''
    expr : expr operator_bitxor expr
    '''
    # print("^", p.lexer.lineno)
    p[0] = ('call', 'operator_bitxor', [p[1], p[3]])


def p_operator_bitshiftleft(p):
    '''
    expr : expr operator_bitshiftleft expr
    '''
    # print("<<", p.lexer.lineno)
    p[0] = ('call', 'operator_bitshiftleft', [p[1], p[3]])


def p_operator_bitshiftright(p):
    '''
    expr : expr operator_bitshiftright expr
    '''
    # print(">>", p.lexer.lineno)
    p[0] = ('call', 'operator_bitshiftright', [p[1], p[3]])


def p_operator_and(p):
    '''
    expr : expr operator_and expr
    '''
    # print("and", p.lexer.lineno)
    p[0] = ('call', 'operator_and', [p[1], p[3]])


def p_operator_or(p):
    '''
    expr : expr operator_or expr
    '''
    # print("or", p.lexer.lineno)
    p[0] = ('call', 'operator_or', [p[1], p[3]])


def p_operator_xor(p):
    '''
    expr : expr operator_xor expr
    '''
    # print("xor", p.lexer.lineno)
    p[0] = ('call', 'operator_xor', [p[1], p[3]])


def p_operator_contains(p):
    '''
    expr : expr operator_contains expr
    '''
    # print("in", p.lexer.lineno)
    p[0] = ('call', 'operator_contains', [p[1], p[3]])


def p_operator_bitnot(p):
    '''
    expr : operator_bitnot expr
    '''
    # print("~", p.lexer.lineno)
    p[0] = ('call', 'operator_bitnot', [p[2]])


def p_operator_not(p):
    '''
    expr : operator_not expr
    '''
    # print("not", p.lexer.lineno)
    p[0] = ('call', 'operator_not', [p[2]])


def p_operator_incr(p):
    '''
    expr : expr operator_incr
    '''
    # print("++", p.lexer.lineno)
    p[0] = ('call', 'operator_incr', [p[1]])


def p_operator_decr(p):
    '''
    expr : expr operator_decr
    '''
    # print("--", p.lexer.lineno)
    p[0] = ('call', 'operator_decr', [p[1]])


def p_operator_outer(p):
    '''
    expr : expr operator_outer OPERATOR expr
    '''
    # print("+.", p.lexer.lineno)
    p[0] = ('call', 'operator_outer', [p[1], p[3], p[4]])


def p_operator_inner(p):
    '''
    expr : expr OPERATOR operator_inner OPERATOR expr
    '''
    # print("-.", p.lexer.lineno)
    p[0] = ('call', 'operator_inner', [p[1], p[2], p[4], p[5]])


def p_operator_reverse(p):
    '''
    expr : operator_reverse expr
    '''
    # print("<|>", p.lexer.lineno)
    p[0] = ('call', 'operator_reverse', [p[2]])


def p_operator_rotate(p):
    '''
    expr : expr operator_rotate expr
    '''
    # print("-o-", p.lexer.lineno)
    p[0] = ('call', 'operator_rotate', [p[1], p[3]])


def p_operator_apply(p):
    '''
    expr : expr operator_apply expr
    '''
    # print(".", p.lexer.lineno)
    p[0] = ('call', 'operator_apply', [p[1], p[3]])


def p_operator_compose(p):
    '''
    expr : expr operator_compose expr
    '''
    # print("::", p.lexer.lineno)
    p[0] = ('call', 'operator_compose', [p[1], p[3]])


def p_operator_over(p):
    '''
    expr : expr operator_over expr
    '''
    # print("..", p.lexer.lineno)
    p[0] = ('call', 'operator_over', [p[1], p[3]])


def p_operator_map(p):
    '''
    expr : expr operator_map
    '''
    # print("[]", p.lexer.lineno)
    p[0] = ('call', 'operator_map', [p[1]])


def p_operator_sorted_incr(p):
    '''
    expr : operator_sorted_incr expr
    '''
    # print(">_>", p.lexer.lineno)
    p[0] = ('call', 'operator_sorted_incr', [p[2]])


def p_operator_sorted_decr(p):
    '''
    expr : operator_sorted_decr expr
    '''
    # print("<_<", p.lexer.lineno)
    p[0] = ('call', 'operator_sorted_decr', [p[2]])


def p_operator_less_than(p):
    '''
    expr : expr operator_less_than expr
    '''
    # print("<", p.lexer.lineno)
    p[0] = ('call', 'operator_less_than', [p[1], p[3]])


def p_operator_less_than_equals(p):
    '''
    expr : expr operator_less_than_equals expr
    '''
    # print("<=", p.lexer.lineno)
    p[0] = ('call', 'operator_less_than_equals', [p[1], p[3]])


def p_operator_greater_than(p):
    '''
    expr : expr operator_greater_than expr
    '''
    # print(">", p.lexer.lineno)
    p[0] = ('call', 'operator_greater_than', [p[1], p[3]])


def p_operator_greater_than_equals(p):
    '''
    expr : expr operator_greater_than_equals expr
    '''
    # print(">=", p.lexer.lineno)
    p[0] = ('call', 'operator_greater_than_equals', [p[1], p[3]])


def p_operator_equals(p):
    '''
    expr : expr operator_equals expr
    '''
    # print("==", p.lexer.lineno)
    p[0] = ('call', 'operator_equals', [p[1], p[3]])


def p_operator_not_equals(p):
    '''
    expr : expr operator_not_equals expr
    '''
    # print("!=", p.lexer.lineno)
    p[0] = ('call', 'operator_not_equals', [p[1], p[3]])


def p_operator_smallest(p):
    '''
    expr : expr operator_smallest expr
    '''
    # print("<?", p.lexer.lineno)
    p[0] = ('call', 'operator_smallest', [p[1], p[3]])


def p_operator_greatest(p):
    '''
    expr : expr operator_greatest expr
    '''
    # print(">?", p.lexer.lineno)
    p[0] = ('call', 'operator_greatest', [p[1], p[3]])


def p_operator_goodname(p):
    '''
    expr : expr operator_goodname expr
    '''
    # print("op", p.lexer.lineno)
    p[0] = ('call', 'operator_goodname', [p[1], p[3]])


def p_operator_s_combinator(p):
    '''
    expr : operator_s_combinator expr expr expr
    '''
    # print("S", p.lexer.lineno)
    p[0] = ('call', 'operator_s_combinator', [p[2], p[3], p[4]])


def p_operator_s_combinator_2(p):
    '''
    expr : operator_s_combinator_2 OPERATOR OPERATOR expr
    '''
    # print("S", p.lexer.lineno)
    p[0] = ('call', 'operator_s_combinator_2', [p[2], p[3], p[4]])


def p_operator_goodname2(p):
    '''
    expr : operator_goodname2 expr
    '''
    # print("op2", p.lexer.lineno)
    p[0] = ('call', 'operator_goodname2', [p[2]])



def p_var(p):
    '''
    expr : VAR
    '''
    # print("var", p[1], p.lexer.lineno)
    p[0] = ("var", p[1])

def p_return_val(p):
    '''
    return_val : VAR '(' arguments ')'
    '''
    # print("return value", p.lexer.lineno)
    p[0] = ("call", p[1], p[3])

def p_instantiation(p):
    '''
    return_val : type_type '(' arguments ')'
               | type_num '(' arguments ')'
               | type_bool '(' arguments ')'
               | type_any '(' arguments ')'
               | type_u64 '(' arguments ')'
               | type_u32 '(' arguments ')'
               | type_u16 '(' arguments ')'
               | type_u8 '(' arguments ')'
               | type_i64 '(' arguments ')'
               | type_i32 '(' arguments ')'
               | type_i16 '(' arguments ')'
               | type_i8 '(' arguments ')'
               | type_f32 '(' arguments ')'
               | type_f64 '(' arguments ')'
               | type_str '(' arguments ')'
               | type_list '(' arguments ')'
               | type_tuple '(' arguments ')'
               | type_array '(' arguments ')'
               | type_vector '(' arguments ')'
               | type_dict '(' arguments ')'
               | type_generator '(' arguments ')'
               | type_linked_list '(' arguments ')'
               | type_doubly_linked_list '(' arguments ')'
               | type_deque '(' arguments ')'
               | type_heap '(' arguments ')'
               | type_fibonacci_heap '(' arguments ')'
               | type_tree '(' arguments ')'
               | type_trie '(' arguments ')'
               | type_stack '(' arguments ')'
               | type_queue '(' arguments ')'
               | type_binary_search_tree '(' arguments ')'
               | type_bitset '(' arguments ')'
               | type_set '(' arguments ')'
               | type_map '(' arguments ')'
               | type_range '(' arguments ')'
               | type_bad_struct '(' arguments ')'
               | type_bad_struct2 '(' arguments ')'
    '''
    # print("return value", p.lexer.lineno)
    p[0] = ("call", ("make_"+p[1]), p[3])

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
            #   | format_types_and_funcs_as_args()
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
    OPERATOR : operator_add
         | operator_sub
         | operator_mul
         | operator_div
         | operator_trudiv
         | operator_pow
         | operator_join
         | operator_split
         | operator_scan
         | operator_reduc
         | operator_bitand
         | operator_bitor
         | operator_bitxor
         | operator_bitshiftleft
         | operator_bitshiftright
         | operator_and
         | operator_or
         | operator_xor
         | operator_contains
         | operator_bitnot
         | operator_not
         | operator_incr
         | operator_decr
         | operator_outer
         | operator_inner
         | operator_reverse
         | operator_rotate
         | operator_apply
         | operator_compose
         | operator_over
         | operator_map
         | operator_sorted_incr
         | operator_sorted_decr
         | operator_less_than
         | operator_less_than_equals
         | operator_greater_than
         | operator_greater_than_equals
         | operator_equals
         | operator_not_equals
         | operator_smallest
         | operator_greatest
         | operator_goodname
         | operator_s_combinator
         | operator_s_combinator_2
         | operator_goodname2
    '''
    p[0] = ("var", get_operator_name(p[1]))

def p_error(p):
    if p:
        print("Syntax error at token", p.type, ":", repr(p.value), "at line", p.lexer.lineno)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()



from Utils.array_functions import flatten
from base_compiler import operator
# import json

def translate(stmt, indent = 0):
    if len(stmt) == 1:
        # print(stmt)
        return stmt[0]
    if stmt[0] == "type":
        return "type_"+stmt[1]
    if stmt[0] == "struct":
        return "\t"*indent + "struct "+ translate(stmt[1]) +" {\n" + "\t"*(indent+1) + (";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]]))+ ";\n" + "\t"*indent + "};"
    if stmt[0] == "declaration":
        type_ = translate(stmt[1])
        return [type_+" "+name[1] for name in stmt[2]]
    if stmt[0] == "call":
        # return "\t"*indent + stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
        if stmt[1] == "operator_apply":
            stmt[2][1][2].insert(0, stmt[2][0])
            return translate(stmt[2][1])
        return stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
    if stmt[0] == "const":
        return str(stmt[1])
    if stmt[0] == "assign":
        if len(stmt[1]) == 1:
            return "auto " + translate(stmt[1][0], indent+1) + " = " + translate(stmt[2], indent+1)
        return "auto tmp = " + translate(stmt[2], indent+1) + "; auto " + "; auto ".join(translate(i, indent+1)+" = temp["+ str(idx) +"]" for idx, i in enumerate(stmt[1]))
    if stmt[0] == "var":
        return stmt[1]
    if stmt[0] == "return":
        return "return "+translate(stmt[1], indent+1)
    if stmt[0] == "func":
        return "\t"*indent+"auto " + stmt[1] + "("+ (", ").join(flatten([translate(i, indent+1) for i in stmt[2]])) +"){\n"+"\t"*(indent+1)+(";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[3]]))+";\n"+"\t"*indent+"}"
    if stmt[0] == "operator":
        op = operator(*(eval(str(v[1])) for v in stmt[1]))
        return \
f'''
template<{", ".join("typename "+chr(65+i) for i in range(op.nb_args-1))}>
auto {op.__name__}({", ".join(chr(65+i)+" "+op.args[i] for i in range(op.nb_args-1))})''' + "{\n" + "\t"*(indent+1) + (";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]])) + ";\n" + "\t"*indent + "}"
    if stmt[0] == "lambda":
        req = ""
        return "["+", ".join(req)+"](auto "+ (", auto ").join(flatten([translate(i, indent+1) for i in stmt[1]])) +"){return "+translate(stmt[2], indent+1)+";}"
    if stmt[0] == "for":
        program = ""
        if len(stmt[1]) == 1:
            program = "for (auto&& "+translate(stmt[1][0])+ " : "+translate(stmt[2])+"){\n"
        else :
            program = "for (auto&& "+"["+", ".join(translate(i) for i in stmt[1])+"] : "+translate(stmt[2])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[3])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "while":
        program = "while ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "if":
        program = "if ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "elif":
        program = "else if ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "else":
        program = "else {\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[1])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    # if stmt[0] == "del":
    #     pass
    return ""
    


def run(p):
    # print(p)
    program = "#include <arrs.cpp>\n\nusing namespace arrs;\nusing namespace operators;\nusing namespace types;\nusing namespace funcs;\n\n"
    for i in p:
        program += translate(i)
        program += ";"*(not program[-1] in '};') 
        program += "\n\n"
    with open(file_destination, "w", encoding="utf-8") as f:
        f.write(program)

def compile(code, filename):
    global file_destination
    file_destination = filename
    parser.parse(code)
    
