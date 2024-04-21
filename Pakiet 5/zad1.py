def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez 0!"

def potega(a, b):
    return a ** b

print(dodawanie(1,2))
print(odejmowanie(5,2))
print(mnozenie(3,2))
print(dzielenie(4,2))
print(potega(2,3))