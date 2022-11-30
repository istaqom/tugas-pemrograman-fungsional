import random
def create_app(l: list):
    s = lambda l: sorted(l)
    l = s(l)

    def append(v):
        l.append(v)

    def set_sort(sorter):
        nonlocal s
        s = sorter

    def sort():
        nonlocal l
        l = s(l)

    def get():
        nonlocal l
        return l

    return append, set_sort, sort, get
    
append, set_sort, sort, get = create_app([1,2,3,4])

sort()
print(get())

set_sort(lambda x: sorted(x, reverse=True))
sort()
print(get())

set_sort(lambda x: sorted(x, key=lambda _: random.random()))
sort()
print(get())