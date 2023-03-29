from ply import *
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

literals = ',()[]{}:='

def t_comment(t):
        r'(/\*(.|\n)*?\*/)|(\#.*)'
        t.lexer.lineno += t.value.count('\n')



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



def p_operator_add(p):
    '''
    expr : expr operator_add expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_sub(p):
    '''
    expr : expr operator_sub expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_mul(p):
    '''
    expr : expr operator_mul expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_div(p):
    '''
    expr : expr operator_div expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_trudiv(p):
    '''
    expr : expr operator_trudiv expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_pow(p):
    '''
    expr : expr operator_pow expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_join(p):
    '''
    expr : expr operator_join expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_split(p):
    '''
    expr : expr operator_split expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_scan(p):
    '''
    expr : expr operator_scan expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_reduc(p):
    '''
    expr : expr operator_reduc expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitand(p):
    '''
    expr : expr operator_bitand expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitor(p):
    '''
    expr : expr operator_bitor expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitxor(p):
    '''
    expr : expr operator_bitxor expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitshiftleft(p):
    '''
    expr : expr operator_bitshiftleft expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitshiftright(p):
    '''
    expr : expr operator_bitshiftright expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_and(p):
    '''
    expr : expr operator_and expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_or(p):
    '''
    expr : expr operator_or expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_xor(p):
    '''
    expr : expr operator_xor expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_contains(p):
    '''
    expr : expr operator_contains expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_bitnot(p):
    '''
    expr : operator_bitnot expr
    '''
    p[0] = (p[1], p[2])


def p_operator_not(p):
    '''
    expr : operator_not expr
    '''
    p[0] = (p[1], p[2])


def p_operator_incr(p):
    '''
    expr : expr operator_incr
    '''
    p[0] = (p[2], p[1])


def p_operator_decr(p):
    '''
    expr : expr operator_decr
    '''
    p[0] = (p[2], p[1])


def p_operator_outer(p):
    '''
    expr : expr operator_outer expr expr
    '''
    p[0] = (p[2], p[1], p[3], p[4])


def p_operator_inner(p):
    '''
    expr : expr expr operator_inner expr expr
    '''
    p[0] = (p[3], p[1], p[2], p[4], p[5])


def p_operator_reverse(p):
    '''
    expr : operator_reverse expr
    '''
    p[0] = (p[1], p[2])


def p_operator_rotate(p):
    '''
    expr : expr operator_rotate expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_apply(p):
    '''
    expr : expr operator_apply expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_compose(p):
    '''
    expr : expr operator_compose expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_over(p):
    '''
    expr : expr operator_over expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_map(p):
    '''
    expr : expr operator_map
    '''
    p[0] = (p[2], p[1])


def p_operator_sorted_incr(p):
    '''
    expr : operator_sorted_incr expr
    '''
    p[0] = (p[1], p[2])


def p_operator_sorted_decr(p):
    '''
    expr : operator_sorted_decr expr
    '''
    p[0] = (p[1], p[2])


def p_operator_less_than(p):
    '''
    expr : expr operator_less_than expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_less_than_equals(p):
    '''
    expr : expr operator_less_than_equals expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_greater_than(p):
    '''
    expr : expr operator_greater_than expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_greater_than_equals(p):
    '''
    expr : expr operator_greater_than_equals expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_equals(p):
    '''
    expr : expr operator_equals expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_not_equals(p):
    '''
    expr : expr operator_not_equals expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_smallest(p):
    '''
    expr : expr operator_smallest expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_greatest(p):
    '''
    expr : expr operator_greatest expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_goodname(p):
    '''
    expr : expr operator_goodname expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_operator_s_combinator(p):
    '''
    expr : operator_s_combinator expr expr expr
    '''
    p[0] = (p[1], p[2], p[3], p[4])


def p_operator_goodname2(p):
    '''
    expr : operator_goodname2 expr
    '''
    p[0] = (p[1], p[2])



def p_expr(p):
    '''
    expr : const_val 
         | VAR
    '''
    p[0] = p[1]

def p_single_argument(p):
    '''
    arguments : expr
    '''
    p[0] = [p[1]]

def p_arguments(p):
    '''
    arguments : arguments ',' arguments
    '''
    p[0] = p[1]+p[3]
    

def p_const_val(p):
    '''
    const_val : NUM
              | FLOAT
              | STRING_3SQ
              | STRING_3DQ
              | STRING_SQ
              | STRING_DQ
    '''
    p[0] = p[1]

def p_return_val(p):
    '''
    return_val : type_type '(' arguments ')'
               | type_num '(' arguments ')'
               | type_any '(' arguments ')'
               | type_u64 '(' arguments ')'
               | type_u32 '(' arguments ')'
               | type_u16 '(' arguments ')'
               | type_u8 '(' arguments ')'
               | type_i64 '(' arguments ')'
               | type_i32 '(' arguments ')'
               | type_i16 '(' arguments ')'
               | type_i8 '(' arguments ')'
               | type_f32 '(' arguments ')'
               | type_f64 '(' arguments ')'
               | type_str '(' arguments ')'
               | type_list '(' arguments ')'
               | type_tuple '(' arguments ')'
               | type_array '(' arguments ')'
               | type_vector '(' arguments ')'
               | type_dict '(' arguments ')'
               | type_generator '(' arguments ')'
               | type_linked_list '(' arguments ')'
               | type_doubly_linked_list '(' arguments ')'
               | type_deque '(' arguments ')'
               | type_heap '(' arguments ')'
               | type_fibonacci_heap '(' arguments ')'
               | type_tree '(' arguments ')'
               | type_trie '(' arguments ')'
               | type_stack '(' arguments ')'
               | type_queue '(' arguments ')'
               | type_binary_search_tree '(' arguments ')'
               | type_bitset '(' arguments ')'
               | type_set '(' arguments ')'
               | type_map '(' arguments ')'
               | type_range '(' arguments ')'
    '''
    p[0] = ()

def p_error(p):
    print(f"Syntax error at line {p.lexer.lineno}")

parser = yacc.yacc()

