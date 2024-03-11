def add(x):
    def inner(y):
        return x+y
    return inner

result = add(5)