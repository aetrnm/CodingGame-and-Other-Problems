import decimal
import math

MODULO = 1234567890


def binpow(a, n=1):
    res = 1
    while n != 0:
        print('RES: %d N: %d A: %d ' % (res, n, a))
        if n % 2 != 0:
            res *= a
            res %= MODULO
        a *= a
        a %= MODULO
        n //= 2
    return res


def getFibonacciNumber(n):
    decimal.getcontext().prec = 100
    k = 76

    root_5 = math.sqrt(5)
    phi = (1 + root_5) / 2

    phiPowK = phi ** k
    print("phipowK:", phiPowK)
    phiPowKX = binpow(phiPowK, n // k)
    print("phipowKX:", phiPowKX)
    phiPowR = phi ** int(n % k)
    print(phiPowR)
    print("phipowR:", phiPowR)

    a = phiPowKX * (phiPowR / root_5) % MODULO

    return a


print(getFibonacciNumber(10))
