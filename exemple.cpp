/*
Bob poss�de un mur divis� en N sections. Il lui arrive de repeidre Ki sections adjacentes, a savoir les sections Ii � Ji. On demandera, apr�s R repeintes, de donner le nombre de fois que chaque section � �t� repeinte.

Entr�e:
N un entier, le nombre de sections
R un entier, le nombre de repeintes
sur les R lignes suivantes :
Ii et Ji deux entiers s�par�s par un espace : les index de d�but et de fin de l'intervalle repeinte (0-indexed)
*/

struct bad_struct {
    nums a,b
    list c
}

operator{"op","goodname",5}("{a} op {b}"):
    tada

operator { "S", "s_combinator" , 0}("S {f} {g} {x}"):
    lambda x: a2(x, b2(x))

operator { "op2", "goodname2" , 9.7}("op2 {a}"):
    tada2

func dummy(num )

N = nums::input()
R = nums::input()
sections = static_array(N, nums) # N:nombre d'items, nums: type
for i in range(R):
    I, J = nums::split::input()
    sections[I]++
    sections[J]--
sections = + -> sections
(ghdujioezhduio
    djeiozdjio)

