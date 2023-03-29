from lexer_compiler import get_lexer
from parser_compiler import get_parser
from pprint import pprint

with open("exemple.arrs", "r", encoding="utf-8") as f:
    code = f.read()

with open("lexer.py", "w", encoding="utf-8") as f:
    f.write(get_lexer(code))

with open("parser.py", "w", encoding="utf-8") as f:
    f.write(get_parser(code))

from lexer import lexer

lexer.input(code)
pprint(list(lexer))

# from parser import parser

# parser.parse(code)
# pprint(list(parser))