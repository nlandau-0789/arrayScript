from base_compiler import tokens, literals, operators, types, consts_types, funcs
import extra_compile_data
from pprint import pprint

def get_translater(code):
    operators.extend(extra_compile_data.get_new_operators(code))
    types.extend(extra_compile_data.get_new_structs(code))
    return \
rf"""

def translate(stmt):
    pass

def run(p):
    print(p)
    # program = "#include <arrs.cpp>\n\n"
    # for i in p:
    #     program += translate(i)
    # print(program)

parser = yacc.yacc(debug=True)
    
    








"""