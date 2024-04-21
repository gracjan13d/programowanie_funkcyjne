def partition_list(lst, condition):
    true_part = [x for x in lst if condition(x)]
    false_part = [x for x in lst if not condition(x)]
    return true_part, false_part

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = partition_list(numbers, is_even)

print("Liczby parzyste:", even_numbers)
print("Liczby nieparzyste:", odd_numbers)
