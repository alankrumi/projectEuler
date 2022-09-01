def število_trikotnikov(n):
    število = 0
    for a in range(1 , n + 1):
        for b in range(a, (n - a) // 2 + 1):
            c = n - a - b
            if c ** 2 == a ** 2 + b ** 2:
                število += 1
    return število
def največ_do(n):
    return max(range(1, n + 1), key=število_trikotnikov)
print(največ_do(1000))

