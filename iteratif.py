def binaire(n):
  if (n==0): #cas particulier: zéro
    return "0"
  ecriture = ""
  while(n>0):
    ecriture = str(n%2)+ecriture
    n=n//2 #division entière
  return ecriture
