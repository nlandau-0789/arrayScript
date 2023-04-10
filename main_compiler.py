def compile(filename, destination=None):
    from lexer_compiler import get_lexer
    from parser_compiler import get_parser
    from translater_compiler import get_translater
    from pprint import pprint

    with open(filename, "r", encoding="utf-8") as f:
        code = f.read().strip()

    with open("compiler.py", "w", encoding="utf-8") as f:
        f.write(get_lexer(code))

    with open("compiler.py", "a", encoding="utf-8") as f:
        f.write(get_parser(code))

    with open("compiler.py", "a", encoding="utf-8") as f:
        f.write(get_translater(code))

    # from compiler import lexer

    # lexer.input(code)
    # pprint(list(lexer))

    # from compiler import parser

    # parser.parse(code)

    from compiler import compile
    compile(code, filename.replace(".arrs", ".cpp") if destination is None else destination)
