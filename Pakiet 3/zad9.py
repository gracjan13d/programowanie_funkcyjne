def zip_with_index(lst):
    return [(element, index) for index, element in enumerate(lst)]

my_list = ["apple", "banana", "orange", "grape"]
result = zip_with_index(my_list)

print("Wynik:", result)
