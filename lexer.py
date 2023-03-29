from ply import lex
from pprint import pprint

tokens = ('NUM', 'FLOAT', 'STRING_3SQ', 'STRING_3DQ', 'STRING_SQ', 'STRING_DQ', 'for', 'while', 'if', 'else', 'elif', 'func', 'struct', 'operator', 'return', 'break', 'continue', 'del', 'true', 'false', 'lambda', 'pass', 'operator_add', 'operator_sub', 'operator_mul', 'operator_div', 'operator_trudiv', 'operator_pow', 'operator_join', 'operator_split', 'operator_scan', 'operator_reduc', 'operator_bitand', 'operator_bitor', 'operator_bitxor', 'operator_bitshiftleft', 'operator_bitshiftright', 'operator_and', 'operator_or', 'operator_xor', 'operator_contains', 'operator_bitnot', 'operator_not', 'operator_incr', 'operator_decr', 'operator_outer', 'operator_inner', 'operator_reverse', 'operator_rotate', 'operator_apply', 'operator_compose', 'operator_over', 'operator_map', 'operator_sorted_incr', 'operator_sorted_decr', 'operator_less_than', 'operator_less_than_equals', 'operator_greater_than', 'operator_greater_than_equals', 'operator_equals', 'operator_not_equals', 'operator_smallest', 'operator_greatest', 'type_type', 'type_num', 'type_any', 'type_u64', 'type_u32', 'type_u16', 'type_u8', 'type_i64', 'type_i32', 'type_i16', 'type_i8', 'type_f32', 'type_f64', 'type_str', 'type_list', 'type_tuple', 'type_array', 'type_vector', 'type_dict', 'type_generator', 'type_linked_list', 'type_doubly_linked_list', 'type_deque', 'type_heap', 'type_fibonacci_heap', 'type_tree', 'type_trie', 'type_stack', 'type_queue', 'type_binary_search_tree', 'type_bitset', 'type_set', 'type_map', 'type_range', 'type_bad_struct', 'operator_goodname', 'operator_s_combinator', 'operator_goodname2', 'VAR')

