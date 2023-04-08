#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <algorithm>
#include <sstream>
#include <numeric>
#include <functional>
#include <type_traits>

namespace arrs {

namespace operators {

template<typename A, typename B>
inline auto operator_add(A a, B b){
    return a + b;
}

template<typename A, typename B>
inline auto operator_sub(A a, B b){
    return a - b;
}

template<typename A, typename B>
inline auto operator_mul(A a, B b){
    return a * b;
}

template<typename A, typename B>
inline auto operator_div(A a, B b){
    return a / b;
}

template<typename A, typename B>
inline auto operator_trudiv(A a, B b){
    return (double)a / (double)b;
}

template<typename A, typename B>
inline auto operator_pow(A a, B b){
    return std::pow(a, b);
}

template<typename A>
inline auto operator_join(std::string a, A b){
    return std::accumulate(std::next(b.begin()), b.end(), b[0],
        [a](const std::string& s1, const std::string& s2) -> std::string {
            return s1 + a + s2;
        });
}

// operator_split("+", "1+2+3") => ["1", "2", "3"]
auto operator_split(std::string str, std::string delimiter){
    std::vector<std::string> result;

    std::string::size_type start = 0;
    auto end = str.find(delimiter);

    while (end != std::string::npos) {
        result.push_back(str.substr(start, end - start));
        start = end + delimiter.length();
        end = str.find(delimiter, start);
    }

    result.push_back(str.substr(start));

    return result;
}

template<typename A, typename B>
auto operator_scan(A op, B b){
    std::partial_sum(b.cbegin(), b.cend(), b.begin(), op);
    return b;
}

template<typename A, typename B>
auto operator_reduc(A op, B b){
    auto first = b.begin();
    auto last = b.end();
    if (first == last) {
        typename B::value_type default_ret = {};
        return default_ret;
    }
    auto init = *first;
    first++;
    for (; first != last; ++first)
        init = op(std::move(init), *first); 
    return init;
}

template<typename A, typename B>
inline auto operator_bitand(A a, B b){
    return a & b;
}

template<typename A, typename B>
inline auto operator_bitor(A a, B b){
    return a | b;
}

template<typename A, typename B>
inline auto operator_bitxor(A a, B b){
    return a ^ b;
}

template<typename A, typename B>
inline auto operator_bitshiftleft(A a, B b){
    return a << b;
}

template<typename A, typename B>
inline auto operator_bitshiftright(A a, B b){
    return a >> b;
}

template<typename A, typename B>
inline auto operator_and(A a, B b){
    return a && b;
}

template<typename A, typename B>
inline auto operator_or(A a, B b){
    return a || b;
}

template<typename A, typename B>
inline auto operator_xor(A a, B b){
    return (a || b) && !(a && b);
}


// il faudra implémenter la fonctions contains dans chaque type
template<typename A, typename B>
inline auto operator_contains(A a, B b){
    return b.contains(a);
}

template<typename A>
inline auto operator_bitnot(A a){
    return ~a;
}

template<typename A>
inline auto operator_not(A a){
    return !a;
}

template<typename A>
inline auto operator_incr(A& a){
    return a++;
}

template<typename A>
inline auto operator_decr(A& a){
    return a--;
}

template<typename A, typename B, typename F>
auto operator_outer(const A& a, F f, const B& b) {
    typedef typename std::result_of<F(typename A::value_type, typename B::value_type)>::type T;
    std::vector<std::vector<T>> result(a.size(), std::vector<T>(b.size()));
    for (size_t i = 0; i < a.size(); ++i) {
        for (size_t j = 0; j < b.size(); ++j) {
            result[i][j] = f(a[i], b[j]);
        }
    }
    return result;
}

template<typename A, typename B, typename F1, typename F2>
auto operator_inner(const A& a, F1 f1, F2 f2, const B& b) {
    typedef typename std::result_of<F2(typename A::value_type, typename B::value_type)>::type T1;
    typedef typename std::result_of<F1(T1, T1)>::type T2;
    T2 init = {};
    return std::inner_product(a.begin(), a.end(), b.begin(), init, f1, f2);
}

template<typename A>
auto operator_reverse(A& a){
    std::reverse(a.begin(), a.end());
    return a;
}

template<typename A, typename B>
auto operator_rotate(A a, B b){
    std::rotate(b.begin(), b.begin() + a, b.end());
    return b;
}


// il faut solve apply a moment de la compilation
// template<typename A, typename B>
// auto operator_apply(A a, B b){
//     auto 
//     return b()
// }

template<typename A, typename B>
auto operator_compose(A a, B b){
    return a(b);
}

template<typename A, typename B>
auto operator_over(A a, const B& b){
    std::transform(b.cbegin(), b.cend(), b.begin(), a);
    return b;
}

template<typename A>
auto operator_map(const A& a){
    return arrs::types::type_map(a);
}

template<typename A>
auto operator_sorted_incr(const A& a){
    std::sort(a.begin(), a.end());
    return a;
}

template<typename A>
auto operator_sorted_decr(A a){
    std::sort(a.begin(), a.end());
    std::reverse(a.cbegin(), a.cend(), a.begin());
    return a;
}

template<typename A, typename B>
inline auto operator_less_than(A a, B b){
    return a < b;
}

template<typename A, typename B>
inline auto operator_less_than_equals(A a, B b){
    return a <= b;
}

template<typename A, typename B>
inline auto operator_greater_than(A a, B b){
    return a > b;
}

template<typename A, typename B>
inline auto operator_greater_than_equals(A a, B b){
    return a >= b;
}

template<typename A, typename B>
inline auto operator_equals(A a, B b){
    return a == b;
}

template<typename A, typename B>
inline auto operator_not_equals(A a, B b){
    return a != b;
}

template<typename A, typename B>
inline auto operator_smallest(A a, B b){
    return std::min(a, b);
}

template<typename A, typename B>
inline auto operator_greatest(A a, B b){
    return std::max(a, b);
}

}
namespace types {

class type_type{
public :
    type_type(){}
    ~type_type(){}
};

class type_num{
public :
    type_num(){}
    ~type_num(){}
};

class type_bool{
public :
    type_bool(){}
    ~type_bool(){}
};

class type_any{
public :
    type_any(){}
    ~type_any(){}
};

class type_u64{
public :
    type_u64(){}
    ~type_u64(){}
};

class type_u32{
public :
    type_u32(){}
    ~type_u32(){}
};

class type_u16{
public :
    type_u16(){}
    ~type_u16(){}
};

class type_u8{
public :
    type_u8(){}
    ~type_u8(){}
};

class type_i64{
public :
    type_i64(){}
    ~type_i64(){}
};

class type_i32{
public :
    type_i32(){}
    ~type_i32(){}
};

class type_i16{
public :
    type_i16(){}
    ~type_i16(){}
};

class type_i8{
public :
    type_i8(){}
    ~type_i8(){}
};

class type_f32{
public :
    type_f32(){}
    ~type_f32(){}
};

class type_f64{
public :
    type_f64(){}
    ~type_f64(){}
};

class type_str{
public :
    type_str(){}
    ~type_str(){}
};

class type_list{
public :
    type_list(){}
    ~type_list(){}
};

class type_tuple{
public :
    type_tuple(){}
    ~type_tuple(){}
};

class type_array{
public :
    type_array(){}
    ~type_array(){}
};

class type_vector{
public :
    type_vector(){}
    ~type_vector(){}
};

class type_dict{
public :
    type_dict(){}
    ~type_dict(){}
};

class type_generator{
public :
    type_generator(){}
    ~type_generator(){}
};

class type_linked_list{
public :
    type_linked_list(){}
    ~type_linked_list(){}
};

class type_doubly_linked_list{
public :
    type_doubly_linked_list(){}
    ~type_doubly_linked_list(){}
};

class type_deque{
public :
    type_deque(){}
    ~type_deque(){}
};

class type_heap{
public :
    type_heap(){}
    ~type_heap(){}
};

class type_fibonacci_heap{
public :
    type_fibonacci_heap(){}
    ~type_fibonacci_heap(){}
};

class type_tree{
public :
    type_tree(){}
    ~type_tree(){}
};

class type_trie{
public :
    type_trie(){}
    ~type_trie(){}
};

class type_stack{
public :
    type_stack(){}
    ~type_stack(){}
};

class type_queue{
public :
    type_queue(){}
    ~type_queue(){}
};

class type_binary_search_tree{
public :
    type_binary_search_tree(){}
    ~type_binary_search_tree(){}
};

class type_bitset{
public :
    type_bitset(){}
    ~type_bitset(){}
};

class type_set{
public :
    type_set(){}
    ~type_set(){}
};

class type_map{
public :
    type_map(){}
    ~type_map(){}
};

class type_range{
public :
    type_range(){}
    ~type_range(){}
};

}
namespace funcs {

}
}