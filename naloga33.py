

import math
def krajšanje(n):
    zgornji = 1
    spodnji = 1
    for a in range(10, n):
        for b in range(10, a):
            zgornji0 = b % 10
            zgornji1 = b // 10
            spodnji0 = a % 10
            spodnji1 = a // 10
            if (spodnji0 == zgornji1 and spodnji1 * b == zgornji0 * a) or (spodnji1 == zgornji0 and spodnji0 * b == zgornji1 * a):
                spodnji *= a
                zgornji *= b
                c = math.gcd(spodnji, zgornji)
    return spodnji // c
print(krajšanje(100))