from base_compiler import types, operators, funcs

arrs_h = open("arrs.h", "w", encoding="utf-8")


arrs_h.write("""
namespace arrs {
""")

arrs_h.write("""
namespace operators {
""")

for i in operators:
    arrs_h.write(\
f"""
template<{", ".join("typename "+chr(65+i) for i in range(i.nb_args))}>
auto {i.__name__}({", ".join(chr(65+i)+" "+chr(97+i) for i in range(i.nb_args))}){{
    
}}
"""
)


arrs_h.write("""
}""")

arrs_h.write("""
}""")

arrs_h.close()