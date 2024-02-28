from iteratif import binaire #voir à gauche l'autre fichier.
from recursif import binaire_r, binaire_rt, base3, en_base, en_base_c # solutions exercice 2
from typing import TypeVar, Callable

T = TypeVar('T', int, float)
 
#=========================
# exercice 2 (voir code dans fichier recursif.py)
print ("35657 en binaire:", binaire(10))

print(binaire_r(5))

binaire_rt(10)
print ("35657 en base 3:", base3(35657))
print(en_base(3,6))


binaire_c = en_base_c(3)
print(binaire_c(6))
#print ("35657 en base 3:", base3(6))
#print (en_base_c(3)(35657))
