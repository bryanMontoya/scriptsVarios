def palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower() #Reemplazar espacio por vacío, todo en minúsculas.
    return string == string[::-1]

def run():
    print(palindrome(1000))

if __name__ == '__main__':
    run()