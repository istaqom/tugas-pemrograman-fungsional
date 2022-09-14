def sum_squares(x):
    res = 0
    for i in x:
        res += i ** 2
    return res

print(sum_squares([1, 2, 3]))