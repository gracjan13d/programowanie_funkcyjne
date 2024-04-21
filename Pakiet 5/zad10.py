def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen_fibonacci = fibonacci()
for _ in range(25):
    print(next(gen_fibonacci), end=" ")




def czytaj_plik(nazwa):
    with open(nazwa, "r") as plik:
        for linia in plik:
            yield linia

generator = czytaj_plik("tekstowy.txt")
for _ in range(3):
    print(next(generator), end="")
