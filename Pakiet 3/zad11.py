def find_max_min_diff(numbers):
    if not numbers:
        return None 
    else:
        max_val = max(numbers)
        min_val = min(numbers)
        return max_val - min_val

numbers = [1, 8, 3, 10, 5]
diff = find_max_min_diff(numbers)
print("Wynik:", diff)
