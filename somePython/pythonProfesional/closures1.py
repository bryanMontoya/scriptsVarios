def multipleString(string):

    assert type(string) == str, "solo puedes usar cadenas"
    
    def numberString(n):
        
        return string * n
    
    return numberString


hola = multipleString("hola")
print(hola(3))

