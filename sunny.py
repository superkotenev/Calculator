def fact(a):
	ans = 1
	for i in range(a):
		ans *= a
		a -= 1
	return ans

print(fact(int(input())))