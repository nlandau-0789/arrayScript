import re

def presolve_structs(bundle):
    types = [
        "int",
        "str",
        "list",
        "tuple",
        "array",
        "vector",
        "dict"
    ]
    new_structs = re.findall(r"""struct *([^\ ,]+) *""", bundle.code)
    types.extend(new_structs)
    # print(types)
    return bundle+types

def presolve_operators(bundle):
    operators = {
        "lmonads" :{},
        "rmonads" :{},
        "dyads" :{}
    }
    new_operators = re.findall(r"""operator *\{ *(\"""|'''|"|')(.*?)\1, *(\"""|'''|"|')(.*?)\3 *, *(-?\d+) *\} *\(([^\ ,]*?) *(?:, *([^\ ,]*?))?\)""", bundle.code)
    for idx, e in enumerate(new_operators):
        new_operators[idx] = list(e)
        del new_operators[idx][0:3:2]
    # print(new_operators)
    return bundle+operators

def presolve_fstrings(bundle):
    return bundle

def tokenize(bundle):
    return bundle

def presolve_exprs(bundle):
    return bundle

def presolve_pipings(bundle):
    return bundle

def write_macros(bundle):
    return bundle

def make_ast(bundle):
    return bundle

def make_cpp(bundle):
    return bundle