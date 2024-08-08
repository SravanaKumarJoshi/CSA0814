def is_smith_number(n):
    s = lambda x: sum(int(d) for d in str(x))
    f, d, factors = n, 2, []
    while d * d <= f:
        while f % d == 0:
            factors.append(d)
            f //= d
        d += 1
    if f > 1: factors.append(f)
    return len(factors) > 1 and s(n) == sum(map(s, factors))
number = 666
print(is_smith_number(number))  # Output: True
