def pangkat(x, y):
    if y == 1:
        return x
    return x * pangkat(x, y - 1)

print(pangkat(3, 2))