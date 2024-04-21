from functools import reduce

liczby = [1, 2, 3, 4, 5]

najwiekszaliczba = reduce(lambda x, y: x if x > y else y, liczby)

print(najwiekszaliczba)

srednia = reduce(lambda x, y: x + y, liczby) / len(liczby) if liczby else 0

print(srednia)