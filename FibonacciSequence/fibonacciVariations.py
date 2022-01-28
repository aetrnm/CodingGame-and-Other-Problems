MODULO = 1234567890


def fibNaive(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MODULO
    return a


def fibAdvanced(n):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = (v1 * v1 + calc) % MODULO, ((v1 + v3) * v2) % MODULO, (calc + v3 * v3) % MODULO
        if rec == '1':
            v1, v2, v3 = (v1 + v2) % MODULO, v1 % MODULO, v2 % MODULO
    return v2


def fibLong(n):
    a = []
    while n != 1:
        a.append(n & 1)
        n >>= 1
    f1 = 1
    f2 = 1
    while a:
        t = (f1 * (f2 * 2 - f1)) % MODULO
        f2 = (f2 * f2 + f1 * f1) % MODULO
        if a.pop() == 1:
            f1 = f2
            f2 += t
            f2 %= MODULO
        else:
            f1 = t
    return f1
