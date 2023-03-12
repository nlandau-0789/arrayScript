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
        print(f'searching : {key}')
        if key == "":
            return True
        if not isinstance(key, str):
            raise ValueError(f"[key] (=<{key}>) was not a string")
        if not (key[0] in self.data):
            return False
        return self.data[key[0]].contains(key[1:])

    def __contains__(self, key):
        return self.contains(key)

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

class Token():
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'

class Lexer():
    def __init__(self, fn, code, bundle):
        self.fn = fn
        self.code = code
        self.bundle = bundle
        self.pos = Position(-1, 0, -1, fn, code)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.code[self.pos.idx] if self.pos.idx < len(self.code) else None
    
    def make_tokens(self):
        tokens = []
        vars = []

        while self.curr_char != None:
            if self.curr_char in ' \t':
                self.advance()
            elif True:
                self.advance()

        return tokens

if __name__ == '__main__':
    r = RadixTree()
    print("a" in r)
    r += "abc"
    print("ab" in r)
    print("ac" in r)
    r += "acg"
    print("acg" in r)
