
def izracun(n):
	ans = sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


print(izracun(1000))