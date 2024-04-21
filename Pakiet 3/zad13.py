def split_list(numbers, list_size):
    return [numbers[i:i+list_size] for i in range(0, len(numbers), list_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_size = 3
splitted = split_list(numbers, list_size)
print("Wynik:", splitted)
