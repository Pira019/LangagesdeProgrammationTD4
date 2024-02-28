from iteratif import binaire #voir à gauche l'autre fichier.
from recursif import binaire_r, binaire_rt, base3, en_base, en_base_c # solutions exercice 2
from typing import TypeVar, Callable

T = TypeVar('T', int, float)

def somme_jusqua(n:int)->int:
  somme = 0
  k = 0
  while k <= n:
    somme = somme + k
    k = k + 1
  return somme

def somme_carres(n:int)->int:
  somme = 0
  k = 0
  while k <= n:
    somme = somme + k*k
    k = k + 1
  return somme

def somme_pi(n:int)->float:
  somme = 0
  k = 0
  while k <= n:
    somme = somme + (-1)**k * 4 / (2*k +1)
    k = k + 1
  return somme

def somme_parametree(n:int, f:Callable[[int],T])->T:
  somme:T = 0
  k:int = 0
  while k <= n:
    somme = somme + f(k)
    k = k + 1
  return somme

somme_jusqua_2:Callable[[int],int] = lambda n : somme_parametree(n, lambda x:x)
 