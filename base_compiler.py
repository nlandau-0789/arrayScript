import re

class keyword():
    def __init__(self, name):
        self.__name__ = name
        self.tokenizer = f"""t_{self.__name__} = r'''{re.escape(name)}'''"""
        self.keyword = name
    
    def __repr__(self):
        return self.__name__

keywords = [
    keyword("for"),
    keyword("while"),
    keyword("if"),
    keyword("else"),
    keyword("elif"),
    keyword("func"),
    keyword("struct"),
    keyword("operator"),
    keyword("return"),
    keyword("break"),
    keyword("continue"),
    keyword("del"),
    keyword("lambda"),
    keyword("pass"),
]

class type_():
    def __init__(self, name):
        self.__name__ = "type_"+name
        self.tokenizer = f"""t_{self.__name__} = r'''{re.escape(name)}'''"""
        self.keyword = name
    
    def __repr__(self):
        return self.__name__

types = [
    type_('type'), # base mataclass (comme en python)
    type_('num'), # pas de limite
    type_('bool'), # pas de limite
    type_('any'), # pour les déclarations de fonctions
    type_('u64'), 
    type_('u32'), 
    type_('u16'), 
    type_('u8'), 
    type_('i64'), 
    type_('i32'), 
    type_('i16'), 
    type_('i8'), 
    type_('f32'), 
    type_('f64'), 
    type_('str'), # immutable
    type_('list'), # dynamic length, dynamic type
    type_('tuple'), # static length, dynamic type
    type_('array'), # static length, static type
    type_('vector'), # dynamic length, static type
    type_('dict'), 
    type_('generator'), 
    type_('linked_list'), 
    type_('doubly_linked_list'), 
    type_('deque'), 
    type_('heap'), 
    type_('fibonacci_heap'), 
    type_('tree'), # arbre enraciné normal
    type_('trie'), 
    type_('stack'), 
    type_('queue'), 
    type_('binary_search_tree'), 
    type_('bitset'), 
    type_('set'), 
    type_('map'), # active le ranked polymorphism
    type_('range')
]

literals = ",()[]{}:=;"

class NUM():
    tokenizer = r"""
def t_NUM(t):
    r"-?\d+"
    t.value = int(t.value)
    return t"""

class FLOAT():
    tokenizer = r"""
def t_FLOAT(t):
    r"-?\d+\.\d+"
    t.value = float(t.value)
    return t"""

class STRING_3SQ():
    match_string = r"\'\'\'([^\\\n]|(\\.))*?\'\'\'"
    tokenizer = rf'''
def t_STRING_3SQ(t):
    r"""{match_string}"""
    t.value = json.dumps(eval(t.value))
    return t'''

class STRING_3DQ():
    match_string = r'\"\"\"([^\\\n]|(\\.))*?\"\"\"'
    tokenizer = rf"""
def t_STRING_3DQ(t):
    r'''{match_string}'''
    t.value = json.dumps(eval(t.value))
    return t"""

class STRING_SQ():
    match_string = r"\'([^\\\n]|(\\.))*?\'"
    tokenizer = rf'''
def t_STRING_SQ(t):
    r"""{match_string}"""
    t.value = json.dumps(eval(t.value))
    return t'''

class STRING_DQ():
    match_string = r'\"([^\\\n]|(\\.))*?\"'
    tokenizer = rf'''
def t_STRING_DQ(t):
    r"""{match_string}"""
    t.value = json.dumps(eval(t.value))
    return t'''

consts_types = [
    FLOAT,
    NUM,
    STRING_3SQ,
    STRING_3DQ,
    STRING_SQ,
    STRING_DQ,
    keyword("true"),
    keyword("Null"),
    keyword("false"),
]

