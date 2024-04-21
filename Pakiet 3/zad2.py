def filter_long_words(strings_list):

    avg_length = sum(len(s) for s in strings_list) / len(strings_list)
    filtered_list = [s for s in strings_list if len(s) > avg_length]

    return filtered_list

strings_list = ["apple", "banana", "watermelon", "pineapple"]
filtered_list = filter_long_words(strings_list)

print("Wynik:", filtered_list)