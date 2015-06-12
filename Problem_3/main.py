import time

def isprime(n):
    if n < 7:
        if n in (2, 3, 5):
            return True
        else:
            return False

    if n & 1 == 0:
        return False

    k = 3
    sqrtn = heronsqrt(n)

    while k <= sqrtn:
        if n % k == 0:
            return False
        k += 2

    return True

def heronsqrt(n):
    s1 = 1
    while True:
        s2 = (s1 + n // s1) // 2
        if abs(s1 - s2) < 2:
            if s1 * s1 <= n and (s1 + 1) * (s1 + 1) > n:
                return s1
        s1 = s2

def factorsdiv2(n):
    pstack = [2, 3, 5, 7, 11]
    sqrtn = heronsqrt(n)

    for p in pstack:
        if p > sqrtn:
            return [n, 1]
        if n % p == 0:
            return [p, n // p]

    p = pstack[-1] + 2

    while p <= sqrtn:
        if n % p == 0:
            return [p, n // p]
        p += 2

    return [n, 1]

def process(n):
    factors = []
    stack = [n]
    while len(stack) != 0:
        x = stack.pop(-1)
        if(x == 1):
            continue
        if isprime(x):
            factors.append(x)
        else:
            xa, xb = factorsdiv2(x)

            stack.append(xa)
            stack.append(xb)
    factors.sort()
    return factors

def main():
    n = 600851475143

    factors = process(n)

    print(factors)

if __name__ == '__main__':
    main()
