def remove_duplicates(numbers):
    seen = set()
    result = []
    for item in numbers:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8]
unique_list = remove_duplicates(numbers)

print("Wynik:", unique_list)