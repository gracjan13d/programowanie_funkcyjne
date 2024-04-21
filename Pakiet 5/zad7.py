def kwadrat(x):
    return x ** 2

def dodaj5(x):
    return x + 5

liczby = [1, 2, 3, 4, 5]

def funkcja(liczby, funkcje):
    return [funkcja(element) for element in liczby for funkcja in funkcje]

funkcje = [kwadrat, dodaj5]

print(funkcja(liczby, funkcje))