import math
def je_prastevilo(n):
  for i in range(2, int(math.sqrt(n))):
    if (n % i) == 0:
      return False
  return True

def najvecji_prastevilski_faktor(n):
    najvecji = 0
    for i in range(2, int(math.sqrt(n))):
        if je_prastevilo(i) == True and n % i == 0:
            najvecji = i
    return najvecji
print(najvecji_prastevilski_faktor(600851475143))
print(je_prastevilo(10))