class operator():
    def __init__(self,symbol,name,priority,pattern):
        self.symbol = symbol
        self.__name__ = f"operator_{name}"
        self.priority = float(priority)
        self.return_value = []
        self.pattern = []
        buffer = ""
        state = 0
        self.nb_args = 0
        found_symbol = False
        self.args = []
        def check_symbol():
            nonlocal buffer, found_symbol
            if buffer:
                if buffer != self.symbol:
                    raise ValueError("presence of "+buffer+" symbol in "+name+"'s definition, which is not correct")
                if found_symbol:
                    raise ValueError("presence of symbol twice in "+name+"'s definition, which is not correct")
                self.pattern.append(self.__name__)
                self.nb_args += 1
                # self.return_value.insert(0, self.nb_args)
                found_symbol = True
                buffer = ""
        for i in pattern:
            # print(f"{state=}")
            if i == " ":
                check_symbol()
                continue
            if i == "{":
                if state == 1 or state > 2:
                    raise ValueError("should have closed '{' in operator "+name+"'s definition")
                    # print("found symbol :", buffer)
                state += 1
                check_symbol()
                continue
            if i == "}":
                if state == 0:
                    raise ValueError("should have opened '{' in operator "+name+"'s definition")
                self.pattern.append("expr" if state == 1 else "OPERATOR")
                state = 0
                self.nb_args += 1
                self.return_value.append(self.nb_args)
                self.args.append(buffer)
                buffer = ""
                continue
            if i == "§":
                if state > 0:
                    raise ValueError("should have closed '{' in operator "+name+"'s definition")
                    # print("found symbol :", buffer)
                state = 2
                # print("opened '<' in operator "+name+"'s definition", f"{state=}")
                check_symbol()
                continue
            buffer += i
        check_symbol()
        self.pattern = " ".join(self.pattern)
        self.return_value = f"p[0] = ('call', '{self.__name__}', [{', '.join('p['+str(i)+']' for i in self.return_value)}])"
        self.tokenizer = f"""t_{self.__name__} = r'''{re.escape(symbol)}'''"""
        self.keyword = symbol
    
    def __repr__(self):
        return f"<{self.symbol=}; {self.__name__=}; {self.priority=}; {self.pattern=}>".replace("self.","").replace("="," = ")

operators = [
    operator("+","add",1,"{a} + {b}"),
    operator("-","sub",1,"{a} - {b}"),
    operator("*","mul",2,"{a} * {b}"),
    operator("//","div",2,"{a} // {b}"),
    operator("/","trudiv",2,"{a} / {b}"),
    operator("**","pow",3,"{a} ** {b}"),
    operator("-+-","join",1,"{a} -+- {b}"),
    operator("-|-","split",1,"{a} -|- {b}"),
    operator("->","scan",4,"§{a} -> {b}"),
    operator("/>","reduc",4,"§{a} /> {b}"),
    operator("&&","bitand",1,"{a} && {b}"),
    operator("||","bitor",1,"{a} || {b}"),
    operator("^","bitxor",1,"{a} ^ {b}"),
    operator("<<","bitshiftleft",1,"{a} << {b}"),
    operator(">>","bitshiftright",1,"{a} >> {b}"),
    operator("and","and",0,"{a} and {b}"),
    operator("or","or",0,"{a} or {b}"),
    operator("xor","xor",0,"{a} xor {b}"),
    operator("in","contains",0,"{a} in {b}"),
    operator("~","bitnot",5,"~ {a}"),
    operator("not","not",0,"not {a}"),
    operator("++","incr",5,"{a} ++"),
    operator("--","decr",5,"{a} --"),
    operator("+.","outer",1,"{a} +. §{b} {c}"),
    operator("-.","inner",1,"{a} §{b} -. §{c} {d}"),
    operator("<|>","reverse",5,"<|> {a}"),
    operator("-o-","rotate",4,"{a} -o- {b}"),
    operator(".","apply",4,"{a} . {b}"),
    operator("::","compose",7.5,"{a} :: {b}"),
    operator("..","over",7,"{a} .. {b}"),
    # operator("()","call",6,"{a} ( {*} )"), # special symbol "*" (cf regex)
    # operator("[]","item",6,"{a} [ {+} ]"), # special symbol "+" (cf regex)
    # operator("[:]","slice",6,"{a} [ {b} : {c} ]"),
    # operator("[::]","slice_step",6,"{a} [ {b} : {c} : {d}]"),
    operator("[]","map",6,"{a} []"), # renvoie un objet de type "map"
    operator(">_>","sorted_incr",5,">_> {a}"),
    operator("<_<","sorted_decr",5,"<_< {a}"),
    operator("<", "less_than",0,"{a} < {b}"),
    operator("<=", "less_than_equals",0,"{a} <= {b}"),
    operator(">", "greater_than",0,"{a} > {b}"),
    operator(">=", "greater_than_equals",0,"{a} >= {b}"),
    operator("==", "equals",0,"{a} == {b}"),
    operator("!=", "not_equals",0,"{a} != {b}"),
    operator("<?", "smallest",0,"{a} <? {b}"),
    operator(">?", "greatest",0,"{a} >? {b}"),
    # operator("Ov", "floor",5,"Ov {a}"),
    # operator("O^", "ceil",5,"O^ {a}"),
]

funcs = []

tokens = consts_types + keywords + operators + types + funcs

# from pprint import pprint
# pprint([(x.pattern, x.return_value) for x in operators])