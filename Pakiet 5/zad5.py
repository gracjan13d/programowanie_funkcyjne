def liczby_parzyste(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(liczby_parzyste(liczby))

pole_p= lambda a, b: a * b

a = 8
b = 5

print(pole_p(a, b))