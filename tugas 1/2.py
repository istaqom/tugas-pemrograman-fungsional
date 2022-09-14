def triangular(n):
    res = [i for i in range(n, 0, -1)]
    return sum(res)

print(triangular(5))