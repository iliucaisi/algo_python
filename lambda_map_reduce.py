from functools import reduce

s = lambda a, b, c : a + b + c

print(s(1, 2, 3))

ls1 = (1, 2, 3, 4, 5, 6)
ls2 = map(lambda x : x * 2, ls1)

for i in ls2:
    print(i, end=' ')
print()

def add(x, y):
    return x + y
print(reduce(add, ls1))
