def capitalize_all_words(text):
    return ' '.join(word.capitalize() for word in text.split())

text = "this is an example text."
capitalized_text = capitalize_all_words(text)
print("Wynik:", capitalized_text)
