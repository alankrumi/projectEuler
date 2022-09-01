from tokenize import Pointfloat


def pitagora(n):
    for a in range(1, n + 1):
        for b in range(a + 1 , n + 1):
            c = n - b - a
            if c ** 2 == a ** 2 + b ** 2:
                return a * b * c
print(pitagora(1000))