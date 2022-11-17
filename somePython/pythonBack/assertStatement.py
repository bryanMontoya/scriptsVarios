def palindrome(string):
    assert len(string) > 0, "Cadena vacía."
    return string == string[::-1]

print(palindrome("")) 