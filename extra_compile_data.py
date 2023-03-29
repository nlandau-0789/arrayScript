def get_new_structs(code):
    import re
    from base_compiler import type_
    new_structs = re.findall(r"""struct *([^\ ,]+) *""", code)
    new_structs = list(map(type_, new_structs))
    return new_structs

def get_new_operators(code):
    import re
    from base_compiler import operator
    new_operators = re.findall(r"""operator *\{ *(\"""|'''|"|')(.*?)\1, *(\"""|'''|"|')(.*?)\3 *, *(-?(:?[0-9]*[.])?[0-9]+) *\} *\((.*)\)""", code)
    for idx, e in enumerate(new_operators):
        new_operators[idx] = list(e)
        del new_operators[idx][0]
        del new_operators[idx][1]
        del new_operators[idx][3]
        new_operators[idx][3] = new_operators[idx][3][1:-1]
    new_operators = list(map(lambda x: operator(*x), new_operators))
    return new_operators

