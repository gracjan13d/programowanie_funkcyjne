def apply_function_to_tuples(lst, function):
    return [function(*tuple) for tuple in lst]


print(apply_function_to_tuples([(1, 2), (3, 4), (5, 6)], lambda x, y: x + y))
