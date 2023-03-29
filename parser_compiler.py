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
    {op.return_value}

"""

def format_func_ret_val():
    return f"\n               | ".join(map(lambda x : f"{x.__name__} '(' arguments ')'", types+funcs))

def format_consts_types():
    return "\n              | ".join(x.__name__ for x in consts_types)

def get_parser(code):
    operators.extend(extra_compile_data.get_new_operators(code))
    return \
f"""
{"".join(map(format_operator_def, operators))}

def p_expr(p):
    '''
    expr : const_val 
         | VAR
    '''
    p[0] = p[1]

def p_single_argument(p):
    '''
    arguments : expr
    '''
    p[0] = [p[1]]

def p_arguments(p):
    '''
    arguments : arguments ',' arguments
    '''
    p[0] = p[1]+p[3]
    

def p_const_val(p):
    '''
    const_val : {format_consts_types()}
    '''
    p[0] = p[1]

def p_return_val(p):
    '''
    return_val : {format_func_ret_val()}
    '''
    p[0] = ()

def p_error(p):
    print(f"Syntax error at line {{p.lexer.lineno}}")

parser = yacc.yacc()

"""
