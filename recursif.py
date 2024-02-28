from typing import Callable

def binaire_r(x:int)->str:
  if (x<2):
    return str(x)
  else :
    return binaire_r(x//2)+str(x%2)

#récursif terminal 
def b_helper(x:int,s:str)->str:
  if (x<2):
    return str(x%2) + s
  else :
    return b_helper(x//2, str(x%2)+s)
  
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

