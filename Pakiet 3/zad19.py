def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

string1 = "Listen"
string2 = "Silent"
if check_anagrams(string1, string2):
    print(f"String '{string1}' i string '{string2}' są anagramami.")
else:
    print(f"String '{string1}' i string '{string2}' nie są anagramami.")
