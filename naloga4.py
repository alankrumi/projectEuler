def najvecji_palindrom(n):
    najvecji = 1
    for i in range(100, n):
        for j in range(i, n):
            a = str(i * j)
            if a == a[::-1]:
                najvecji = max(najvecji, i * j)
    return najvecji

print(najvecji_palindrom(1000))
