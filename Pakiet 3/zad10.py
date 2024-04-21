def cumulative_sum(numbers):
    sum = 0
    cumulative_result = []
    for num in numbers:
        sum += num
        cumulative_result.append(sum)
    return cumulative_result

numbers = [1, 2, 3, 4, 5]
result = cumulative_sum(numbers)

print("Wynik:", result)
