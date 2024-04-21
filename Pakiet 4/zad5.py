def split_list(lst, max_length):
    return [lst[i:i + max_length] for i in range(0, len(lst), max_length)]


print(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) 