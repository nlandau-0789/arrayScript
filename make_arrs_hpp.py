from base_compiler import types, operators, funcs

arrs_h = open("arrs.hpp", "x", encoding="utf-8")


arrs_h.write("""
namespace arrs {
""")

# begin operators namespace
arrs_h.write("""
namespace operators {
""")

for i in operators:
    arrs_h.write(\
f"""
template<{", ".join("typename "+chr(65+i) for i in range(i.nb_args-1))}>
auto {i.__name__}({", ".join(chr(65+i)+" "+chr(97+i) for i in range(i.nb_args-1))}){{
    
}}
"""
)

arrs_h.write("""
}""")
# end operators namespace

# begin types namespace
arrs_h.write("""
namespace types {
""")

for i in types:
    arrs_h.write(\
f"""
class {i.__name__}{{
public :
    {i.__name__}(){{}}
    ~{i.__name__}(){{}}
}};
"""
)

arrs_h.write("""
}""")
# end types namespace

# begin funcs namespace
arrs_h.write("""
namespace funcs {
""")
for i in types:
    arrs_h.write(\
f"""
template<typename T>
arrs::types::{i.__name__} make_{i.__name__}(T){{}};
"""
)

for i in funcs:
    arrs_h.write(\
f"""
class {i}{{
public :
    {i}(){{}}
    ~{i}(){{}}
}};
"""
)

arrs_h.write("""
}""")
# end funcs namespace

arrs_h.write("""
}""")

arrs_h.close()