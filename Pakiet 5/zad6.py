slowa = ["arbuz", "banan", "jablko", "ananas"]

print(list(filter(lambda x: x.startswith('a'), slowa)))

liczby = [1, 2, 3, 4, 5]

kwadraty = list(map(lambda x: x ** 2, liczby))

print(kwadraty)