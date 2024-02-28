from iteratif import binaire #voir à gauche l'autre fichier.
from recursif import binaire_r, binaire_rt, base3, en_base, en_base_c # solutions exercice 2
from typing import TypeVar, Callable

T = TypeVar('T', int, float)

 

def somme_parametree(n:int, f:Callable[[int],T])->T:
  somme:T = 0
  k:int = 0
  while k <= n:
    somme = somme + f(k)
    k = k + 1
  return somme

somme_jusqua_2:Callable[[int],int] = lambda n : somme_parametree(n, lambda x:x)
somme_carres_2:Callable[[int],int] = lambda n : somme_parametree(n, lambda x:x*x)
somme_pi_2:Callable[[int],float] = lambda n : somme_parametree(n, lambda x: (-1)**x * 4/ (2*x +1))

print("somme_jusqua(1000)=", somme_jusqua_2(1000))
print("somme_carres(1000)=", somme_carres_2(100))
print("somme_pi(1000)=", somme_pi_2(1000))