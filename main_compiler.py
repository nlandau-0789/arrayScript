from lexer_compiler import get_lexer
from parser_compiler import get_parser
from pprint import pprint

with open("exemple.arrs", "r", encoding="utf-8") as f:
    code = f.read()

with open("arrs_lexer.py", "w", encoding="utf-8") as f:
    f.write(get_lexer(code))

with open("arrs_parser.py", "w", encoding="utf-8") as f:
    f.write(get_parser(code))

from arrs_lexer import lexer

lexer.input(code)
pprint(list(lexer))

# from arrs_parser import parser

# parser.parse(code)
# pprint(list(parser))