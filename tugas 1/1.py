def sum_squares(x):
    res = [i ** 2 for i in x]
    return sum(res)

print(sum_squares([1, 2, 3]))