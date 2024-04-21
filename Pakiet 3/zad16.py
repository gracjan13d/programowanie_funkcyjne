def remove_whitespace(str_list):
    return [s.replace(" ", "") for s in str_list]

str_list = ["  apple ", "banana  ", "  watermelon  ", "pineapple"]
cleaned_list = remove_whitespace(str_list)
print("Wynik:", cleaned_list)
