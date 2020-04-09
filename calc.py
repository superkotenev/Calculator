import math

def fact(a):
	ans = 1
	for i in range(a):
		ans *= a
		a -= 1
	return ans

def comb(n,k):
	if n < k:
		return 0
	# elif n == k:
	# 	return 1
	else:
		ans = fact(n)/(fact(n-k)*fact(k))
		return ans

def array(m,n):
	array = []
	for i in range(1,m+1):
		array.append([])
		for e in range(1,n+1):
			array[i].append([])
	return array

# for i in range(1,5+1):
# 	print(i)

def bern(p,n,k):
	try:
		k = int(k)
		ans = comb(n,k) * p**k * (1-p)**(n-k)
		return ans
	except:
		if k[1] == "=":
			if k[0] == "<":
				ans = 0
				for i in range(int(k[2:])+1):
					ans += comb(n,i) * p**i * (1-p)**(n-i)
				return ans
			else:
				ans = 0
				for i in range(int(k[2:]),n):
					ans += comb(n,i) * p**i * (1-p)**(n-i)
				return ans
		else:
			if k[0] == "<":
				ans = 0
				for i in range(int(k[1:])):
					ans += comb(n,i) * p**i * (1-p)**(n-i)
				return ans
			else:
				ans = 0
				for i in range(int(k[1:])+1,n+1):
					ans += comb(n,i) * p**i * (1-p)**(n-i)
				return ans

def lotto(n,h,k,p):
	try:
		p = int(p)
		ans = comb(h,p)*comb((n-h),(k-p))/comb(n,k)
		return ans
	except:
		if p[1] == "=":
			if p[0] == "<":
				ans = 0
				for i in range(int(p[2:])+1):
					ans += comb(h,i)*comb((n-h),(k-i))/comb(n,k)
				return ans
			else:
				ans = 0
				for i in range(int(p[2:]),k+1):
					ans += comb(h,i)*comb((n-h),(k-i))/comb(n,k)
				return ans
		else:
			if p[0] == "<":
				ans = 0
				for i in range(int(p[1:])):
					ans += comb(h,i)*comb((n-h),(k-i))/comb(n,k)
				return ans
			else:
				ans = 0
				for i in range(int(p[1:])+1,k+1):
					ans += comb(h,i)*comb((n-h),(k-i))/comb(n,k)
					print(i)
				return ans

def minmin(p,a):
	ans = math.log(1-a)/math.log(1-p)
	return math.ceil(ans)

# def viertafel():
#
#
# print(viertafel())


# Bernulli input

n = int(input('Enter n: '))
k = input('Enter k: ')
p = float(input('Enter p: '))

print(bern(p,n,k))

# Lottomodell input
#
# n = int(input('Enter n: '))
# k = int(input('ENter k: '))
# h = int(input('Enter h: '))
# p = input('Enter p: ')
#
# print(lotto(n,h,k,p))

# MindestensMindestensMindestens input
#
# p = float(input('Enter p: '))
# a = float(input('Enter a: '))
#
# print(minmin(p,a))

# https://www.abiturma.de/mathe-lernen/stochastik/wichtige-grundbegriffe/die-vierfeldertafel
