def zadnje_stevke(n):
    a = 10 ** n
    b = 28433 * (2 ** 7830457) + 1
    return (b % a)
print(zadnje_stevke(10))
