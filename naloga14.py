def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return 1 + dolzina_zaporedja(naslednji_clen(n))

def kateri(n):
    maks = 0
    j = 0
    for i in range(1, n):
        if maks < dolzina_zaporedja(i):
            j = i
        maks = max(maks,dolzina_zaporedja(i))
    return j
print(kateri(1000000))

