def return_list(lst, function):
    return [function(element) for element in lst]


print(return_list([1, 2, 3], lambda x: x ** 2))
