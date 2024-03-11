words = ["hello", "world", "python", "functions"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)