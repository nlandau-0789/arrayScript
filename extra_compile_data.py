def get_new_structs(code):
    import re
    from base_compiler import type_
    new_structs = re.findall(r"""struct *([^\ ,]+) *""", code)
    new_structs = list(map(type_, new_structs))
    return new_structs

def get_new_operators(code):
    import re
    from base_compiler import operator
    new_operators = re.findall(r"""operator *\((.*)\)""", code)
    new_operators = list(map(lambda x: list(map(lambda y: eval(str.strip(y)), x)), (x.split(",") for x in new_operators)))
    new_operators = list(map(lambda x: operator(*x), new_operators))
    return new_operators

