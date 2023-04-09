from base_compiler import tokens, literals
import extra_compile_data
from pprint import pprint

def isAttrAlpha(s, attr, exceptions = []):
    if not getattr(s, attr, None):
        return False
    t = getattr(s, attr)
    # print(t)
    t = "".join(filter(lambda x: not x in exceptions, t))
    # print(t)
    return all(map(str.isalnum, t))

def get_lexer(code):
    tokens.extend(extra_compile_data.get_new_structs(code))
    tokens.extend(extra_compile_data.get_new_operators(code))
    return """from ply import *
from pprint import pprint
import json

tokens = (""" + ", ".join(map(lambda x: repr(x.__name__), tokens)) + """, 'VAR', 'NEWLINE')
""" + "\n".join(map(lambda x: x.tokenizer, tokens)) + f"""

reserved = {{{", ".join(map(lambda x: repr(x.keyword)+": "+repr(x.__name__),filter(lambda x: isAttrAlpha(x, "keyword", "_"), tokens)))}}}

def t_VAR(t):
   r'[a-zA-Z_][a-zA-Z_\d]*'
   t.type = reserved.get(t.value,'VAR')
   return t

literals = {repr(literals)}

def t_comment(t):"""+r"""
        r'(/\*(.|\n)*?\*/)|(\#.*)'
        t.lexer.lineno += t.value.count('\n')

""" + r"""

def t_lbrace(t):
    r'\{\n*'
    t.type = '{'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_rbrace(t):
    r'\n*\}'
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

"""

