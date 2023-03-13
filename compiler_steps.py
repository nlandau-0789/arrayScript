import re
from arrayscript import operator, Lexer

def presolve_structs(bundle):
    types = [
        "type", # base mataclass (comme en python)
        "num", # pas de limite
        "int", # nb de bits du processeur
        "u64",
        "u32",
        "u16",
        "u8",
        "i64",
        "i32",
        "i16",
        "i8",
        "f32",
        "f64",
        "str", # immutable
        "list", # dynamic length, dynamic type
        "tuple", # static length, dynamic type
        "array", # static length, static type
        "vector", # dynamic length, static type
        "dict", # hashtable
        "any", # pour les déclarations de fonctions
        "generator", 
        "linked_list",
        "doubly_linked_list",
        "deque",
        "heap", # priority queue
        "fibonacci_heap", # priority queue
        "tree", # arbre enraciné normal
        "trie", # arbre lexicographique
        "stack", # FILO
        "queue", # FIFO
        "binary_search_tree", 
        "bitset",
        "set",
        "map", # active le ranked polymorphism
        "range",
    ]
    new_structs = re.findall(r"""struct *([^\ ,]+) *""", bundle.code)
    types.extend(new_structs)
    # print(types)
    return bundle+types

def presolve_operators(bundle):
    operators = [
        operator("+","add",1,"{a} + {b}"),
        operator("-","sub",1,"{a} - {b}"),
        operator("*","mul",2,"{a} * {b}"),
        operator("/","div",2,"{a} / {b}"),
        operator("//","trudiv",2,"{a} // {b}"),
        operator("**","pow",3,"{a} ** {b}"),
        operator("-+-","join",1,"{a} -+- {b}"),
        operator("-|-","split",1,"{a} -|- {b}"),
        operator("->","scan",4,"{a} -> {b}"),
        operator("/>","reduc",4,"{a} /> {b}"),
        operator("&&","bitand",1,"{a} && {b}"),
        operator("||","bitor",1,"{a} || {b}"),
        operator("^","bitxor",1,"{a} ^ {b}"),
        operator("<<","bitshiftleft",1,"{a} << {b}"),
        operator(">>","bitshiftright",1,"{a} >> {b}"),
        operator("and","and",0,"{a} and {b}"),
        operator("or","or",0,"{a} or {b}"),
        operator("xor","xor",0,"{a} xor {b}"),
        operator("~","bitnot",5,"~ {a}"),
        operator("not","not",0,"not {a}"),
        operator("++","incr",5,"{a} ++"),
        operator("--","decr",5,"{a} --"),
        operator("+.","outer",1,"{a} +. {b} {c}"),
        operator("-.","inner",1,"{a} {b} -. {c} {d}"),
        operator("o|","reverse",5,"o| {a}"),
        operator("o-","rotate",4,"{a} o- {b}"),
        operator(".","apply",4,"{a} . {b}"),
        operator("::","compose",7,"{a} :: {b}"),
        operator("()","call",6,"{a} ( {*} )"), # special symbol "*" (cf regex)
        operator("[]","item",6,"{a} [ {+} ]"), # special symbol "+" (cf regex)
        operator("[:]","slice",6,"{a} [ {b} : {c} ]"),
        operator("[::]","slice_step",6,"{a} [ {b} : {c} : {d}]"),
        operator("[]","map",6,"{a} []") # renvoie un objet de type "map"
    ]
    new_operators = re.findall(r"""operator *\{ *(\"""|'''|"|')(.*?)\1, *(\"""|'''|"|')(.*?)\3 *, *(-?(:?[0-9]*[.])?[0-9]+) *\} *\((.*)\)""", bundle.code)
    for idx, e in enumerate(new_operators):
        new_operators[idx] = list(e)
        del new_operators[idx][0]
        del new_operators[idx][1]
        del new_operators[idx][3]
        new_operators[idx][3] = new_operators[idx][3][1:-1]
        operators.append(operator(*new_operators[idx]))
    print(new_operators)
    return bundle+operators

def presolve_functions(bundle):
    functions = []
    new_functions = re.findall(r"""func *\{ *(\"""|'''|"|')(.*?)\1, *(\"""|'''|"|')(.*?)\3 *, *(-?(:?[0-9]*[.])?[0-9]+) *\} *\((.*)\)""", bundle.code)
    for idx, e in enumerate(new_functions):
        new_functions[idx] = list(e)
        del new_functions[idx][0]
        del new_functions[idx][1]
        del new_functions[idx][3]
        new_functions[idx][3] = tuple(map(str.strip, new_functions[idx][3].split(",")))
        functions.append(function(*new_functions[idx]))
    print(new_functions)
    return bundle+functions

def presolve_fstrings(bundle):
    return bundle

def tokenize(bundle):
    l = Lexer(bundle)
    # tokens = l.make_tokens()
    # return bundle+tokens
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