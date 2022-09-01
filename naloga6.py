def razlika(n):
    i = 1
    vsota1 = 0
    vsota2 = 0
    while i < n + 1:
        vsota1 += i
        vsota2+= i ** 2
        i += 1
    return vsota1 ** 2 - vsota2
print(razlika(100))
