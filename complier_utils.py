def var_name(var):
    import inspect
    lcls = inspect.stack()[2][0].f_locals
    for name in lcls:
        if id(var) == id(lcls[name]):
            return name
    return None

class Bundle(dict):
    import pprint
    def __getattr__(self, name):
        if name in self: return self[name]
        return "Unknown"

    def __iadd__(self, other):
        self[var_name(other)] = other
        return self
    
    def __add__(self, other):
        self[var_name(other)] = other
        return self

    def __repr__(self):
        res = "bundle :\n"
        for key, val in self.items():
            res += f"{key.upper().center(92).replace(' ', '=')}\n{self.pprint.pformat(val)}\n\n"
        return res

class Position():
    def __init__(self, idx, ln, col, filename, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = filename
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
    
    def go_back(self, delta):
        if delta < self.idx:
            raise ValueError("Delta is too big")
        for i in range(delta):
            self.idx -= 1
            self.col -= 1

            if self.col < 0:
                self.ln -= 1
                self.col = len(self.ftxt.splitlines()[self.ln])-1

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

class Error():
    def __init__(self, pos_start, pos_end, error_name = "Unknown", details = "Unknown"):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

from Utils.data_structures import Trie
class TokenDict(Trie):
    def __init__(self):
        super.__init__()
        self.values = {}
    
    def add(self, token, value):
        super().add(token)
        self.values[token] = value

class Token():
    def __init__(self, value = None):
        self.value = value

    def __getattr__(self, name):
        return False
    
    def __repr__(self):
        return f'{self.__class__}{f": {self.value}" if self.value else ""}'

class Keyword(Token):
    pass

class Identifier(Token):
    def __init__(self, name, value="undefined"):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f'{self.__class__} : {self.name} : {self.value}'

class Value(Token):
    def __init__(self, value):
        self.value = value

class Operator(Token):
    def __init__(self,symbol,name,priority,pattern):
        self.symbol = symbol
        self.name = f"operator_::{name}"
        self.priority = float(priority)
        self.pattern = pattern
    
    def __repr__(self):
        return f"<{self.symbol=}; {self.name=}; {self.priority=}; {self.pattern=}>".replace("self.","").replace("="," = ")

class Lexer():
    def __init__(self, code, filename, tokens):
        self.code = code
        self.codeLength = len(code)
        self.filename = filename
        self.tokens = tokens
        self.position = Position(-1, 0, -1, filename, code)
        self.advance()
    
    def advance(self):
        self.position.advance(self.curr_char)
        self.curr_char = self.code[self.position.idx] if self.position.idx < self.codeLength else None

    def go_back(self, delta):
        self.position.go_back(delta)
        self.curr_char = self.code[self.position.idx] if self.position.idx >= 0 else None
    
    def tokenize(self):
        tokens = []
        buffer = ""
        while self.curr_char:
            if self.tokens.containsPrefix(buffer + self.curr_char):
                buffer += self.curr_char
                self.advance()
                continue
            if buffer == "":
                if self.curr_char in {'"', "'"}:
                    tokens.append(self.make_string())
                tokens.append(self.make_value())
        return tokens
        
    def make_value(self):
        bufferStack = []
        buffer = ""
        while not self.curr_char in {" ", "\t", "\n", "=", ",", ")"}:
            for count, buf in enumerate(bufferStack):
                if self.tokens.containsPrefix(buf+self.curr_char):
                    bufferStack[count]+=self.curr_char
                else :
                    bufferStack[count] = None
            bufferStack = [i for i in bufferStack if i]
            if self.tokens.containsPrefix(self.curr_char):
                bufferStack.append(self.curr_char)
            for count, buf in enumerate(bufferStack):
                if buf in self.tokens.values \
                and (not (buf.isalpha())) \
                and (not (buffer.isnumeric() and buf == ".")):
                    buffer = buffer[:-len(buf)]
                    self.go_back(len(buf)-1)
                    return buffer
            buffer += self.curr_char
            self.advance()
        from Utils.string_functions import isnumber
        if not isnumber(buffer):
            self.tokens.add(buffer, Identifier(buffer))
            return Identifier(buffer)
        else :
            return Value(buffer)

    def make_string(self):
        string = ""
        end_if = self.curr_char
        self.advance()
        while self.curr_char == end_if:
            end_if += self.curr_char
            self.advance()
        count = 0
        while count < len(end_if):
            if self.curr_char == "\\":
                self.advance()
                string += self.curr_char
                count = 0
                self.advance()
            string += self.curr_char
            self.advance
            if self.curr_char != end_if[0]:
                count = 0
            else :
                count += 1
        return Value(string[:-count])