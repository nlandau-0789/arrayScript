#include <arrs.cpp>

using namespace arrs;
using namespace operators;
using namespace types;
using namespace funcs;

struct bad_struct {
	num a;
	num b;
	list c;
};

struct bad_struct2 {
	num a;
	num b;
	list c;
};


template<typename A, typename B>
auto operator_goodname(A a, B b){
	return NULL;
}


template<typename A, typename B, typename C>
auto operator_s_combinator(A f, B g, C x){
	return [](auto x){return f(x, g(x));};
}


template<typename A, typename B, typename C>
auto operator_s_combinator_2(A f, B g, C x){
	return [](auto x){return f(x, g(x));};
}


template<typename A>
auto operator_goodname2(A a){
	return NULL;
}

auto dummy(num a){
	return NULL;
}

auto dummy2(num a, num b, list c){
	auto variable = operator_add(operator_map(simple_slice(nom, 5, 9)), operator_pow(90, 2));
	return NULL;
}

auto a = operator_add(1, operator_mul(3, operator_add(5, operator_compose(input, input()))));

auto main(){
	auto N = operator_compose(make_num, input());
	auto R = operator_compose(make_num, input());
	auto sections = array(N, make_num);
	for (auto&& i : range(R)){
		auto tmp = operator_over(make_num, operator_compose(split, input())); auto I = temp[0]; auto J = temp[1];

		operator_decr(item(sections, I));

		operator_incr(item(sections, J));
	};
	auto sections = operator_scan(operator_add, sections);
	output(operator_join(" ", operator_over(make_str, sections)));
	output(operator_goodname(a, operator_goodname2(b)));
	operator_s_combinator_2(operator_add, operator_sub, aze);
}

output(123);

output(input);

auto tmp = operator_over(make_num, operator_compose(split, input())); auto I = temp[0]; auto J = temp[1];

