from functools import partial

def add(x, y):
    return x + y

result = partial(add, 5)

print(result(3))
print(result(5))