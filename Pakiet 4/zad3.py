def filter_even(dictionary):
    return {k: v for k, v in dictionary.items() if v % 2 == 0}


print(filter_even({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
