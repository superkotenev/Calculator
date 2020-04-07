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

def lotto(n,h,k,p):
	if type(p) == int:
		ans = comb(h,p)*comb((n-h),(k-p))/comb(n,k)
		return ans
	elif p[1] == "=":
		if p[0] == "<":
			ans = 0
			p = int(p[2:])
			for i in range(p):
				ans += comb(h,p)*comb((n-h),(k-p))/comb(n,k)
			return ans

n = int(input('Enter n: '))
k = int(input('Enter k: '))
h = int(input('Enter h: '))
p = int(input('Enter p: '))

print(lotto(n,h,k,p))
