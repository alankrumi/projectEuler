
import datetime


# We simply use Python's built-in date library to compute the answer by brute force.
def nedelje(a, b):
	vsota = sum(1 for y in range(a, b) for m in range(1, 13) if datetime.date(y, m, 1).weekday() == 6)
	return vsota
print(nedelje(1901, 2001))