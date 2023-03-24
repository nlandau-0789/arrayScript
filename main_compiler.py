from lexer_compilator import get_compilator

with open("exemple.arrs", "r", encoding="utf-8") as f:
    code = f.read()

with open("lexer.py", "w", encoding="utf-8") as f:
    f.write(get_compilator(code))