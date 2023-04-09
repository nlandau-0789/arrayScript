#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <algorithm>
#include <sstream>
#include <numeric>
#include <functional>
#include <type_traits>
#include <variant>
#include <cmath>
#include <arrs.hpp>

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

typedef bool type_bool;

// type_any must be defined using a std::variant of all the types, after precompilations

typedef unsigned long long type_u64;
typedef unsigned long type_u32;
typedef unsigned short type_u16;
typedef unsigned char type_u8;

typedef long long type_i64;
typedef long type_i32;
typedef short type_i16;
typedef char type_i8;

typedef float type_f32;
typedef double type_f64;

typedef std::string type_str;

typedef std::variant<type_u64, type_u32, type_u16, type_u8, type_i64, type_i32, type_i16, type_i8, type_bool, type_str> primitive_type;

// class type_list{
// private :

// public :
//     type_list(){}
//     ~type_list(){}
// };

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
#ifndef ALT2
template<typename T, std::size_t i = 0, std::size_t j = std::tuple_size<T>::value>
struct tuple_compare {
    static bool
    one_equal(T const& lhs, T const& rhs) {
        if constexpr(i == j) return false;
        else {
            return (std::get<i>(lhs) == std::get<i>(rhs) ||
            tuple_compare<T, i + 1, j>::one_equal(lhs, rhs));
        }
    }
};
#endif

template<typename... Conts>
struct container_ref_tuple {
    static auto constexpr get_begin{[](auto&&... args){return std::make_tuple(begin(args)...);}};

    typename std::invoke_result<decltype(&std::forward_as_tuple<Conts...>), Conts&&...>::type m_refs;

    struct iterator {
        typename std::invoke_result<decltype(get_begin), Conts&&...>::type m_iterators;

        decltype(auto)
        operator++() {
            apply([](auto&... args) {((++args), ...);}, m_iterators);
            return (*this);
        }

        #ifndef ALT2
        //Alternative 1(safe)
        //will stop when it reaches the end of the shortest container
        auto
        operator!=(iterator const& rhs) const {
            return !tuple_compare<decltype(m_iterators)>::one_equal(m_iterators, rhs.m_iterators);
        }
        #else
        //Alternative 2 (probably faster, but unsafe):
        //use only, if first container is shortest
        auto
        operator!=(iterator const& rhs) const {
            return std::get<0>(m_iterators) != std::get<0>(rhs.m_iterators);
        }
        #endif

        auto
        operator*() const {
            return apply([](auto&... args){return std::forward_as_tuple(*args...);}, m_iterators);
        }
    };

    auto
    begin() const {
        return iterator{apply(get_begin, m_refs)};
    }

    #ifndef ALT2
    //Alternative 1(safe)
    //will stop when it reaches the end of the shortest container
    static auto constexpr get_end{[](auto&&... args){return std::make_tuple(end(args)...);}};
    auto
    end() const {
        return iterator{apply(get_end, m_refs)};
    }
    #else
    //Alternative 2 (probably faster, but unsafe):
    //use only, if first container is shortest
    auto
    end() const {
        iterator ret;
        std::get<0>(ret.m_iterators) = std::end(std::get<0>(m_refs));
        return ret;
    }
    #endif
};

template<typename... Conts>
auto
zip(Conts&&... conts) {
    return container_ref_tuple<Conts...>{std::forward_as_tuple(conts...)};
}
}
}