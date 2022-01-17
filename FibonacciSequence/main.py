import decimal

def binpow (a, n=1):
	res = 1
	while n:
		if (n & 1): res *= a
		a *= a
		n >>= 1
	return res

def getFibonacciNumber(n):
    decimal.getcontext().prec = 100

    root_5 = decimal.Decimal(5).sqrt()
    phi = (1 + root_5) / 2

    a = binpow(phi, n) / (root_5)

    return a

    

print(getFibonacciNumber(1000000))