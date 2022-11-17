#Función que recibe como parámetro una función, le añade cosas, la modifica y la retorna.
def decorador(func):
    def envoltura():
        print('Esto es un saludito.')
        func()
    return envoltura

def saludo():
    print('Hola')

saludito = decorador(saludo)
saludito()
