def rotate_list(numbers, steps):
    if not numbers:
        return []
    
    steps = steps % len(numbers)
    rotated_list = numbers[-steps:] + numbers[:-steps]
    
    return rotated_list

numbers = [1, 2, 3, 4, 5]
steps = 2
rotated_list = rotate_list(numbers, steps)
print("Wynik:", rotated_list)
