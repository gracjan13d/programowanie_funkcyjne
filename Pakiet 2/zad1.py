from itertools import product

list1 = ['A', 'B']
list2 = ['C', 'D']

combinations = product(list1, list2)

for combination in combinations:
    print(combination)