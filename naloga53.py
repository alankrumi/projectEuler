def fakulteta(i):
    return 1 if i == 0 else i * fakulteta(i - 1)
def binomski(n, i):
    return fakulteta(n) // (fakulteta(n - i) * fakulteta(i))
def koliko(n):
    koliko = 0
    for i in range(n + 1):
        if binomski(n , i) > 1000000:
            koliko += 1
    return koliko
def vsi(n):
    vsota = 0
    for i in range(1, n + 1):
        vsota += koliko(i)
    return vsota

print(vsi(100))