def t_NUM(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r"-?\d+\.\d+"
    t.value = float(t.value)
    return t

def t_STRING_3SQ(t):
    r"""\'\'\'([^\\\n]|(\\.))*?\'\'\'"""
    return t

def t_STRING_3DQ(t):
    r'''\"\"\"([^\\\n]|(\\.))*?\"\"\"'''
    return t

def t_STRING_SQ(t):
    r"""\'([^\\\n]|(\\.))*?\'"""
    return t

def t_STRING_DQ(t):
    r"""\"([^\\\n]|(\\.))*?\""""
    return t
t_for = r'''for'''
t_while = r'''while'''
t_if = r'''if'''
t_else = r'''else'''
t_elif = r'''elif'''
t_func = r'''func'''
t_struct = r'''struct'''
t_operator = r'''operator'''
t_return = r'''return'''
t_break = r'''break'''
t_continue = r'''continue'''
t_del = r'''del'''
t_true = r'''true'''
t_false = r'''false'''
t_lambda = r'''lambda'''
t_pass = r'''pass'''
t_operator_add = r'''\+'''
t_operator_sub = r'''\-'''
t_operator_mul = r'''\*'''
t_operator_div = r'''//'''
t_operator_trudiv = r'''/'''
t_operator_pow = r'''\*\*'''
t_operator_join = r'''\-\+\-'''
t_operator_split = r'''\-\|\-'''
t_operator_scan = r'''\->'''
t_operator_reduc = r'''/>'''
t_operator_bitand = r'''\&\&'''
t_operator_bitor = r'''\|\|'''
t_operator_bitxor = r'''\^'''
t_operator_bitshiftleft = r'''<<'''
t_operator_bitshiftright = r'''>>'''
t_operator_and = r'''and'''
t_operator_or = r'''or'''
t_operator_xor = r'''xor'''
t_operator_contains = r'''in'''
t_operator_bitnot = r'''\~'''
t_operator_not = r'''not'''
t_operator_incr = r'''\+\+'''
t_operator_decr = r'''\-\-'''
t_operator_outer = r'''\+\.'''
t_operator_inner = r'''\-\.'''
t_operator_reverse = r'''<\|>'''
t_operator_rotate = r'''\-o\-'''
t_operator_apply = r'''\.'''
t_operator_compose = r'''::'''
t_operator_over = r'''\.\.'''
t_operator_map = r'''\[\]'''
t_operator_sorted_incr = r'''>_>'''
t_operator_sorted_decr = r'''<_<'''
t_operator_less_than = r'''<'''
t_operator_less_than_equals = r'''<='''
t_operator_greater_than = r'''>'''
t_operator_greater_than_equals = r'''>='''
t_operator_equals = r'''=='''
t_operator_not_equals = r'''!='''
t_operator_smallest = r'''<\?'''
t_operator_greatest = r'''>\?'''
t_type_type = r'''type'''
t_type_num = r'''num'''
t_type_any = r'''any'''
t_type_u64 = r'''u64'''
t_type_u32 = r'''u32'''
t_type_u16 = r'''u16'''
t_type_u8 = r'''u8'''
t_type_i64 = r'''i64'''
t_type_i32 = r'''i32'''
t_type_i16 = r'''i16'''
t_type_i8 = r'''i8'''
t_type_f32 = r'''f32'''
t_type_f64 = r'''f64'''
t_type_str = r'''str'''
t_type_list = r'''list'''
t_type_tuple = r'''tuple'''
t_type_array = r'''array'''
t_type_vector = r'''vector'''
t_type_dict = r'''dict'''
t_type_generator = r'''generator'''
t_type_linked_list = r'''linked_list'''
t_type_doubly_linked_list = r'''doubly_linked_list'''
t_type_deque = r'''deque'''
t_type_heap = r'''heap'''
t_type_fibonacci_heap = r'''fibonacci_heap'''
t_type_tree = r'''tree'''
t_type_trie = r'''trie'''
t_type_stack = r'''stack'''
t_type_queue = r'''queue'''
t_type_binary_search_tree = r'''binary_search_tree'''
t_type_bitset = r'''bitset'''
t_type_set = r'''set'''
t_type_map = r'''map'''
t_type_range = r'''range'''
t_type_bad_struct = r'''bad_struct'''
t_operator_goodname = r'''op'''
t_operator_s_combinator = r'''S'''
t_operator_goodname2 = r'''op2'''

reserved = {'for': 'for', 'while': 'while', 'if': 'if', 'else': 'else', 'elif': 'elif', 'func': 'func', 'struct': 'struct', 'operator': 'operator', 'return': 'return', 'break': 'break', 'continue': 'continue', 'del': 'del', 'true': 'true', 'false': 'false', 'lambda': 'lambda', 'pass': 'pass', 'and': 'operator_and', 'or': 'operator_or', 'xor': 'operator_xor', 'in': 'operator_contains', 'not': 'operator_not', 'type': 'type_type', 'num': 'type_num', 'any': 'type_any', 'str': 'type_str', 'list': 'type_list', 'tuple': 'type_tuple', 'array': 'type_array', 'vector': 'type_vector', 'dict': 'type_dict', 'generator': 'type_generator', 'linked_list': 'type_linked_list', 'doubly_linked_list': 'type_doubly_linked_list', 'deque': 'type_deque', 'heap': 'type_heap', 'fibonacci_heap': 'type_fibonacci_heap', 'tree': 'type_tree', 'trie': 'type_trie', 'stack': 'type_stack', 'queue': 'type_queue', 'binary_search_tree': 'type_binary_search_tree', 'bitset': 'type_bitset', 'set': 'type_set', 'map': 'type_map', 'range': 'type_range', 'bad_struct': 'type_bad_struct', 'op': 'operator_goodname', 'S': 'operator_s_combinator'}

def t_VAR(t):
   r'[a-zA-Z_][a-zA-Z_\d]*'
   t.type = reserved.get(t.value,'VAR')
   return t

literals = ',()[]{}:=#'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# while True:
#     inp = input(">>> ")
#     if inp in {"exit", "quit", "kill"}:
#         break
#     lex.input(inp)
#     pprint(list(lexer))

