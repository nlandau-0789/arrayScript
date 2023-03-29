from base_compiler import tokens, literals, operators
import extra_compile_data
from pprint import pprint


def isAttrAlpha(s, attr, exceptions = []):
    if not getattr(s, attr, None):
        return False
    t = getattr(s, attr)
    t = "".join(filter(lambda x: not x in exceptions, t))
    return all(map(str.isalpha, t))

def get_parser(code):
    operators.extend(extra_compile_data.get_new_operators(code))
    return \
f"""

# parser = yacc.yacc()

"""
