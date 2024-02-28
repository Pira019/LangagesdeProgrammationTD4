from typing import Callable



#binaire_r(x//2) renvoie une chaîne de caractères représentant les bits binaires les plus significatifs de x, 
#str(x % 2) renvoie une chaîne de caractères représentant le bit binaire le moins significatif de x
def binaire_r(x:int)->str:
  if (x<2):
    return str(x) # cas de base
  else : 
    return binaire_r(x//2)+str(x%2)

#récursif terminal
  # Fonction auxiliaire pour gérer l'accumulation de l'accumulateur 
def b_helper(x:int,s:str)->str:
  print(s)
  if (x<2):
    return str(x%2) + s  # Ajout du bit binaire final à l'accumulateur
  else : 
    return b_helper(x//2, str(x%2)+s) # Appel récursif avec l'accumulateur mis à jour
  
  
 # Fonction principale qui initialise l'accumulateur et appelle la fonction auxiliaire
binaire_rt:Callable[[int],str] = lambda x: b_helper(x, "") 

#base 3 récursif terminal 
def b3_helper(x:int, s:str)->str:
  if (x<3):
    return str(x%3) + s
  else :
    return b3_helper(x//3, str(x%3)+s)
  
base3:Callable[[int],str] = lambda x: b3_helper(x, "")

# conversion en base quelconque
def eb_helper(b:int, x:int, s:str)->str:
  if (x<b):
    return str(x%b) + s
  else :
    return eb_helper(b, x//b, str(x%b)+s)
  
en_base = lambda b,n: eb_helper(b, n, "")

#version currifiée
def en_base_c(b:int)->Callable[[int],str]:
  return lambda n: eb_helper(b, n, "") 
  #return lambda n: en_base(x, n)  ceci est aussi possible

