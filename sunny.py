def fact(a):
	ans = 1
	for i in range(a):
		ans *= a
		a -= 1
	return ans

def comb(n,k):
	if n < k:
		print("n must bigger then k or equal to it ")
		return False 
	elif n == k:
		return 1
	else:
		ans = fact(n)/(fact(n-k)*fact(k))
		return ans

def bern(p,n,k):
	ans = comb(n,k) * p**k * (1-p)**(n-k)
	return ans

