def count_unique_elements(numbers):
    unique_elements = set(numbers)
    return len(unique_elements)

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
unique_count = count_unique_elements(numbers)
print("Wynik:", unique_count)
