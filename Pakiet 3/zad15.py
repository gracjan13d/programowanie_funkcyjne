def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)

strings_list = ["apple", "banana", "watermelon", "pineapple"]
sorted_list = custom_sort(strings_list, key_func=len)
print("Wynik:", sorted_list)
