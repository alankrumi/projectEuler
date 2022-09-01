
import math

def deljiv(n):
    a = 1
    for i in range(1, n + 1):
        a *= i // math.gcd(a, i)
    return a

print(deljiv(20))