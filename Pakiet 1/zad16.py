def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def add(x):
    return x + 2

def multiply(x):
    return x * 3

result = compose(add, multiply)
print(result(3))