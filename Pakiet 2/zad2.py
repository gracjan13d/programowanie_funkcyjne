from itertools import combinations

def generate_combinations(elements):
    combinations_list = list(combinations(elements, 2))
    return combinations_list

elements = [1, 2, 3, 4]
result = generate_combinations(elements)
print(result)