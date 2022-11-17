def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)")
    return wrapper

#zumbido = funcion_decoradora(zumbido) #Sería lo mismo:
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

zumbido()