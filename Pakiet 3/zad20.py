def sum_of_squares_of_odds(numbers):
    return sum(x ** 2 for x in numbers if x % 2 != 0)

numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_squares_of_odds(numbers)
print("Wynik:", result)
