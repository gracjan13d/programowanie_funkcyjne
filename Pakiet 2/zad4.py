numbers = [32, 2, 5, 1, 52]

squared_greater_than_10 = [x**2 for x in numbers if (square := x**2) > 10]

print(squared_greater_than_10)