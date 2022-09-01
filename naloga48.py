def zadnjih_n_stevk(n):
    a = 10 ** n
    return sum(pow(i , i, a) for i in range(1, 1001)) % a
print(zadnjih_n_stevk(10))