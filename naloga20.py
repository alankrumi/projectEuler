def fakulteta(i):
    return 1 if i == 0 else i * fakulteta(i - 1)
def vsota(n):
    a = fakulteta(n)
    b = str(a)
    vsota = 0
    for številka in b:
        vsota += int(številka)
    return vsota
print(vsota(100))