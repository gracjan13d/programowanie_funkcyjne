def sum_of_even(lst):
    return sum(x for x in lst if x % 2 == 0)

print(sum_of_even([1, 2, 3, 4, 5, 6]))