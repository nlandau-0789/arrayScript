# Array oriented language : ArrayScript

extension de fichiers .arrs
compilé en c++

## syntaxe
- indenté
- déclaratif
- types statiques
- type à spécifier dans les définitions de fonctions
- abus du type auto, qui est non spécifié (en gros si on ne vois pas de déclaration de type explicite, il faut nécessairement que la variable soit initialisée par un constructeur)
- garbage collector (peut être si j'y arrive)
- /*  */ ou # pour les commentaires
- les opérators doivent avoir un nom, un symbole, une priorité et un pattern
- pas de rstrings, (fstring), bstring, ustring


## built-in keywords
- func : définition de fonction
- lambda : fonction anonyme
- for 
- while
- if
- elif
- struct
- (dans le futur) :
    - import/from (comme en python) 

## built-in datatypes
- "type", # base mataclass (comme en python)
- "num", # pas de limite
- "u64",
- "u32",
- "u16",
- "u8",
- "i64",
- "i32",
- "i16",
- "i8",
- "f32",
- "f64",
- "str", # immutable
- "list", # dynamic length, dynamic type
- "tuple", # static length, dynamic type
- "array", # static length, static type
- "vector", # dynamic length, static type
- "dict", # hashtable
- "any", # pour les déclarations de fonctions
- "generator", 
- "linked_list",
- "doubly_linked_list",
- "deque",
- "heap", # priority queue
- "fibonacci_heap", # priority queue
- "tree",
- "trie",
- "stack", # FILO
- "queue", # FIFO
- "binary_search_tree"
- "bitset"
- "set"
- "map" # active le ranked polymorphism
- "range"

## built-in functions
- log
- sqrt
- nth_root
- find_root (trouve les racine d'une fonction sur un intervalle par balayage puis dichotomie)
- find (renvoie l'index d'un élément dans un itérable et -1 s'il n'y est pas)
- find_if (renvoie l'index d'un élément dans un itérable correspondant à un prédicate et -1 s'il n'y en a pas)
- eval
- input
- output
- error

filters

opérators :
- "+","add",1,"{a} + {b}",
- "-","sub",1,"{a} - {b}",
- "*","mul",2,"{a} * {b}",
- "/","div",2,"{a} / {b}",
- "//","trudiv",2,"{a} // {b}",
- "**","pow",3,"{a} ** {b}",
- "-+-","join",1,"{a} -+- {b}",
- "-|-","split",1,"{a} -|- {b}",
- "->","scan",4,"{a} -> {b}",
- "/>","reduc",4,"{a} /> {b}",
- "&&","bitand",1,"{a} && {b}",
- "||","bitor",1,"{a} || {b}",
- "^","bitxor",1,"{a} ^ {b}",
- "<<","bitshiftleft",1,"{a} << {b}",
- ">>","bitshiftright",1,"{a} >> {b}",
- "and","and",0,"{a} and {b}",
- "or","or",0,"{a} or {b}",
- "xor","xor",0,"{a} xor {b}",
- "~","bitnot",5,"~ {a}",
- "not","not",0,"not {a}",
- "++","incr",5,"{a} ++",
- "--","decr",5,"{a} --",
- "+.","outer",1,"{a} +. {b} {c}",
- "-.","inner",1,"{a} {b} -. {c} {d}",
- "o|","reverse",5,"o| {a}",
- "o-","rotate",4,"{a} o- {b}",
- ".","apply",4,"{a} . {b}",
- "::","compose",7,"{a} :: {b}",
- "()","call",6,"{a} ( {*} )", # special symbol "*" (cf regex)
- "[]","item",6,"{a} [ {+} ]", # special symbol "+" (cf regex)
- "[:]","slice",6,"{a} [ {b} : {c} ]",
- "[::]","slice_step",6,"{a} [ {b} : {c} : {d}]",
- "[]","map",6,"{a} []" # renvoie un objet de type "map"
- ">_>","sorted_incr",5,">_> {a}"
- "<_<","sorted_decr",5,"<_< {a}"
- "in","contains",0,"{a} in {b}"
<!--19. | : dans une fonction : permet d'effectuer la fonction avec le membre de gauche, puis sur le resultat avec le membre de droite: notament g[1][2] <=> []([](g,1),2) <=> g[1|2]-->



