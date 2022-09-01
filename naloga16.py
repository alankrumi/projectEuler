def vsota(n):
    a = 2 ** n
    b = str(a)
    vsota = 0
    for številka in b:
        vsota += int(številka)
    return vsota
print(vsota(1000))
