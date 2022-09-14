def triangular(n):
    res = 0
    for _ in range(n):
        res += n
        n -= 1
    return res

print(triangular(5))