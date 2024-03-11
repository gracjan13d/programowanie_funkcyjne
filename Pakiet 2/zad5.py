is_palindrome = lambda s: s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]
print(is_palindrome("kajak"))
print(is_palindrome("coś"))
print(is_palindrome("Kamil Ślimak"))