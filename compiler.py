from typing import *
import re

# les operators doivent avoir leur symbole comme clé et leur nom comme valeur ("+": ("_operator_add",<priorité>))
operators = {
    
}

regex_number = r"-?\d+\.?\d*"
regex_string = r"""(f?)(\"""|'''|"|')(?:(?!\2)(?:\\.|[^\\]))*\2"""
regex_fstrings = """f(\"""|'''|"|')(((.*?)(\{.*?\}))*)\1""" #group 2

class Pipe():
    def __init__(self, data):
        self.result = data
    def __repr__(self):
        return self.result
    def remove_comments(self):
        text = self.result
        idx = 0
        res = ""
        while idx < len(text):
            next_comment = min([float("inf")]+list(filter(lambda x: x >= 0,(text.find("#", idx), text.find("/*", idx)))))
            if next_comment == float("inf"):
                res += text[idx:]
                return Pipe(res)
            res += text[idx:next_comment]
            if text[next_comment] == "#":
                idx = text.find("\n", next_comment)
                if idx == -1:
                    return Pipe(res)
            else :
                idx = text.find("*/", next_comment) + 2
                if idx == 1:
                    print("Dernier commentaire non fermé")
                    raise
        return Pipe(res)
    def remove_newlines_in_parenthesis(self):
        # print(self.result)
        res = ""
        toggle = 0
        for i in self.result:
            if i == "(":
                toggle += 1
            if i == ")":
                toggle -= 1
            if not (toggle and i == "\n"):
                res+=i
        # print(res)
        return Pipe(res)
    def split_lines(self):
        return Pipe(self.result.splitlines())
    def rstrip_lines(self):
        return Pipe(list(map(str.rstrip, self.result)))
    def remove_empty_lines(self):
        return Pipe(list(filter(bool, self.result)))
    def cleanup(self):
        return Pipe("\n".join(self.remove_comments().remove_newlines_in_parenthesis().split_lines().rstrip_lines().remove_empty_lines().result))
    def presolve_operators(self):
        global operators
        new_operators = re.findall(r"""operator *\{ *(\"""|'''|"|')(.*?)\1 *, *(\"""|'''|"|')(.*?)\3 *, *(-?\d+\.?\d*) *\}""", self.result)
        #print(new_operators)
        #open("output","w").write(f"""operator *\\{{ *{regex_string} *, *{regex_string} *, *{regex_number} *\\}}""")
        new_operators = map(lambda op: (op[1],op[3],int(op[4])), new_operators)
        for symbol, name, priority in new_operators:
            operators[symbol] = ("_operator_"+name, priority)
        return self  
    def solve_format_strings(self):
        pass

def find_indentations(lines: List[str]):
    first_indented_line = list(filter(lambda x: x[0] in {"\t"," "}, lines))[0]
    get_indent = lambda line: line[:line.index(line.strip()[0])]
    indentation = get_indent(first_indented_line)
    return list(map(lambda line: len(get_indent(line))//len(indentation), lines)), indentation


class ast_node():
    pass
class ast_for(ast_node):
    pass
class ast_while(ast_node):
    pass
class ast_block(ast_node):
    blocks = {
        "for": ast_for,
        "while": ast_while,
    }
    
    def __new__(self, line, children):
        name = line.split()[0]
        try :
            return self.blocks[name](line, children)
        except :
            print(f"Keyword inconnu : {name}")
            raise



def make_ast(file):
    raw_text = file.read()
    lines = Pipe(raw_text).cleanup()
    print(lines)
    indents, indent = find_indentations(lines.result.split('\n'))
    print(indents)
    lines = lines.presolve_operators()
    print(operators)

if __name__=="__main__":
    file = open("exemple.arrs", "r")
    make_ast(file)