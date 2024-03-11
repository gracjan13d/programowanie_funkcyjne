def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

evens = even_numbers()

print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))