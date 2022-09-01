def potence(n):
    vsota = 0
    for i in range(2, 10 ** (n + 1)):
        j = str(i)
        vsotica = 0
        for številka in j:
            vsotica += int(številka) ** n
        if vsotica == i:
            vsota += i
    return vsota
print(potence(5))


