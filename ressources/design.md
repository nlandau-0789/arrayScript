Array oriented language : ArrayScript

indenté

func pour créer une fonction

lambdas

hashtables ()

matrix math

vector maths

staticly typed, mais typing auto

garbage collector

pointers

structs

.arrs file extention

usual /*  */ or // for comments

ints are also bitarrays by default donc on peut regarder le i eme bit d'un int comme on le ferait avec une string ou un array

string

plusieurs types d'arrays :
    static type => vector
    static size => array
    both => tuple
    none => list

other datastructures built-in:
    linked-list
    doubly linked-list
    deque
    heap (priority queue)
    stack (FILO)
    queue (FIFO)

possibilité de choisir la mémoire occupée par un objet (comme choisir le nombre d'octets pour un int ou un array dynamique (qui souleverait une erreur dans le cas échéant)), mais si non spécifié : non limité

la plupart des opérations (comme les racines carrées etc) sont built-in sans avoir besoin de bibliothèque

on compile tout en c++

# Réductions => on passe un objet (array ou pas) et une fonction

partial_sum built-in/partial_op avec l'opérateur "->"



les opérations sont des fonctions

aucun objet (meme built-in) n'est unmutable donc on peut redéfinir n'importe quelle fonction ou objet

# = est aussi une fonctions

les opérateurs étant des fonctions, on peut les écrire a + b OU +(a,b), donc =(a,b) va assigner la valeur de b à a

si on a une variable arr qui est n'import quel type d'array, écrire arr[] fait référence à "pour chaque élément de arr", et les opérations sont effectuées en partant de l'index 0

composition de fonctions : opérateur "::"

zipper : en utilisant les paranthèses, on peut créer un "zip" qui est comme une liste sauf qu'on peut seulement effectuer des fonctions sur chaque élément indémendament, jamais sur 1 seul, cependant, il reste itérable

filters

opérators :
1. +
2. -
3. * (entre 2 arrays : représente une convolution)
4. /
5. //
6. ** : power
7. -+- : join (str -+- list)
8. -|- : split (str -|- str)
9. -> : running operation (op -> list)
10. /> : réductions (op /> list)
11. ^ : bitwise xor
12. && : bitwise and
13. || : bitwise or
14. << : bitwise left shift
15. >> : bitwise right shift
16. xor : logic gate
17. and : logic gate
18. or : logic gate
19. | : dans une fonction : permet d'effectuer la fonction avec le mebre de gauche, puis sur le resultat avec le membre de droite: notament g[1][2] <=> []([](g,1),2) <=> g[1|2]

monopérators :
1. ! : bitwise not
2. not : logic gate
3. ++ : incrément
4. -- : décrément

les annotations de types envoient un warning à la compilation

les opérators doivent avoir un nom, un symbole et une priorité


pas de rstrings
pas de bstrings
pas de ustrings


need :
reductions accumumlations and outer op