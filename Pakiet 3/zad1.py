def double_list_elements(numbers):
    numbers_list = [x * 2 for x in numbers]
    return numbers_list

normal_list = [2, 4, 5, 8]
numbers_list = double_list_elements(normal_list)

print("Wynik:", numbers_list)
