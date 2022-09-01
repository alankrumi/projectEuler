def vsota(n):
    a = max(sum(int(i) for i in str(x**y))
     for x in range(n) for y in range(n))
    return a

print(vsota(100))