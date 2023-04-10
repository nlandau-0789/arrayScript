from base_compiler import tokens, literals, operators, types, consts_types, funcs
import extra_compile_data
from pprint import pprint

def get_translater(code):
    operators.extend(extra_compile_data.get_new_operators(code))
    types.extend(extra_compile_data.get_new_structs(code))
    return \
r"""

from Utils.array_functions import flatten
from base_compiler import operator
# import json

def translate(stmt, indent = 0):
    if len(stmt) == 1:
        # print(stmt)
        return stmt[0]
    if stmt[0] == "struct":
        return "\t"*indent + "struct "+ stmt[1][1] +" {\n" + "\t"*(indent+1) + (";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]]))+ ";\n" + "\t"*indent + "};"
    if stmt[0] == "declaration":
        type_ = stmt[1][1]
        return [type_+" "+name[1] for name in stmt[2]]
    if stmt[0] == "call":
        # return "\t"*indent + stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
        if stmt[1] == "operator_apply":
            stmt[2][1][2].insert(0, stmt[2][0])
            return translate(stmt[2][1])
        return stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
    if stmt[0] == "const":
        return str(stmt[1])
    if stmt[0] == "assign":
        if len(stmt[1]) == 1:
            return "auto " + translate(stmt[1][0], indent+1) + " = " + translate(stmt[2], indent+1)
        return "auto tmp = " + translate(stmt[2], indent+1) + "; auto " + "; auto ".join(translate(i, indent+1)+" = temp["+ str(idx) +"]" for idx, i in enumerate(stmt[1]))
    if stmt[0] == "var":
        return stmt[1]
    if stmt[0] == "return":
        return "return "+translate(stmt[1], indent+1)
    if stmt[0] == "func":
        return "\t"*indent+"auto " + stmt[1] + "("+ (", ").join(flatten([translate(i, indent+1) for i in stmt[2]])) +"){\n"+"\t"*(indent+1)+(";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[3]]))+";\n"+"\t"*indent+"}"
    if stmt[0] == "operator":
        op = operator(*(eval(str(v[1])) for v in stmt[1]))
        return \
f'''
template<{", ".join("typename "+chr(65+i) for i in range(op.nb_args-1))}>
auto {op.__name__}({", ".join(chr(65+i)+" "+op.args[i] for i in range(op.nb_args-1))})''' + "{\n" + "\t"*(indent+1) + (";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]])) + ";\n" + "\t"*indent + "}"
    if stmt[0] == "lambda":
        req = ""
        return "["+", ".join(req)+"](auto "+ (", auto ").join(flatten([translate(i, indent+1) for i in stmt[1]])) +"){return "+translate(stmt[2], indent+1)+";}"
    if stmt[0] == "for":
        program = ""
        if len(stmt[1]) == 1:
            program = "for (auto&& "+translate(stmt[1][0])+ " : "+translate(stmt[2])+"){\n"
        else :
            program = "for (auto&& "+"["+", ".join(translate(i) for i in stmt[1])+"] : "+translate(stmt[2])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[3])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "while":
        program = "while ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "if":
        program = "if ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "elif":
        program = "else if ("+translate(stmt[1])+"){\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[2])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    if stmt[0] == "else":
        program = "else {\n"
        program += "\n".join("\t"*(indent+1) + (tmp:=translate(i, indent+1)) + ";\n"*(len(tmp) and (not tmp[-1] in '};')) for i in stmt[1])
        return program+("\n" if program[-1] == "}" else "") + "\t"*indent+"}"
    # if stmt[0] == "del":
    #     pass
    return ""
    


def run(p):
    # print(p)
    program = "#include <arrs.cpp>\n\nusing namespace arrs;\nusing namespace operators;\nusing namespace types;\nusing namespace funcs;\n\n"
    for i in p:
        program += translate(i)
        program += ";"*(not program[-1] in '};') 
        program += "\n\n"
    with open(file_destination, "w", encoding="utf-8") as f:
        f.write(program)

def compile(code, filename):
    global file_destination
    file_destination = filename
    parser.parse(code)
    
"""