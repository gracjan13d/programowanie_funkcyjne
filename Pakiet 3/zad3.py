def recursive_sum(numbers):

    sum = 0
    for element in numbers:
        if isinstance(element, list):
            sum += recursive_sum(element)
        else:
            sum += element
    return sum

numbers = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
sum = recursive_sum(numbers)

print("Wynik:", sum)