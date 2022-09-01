def fakulteta(i):
    return 1 if i == 0 else i * fakulteta(i - 1)
def poti(n):
    return fakulteta(2 * n) // (fakulteta(n) ** 2)
print(poti(20))
    