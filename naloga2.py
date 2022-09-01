def vsota(n):
	ans = 0
	a = 1  
	b = 2  
	while a <= n:
		if a % 2 == 0:
			ans += a
		a, b = b, a + b
	return str(ans)

print(vsota(4000000))
