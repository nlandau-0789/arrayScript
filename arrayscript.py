class operator():
    types = ["monadic", "dyadic"]
    def __init__(self,symbol,name,priority,args):
        self.symbol = symbol
        self.name = f"__{name}_operator_"
        self.priority = float(priority)
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

class RadixTree():
    def __init__(self):
        self.data = {}
    
    def add(self, key):
        if not isinstance(key, str):
            raise ValueError(f"[key] (=<{key}>) was not a string")
        if key == "":
            return self
        if key[0] in self.data:
            self.data[key[0]].add(key[1:])
        else :
            self.data[key[0]] = RadixTree()
            self.data[key[0]].add(key[1:])
        return self
    
    def __add__(self, key):
        return self.add(key)
    
    def contains(self, key):
        # print(f'searching : {key}')
        if key == "":
            return True
        if not isinstance(key, str):
            raise ValueError(f"[key] (=<{key}>) was not a string")
        if not (key[0] in self.data):
            return False
        return self.data[key[0]].contains(key[1:])

    def __contains__(self, key):
        return self.contains(key)

    @classmethod
    def test(cls):
        r = RadixTree()
        assert ("a" in r) == False
        r += "abc"
        assert ("ab" in r) == True
        assert ("ac" in r) == False
        r += "acg"
        assert ("acg" in r) == True
        print("RadixTree : all tests passed")

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

# class Token():
#     def __init__(self, type_, value=None):
#         self.type = type_
#         self.value = value
    
#     def __repr__(self):
#         if self.value: return f'{self.type}: {self.value}'
#         return f'{self.type}'
    
#     @classmethod
#     def init_radixtree(cls, bundle):
#         for op in bundle.operators:

        

class Lexer():
    def __init__(self, bundle):
        self.fn = bundle.fn
        self.code = bundle.code
        self.bundle = bundle
        self.pos = Position(-1, 0, -1, self.fn, self.code)
        self.curr_char = None
        self.known_tokens = {}
        for i in bundle.operators:
            self.known_tokens[i.symbol] = i
        for i in bundle.types:
            self.known_tokens[i] = i
        self.known_tokens_tree = RadixTree()
        for i in self.known_tokens:
            self.known_tokens_tree += i
        self.advance()

    def advance(self):
        print(self.pos.idx, self.curr_char)
        self.pos.advance(self.curr_char)
        self.curr_char = self.code[self.pos.idx] if self.pos.idx < len(self.code) else None
    
    def make_tokens(self):
        tokens = []
        buffer = ""
        in_comment = False

        while self.curr_char != None:
            while self.curr_char in " \t":
                self.advance()
            while buffer+self.curr_char in self.known_tokens_tree:
                print("while : "+buffer+self.curr_char)
                buffer+=self.curr_char
                self.advance()
            if buffer == "":
                while not self.curr_char in "=":
                    self.advance()
                continue
            tokens.append(self.known_tokens[buffer])

        return tokens

if __name__ == '__main__':
    # RadixTree.test()
    pass
