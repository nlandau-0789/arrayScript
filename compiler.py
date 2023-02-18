import sys
import compiler_steps as cs
from compiler_bundle import bundle

def parse(file_name):
    refining_steps = [
        cs.presolve_structs,
        cs.presolve_operators,
        cs.presolve_fstrings,
        cs.tokenize,
        cs.presolve_exprs,
        cs.presolve_pipings,
        cs.write_macros,
        cs.make_ast,
        cs.make_cpp
    ]
    arrs_code = bundle()

    with open(file_name, "r", encoding="utf-8") as f:
        arrs_code["code"] = f.read()
    
    for refine in refining_steps:
        arrs_code = refine(arrs_code)
    
    with open(file_name.split(".arrs")[0]+".cpp", "w") as f:
        f.write(arrs_code.code or " ")

    print(arrs_code)

if __name__=="__main__":
    file_name = sys.argv[1] if len(sys.argv) >= 2 else "exemple.arrs"
    parse(file_name)