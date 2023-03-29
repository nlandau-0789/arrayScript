from lexer_compiler import get_lexer
from parser_compiler import get_parser
from pprint import pprint

with open("exemple.arrs", "r", encoding="utf-8") as f:
    code = f.read()

with open("compiler.py", "w", encoding="utf-8") as f:
    f.write(get_lexer(code))

with open("compiler.py", "a", encoding="utf-8") as f:
    f.write(get_parser(code))

from compiler import lexer

lexer.input(code)
pprint(list(lexer))

# from arrs_parser import parser

# parser.parse(code)
# pprint(list(parser))