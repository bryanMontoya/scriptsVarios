from datetime import datetime

def execution_time(func):   
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper

@execution_time
def random_fun():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a : int, b : int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Brayan"):
    print (f'Hola {nombre}')

random_fun()
suma(1, 2)
saludo()

#*args, **kwargs: No importa la cantidad de argumentos posicionales o nombrados.


