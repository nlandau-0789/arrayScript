import re

class operator():
    types = ["monadic", "dyadic"]
    def __init__(self,symbol,name,priority,args):
        self.symbol = symbol
        self.name = f"__{name}_operator_"
        self.priority = int(priority)
        if isinstance(args, int):
            self.type = self.types[args]
        elif len(args) > 2 or len(args) == 0:
            raise ValueError("operators can only have one or two arguments")
        elif len(args) == 1:
            self.type = "monadic"
        else :
            self.type = "dyadic"
    
    def __repr__(self):
        return f"<{self.symbol=}; {self.name=}; {self.priority=}; {self.type=}>".replace("self.","").replace("="," = ")

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
    operators = [
        operator("+","add",1,1),
        operator("-","sub",1,1),
        operator("*","mul",2,1),
        operator("/","div",2,1),
        operator("//","trudiv",2,1),
        operator("**","pow",3,1),
        operator("-+-","join",1,1),
        operator("-|-","split",1,1),
        operator("->","scan",4,1),
        operator("/>","reduc",4,1),
        operator("&&","bitand",1,1),
        operator("||","bitor",1,1),
        operator("^","bitxor",1,1),
        operator("<<","bitshiftleft",1,1),
        operator(">>","bitshiftright",1,1),
        operator("and","and",0,1),
        operator("or","or",0,1),
        operator("xor","xor",0,1),
        operator("~","bitnot",5,0),
        operator("not","not",0,0),
        operator("++","incr",5,0),
        operator("--","decr",5,0),
        operator("+.","outer",6,0),
        # operator("-.","inner",6,1),
    ]
    new_operators = re.findall(r"""operator *\{ *(\"""|'''|"|')(.*?)\1, *(\"""|'''|"|')(.*?)\3 *, *(-?\d+) *\} *\((.*)\)""", bundle.code)
    for idx, e in enumerate(new_operators):
        new_operators[idx] = list(e)
        del new_operators[idx][0:3:2]
        new_operators[idx][3] = tuple(map(str.strip, new_operators[idx][3].split(",")))
        operators.append(operator(*new_operators[idx]))
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