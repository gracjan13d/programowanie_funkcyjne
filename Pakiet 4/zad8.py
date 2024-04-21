def most_frequent(lst):
    return max(set(lst), key=lst.count)


print(most_frequent([1, 2, 3, 2, 2, 4, 5, 2]))  