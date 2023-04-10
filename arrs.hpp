
namespace arrs {

namespace operators {

template<typename A, typename B>
auto operator_add(A a, B b);

template<typename A, typename B>
auto operator_sub(A a, B b);

template<typename A, typename B>
auto operator_mul(A a, B b);

template<typename A, typename B>
auto operator_div(A a, B b);

template<typename A, typename B>
auto operator_trudiv(A a, B b);

template<typename A, typename B>
auto operator_pow(A a, B b);

template<typename A, typename B>
auto operator_join(A a, B b);

template<typename A, typename B>
auto operator_split(A a, B b);

template<typename A, typename B>
auto operator_scan(A a, B b);

template<typename A, typename B>
auto operator_reduc(A a, B b);

template<typename A, typename B>
auto operator_bitand(A a, B b);

template<typename A, typename B>
auto operator_bitor(A a, B b);

template<typename A, typename B>
auto operator_bitxor(A a, B b);

template<typename A, typename B>
auto operator_bitshiftleft(A a, B b);

template<typename A, typename B>
auto operator_bitshiftright(A a, B b);

template<typename A, typename B>
auto operator_and(A a, B b);

template<typename A, typename B>
auto operator_or(A a, B b);

template<typename A, typename B>
auto operator_xor(A a, B b);

template<typename A, typename B>
auto operator_contains(A a, B b);

template<typename A>
auto operator_bitnot(A a);

template<typename A>
auto operator_not(A a);

template<typename A>
auto operator_incr(A a);

template<typename A>
auto operator_decr(A a);

template<typename A, typename B, typename C>
auto operator_outer(A a, B b, C c);

template<typename A, typename B, typename C, typename D>
auto operator_inner(A a, B b, C c, D d);

template<typename A>
auto operator_reverse(A a);

template<typename A, typename B>
auto operator_rotate(A a, B b);

template<typename A, typename B>
auto operator_apply(A a, B b);

template<typename A, typename B>
auto operator_compose(A a, B b);

template<typename A, typename B>
auto operator_over(A a, B b);

template<typename A>
auto operator_map(A a);

template<typename A>
auto operator_sorted_incr(A a);

template<typename A>
auto operator_sorted_decr(A a);

template<typename A, typename B>
auto operator_less_than(A a, B b);

template<typename A, typename B>
auto operator_less_than_equals(A a, B b);

template<typename A, typename B>
auto operator_greater_than(A a, B b);

template<typename A, typename B>
auto operator_greater_than_equals(A a, B b);

template<typename A, typename B>
auto operator_equals(A a, B b);

template<typename A, typename B>
auto operator_not_equals(A a, B b);

template<typename A, typename B>
auto operator_smallest(A a, B b);

template<typename A, typename B>
auto operator_greatest(A a, B b);

}
namespace types {

class type_type;

class type_num;

class type_bool;

class type_any;

class type_u64;

class type_u32;

class type_u16;

class type_u8;

class type_i64;

class type_i32;

class type_i16;

class type_i8;

class type_f32;

class type_f64;

class type_str;

class type_list;

class type_tuple;

class type_array;

class type_vector;

class type_dict;

class type_generator;

class type_linked_list;

class type_doubly_linked_list;

class type_deque;

class type_heap;

class type_fibonacci_heap;

class type_tree;

class type_trie;

class type_stack;

class type_queue;

class type_binary_search_tree;

class type_bitset;

class type_set;

class type_map;

class type_range;

}
namespace funcs {

template<typename T>
arrs::types::type_type make_type_type(T){};

template<typename T>
arrs::types::type_num make_type_num(T){};

template<typename T>
arrs::types::type_bool make_type_bool(T){};

template<typename T>
arrs::types::type_any make_type_any(T){};

template<typename T>
arrs::types::type_u64 make_type_u64(T){};

template<typename T>
arrs::types::type_u32 make_type_u32(T){};

template<typename T>
arrs::types::type_u16 make_type_u16(T){};

template<typename T>
arrs::types::type_u8 make_type_u8(T){};

template<typename T>
arrs::types::type_i64 make_type_i64(T){};

template<typename T>
arrs::types::type_i32 make_type_i32(T){};

template<typename T>
arrs::types::type_i16 make_type_i16(T){};

template<typename T>
arrs::types::type_i8 make_type_i8(T){};

template<typename T>
arrs::types::type_f32 make_type_f32(T){};

template<typename T>
arrs::types::type_f64 make_type_f64(T){};

template<typename T>
arrs::types::type_str make_type_str(T){};

template<typename T>
arrs::types::type_list make_type_list(T){};

template<typename T>
arrs::types::type_tuple make_type_tuple(T){};

template<typename T>
arrs::types::type_array make_type_array(T){};

template<typename T>
arrs::types::type_vector make_type_vector(T){};

template<typename T>
arrs::types::type_dict make_type_dict(T){};

template<typename T>
arrs::types::type_generator make_type_generator(T){};

template<typename T>
arrs::types::type_linked_list make_type_linked_list(T){};

template<typename T>
arrs::types::type_doubly_linked_list make_type_doubly_linked_list(T){};

template<typename T>
arrs::types::type_deque make_type_deque(T){};

template<typename T>
arrs::types::type_heap make_type_heap(T){};

template<typename T>
arrs::types::type_fibonacci_heap make_type_fibonacci_heap(T){};

template<typename T>
arrs::types::type_tree make_type_tree(T){};

template<typename T>
arrs::types::type_trie make_type_trie(T){};

template<typename T>
arrs::types::type_stack make_type_stack(T){};

template<typename T>
arrs::types::type_queue make_type_queue(T){};

template<typename T>
arrs::types::type_binary_search_tree make_type_binary_search_tree(T){};

template<typename T>
arrs::types::type_bitset make_type_bitset(T){};

template<typename T>
arrs::types::type_set make_type_set(T){};

template<typename T>
arrs::types::type_map make_type_map(T){};

template<typename T>
arrs::types::type_range make_type_range(T){};

}
}