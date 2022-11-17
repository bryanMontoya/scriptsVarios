def divisors(num):
    try:
        if (num < 0):
            raise ValueError("Solo numeros positivos.")
        return [i for i in range(1, num + 1) if num % i == 0]
    except ValueError as ve: 
        print(ve)
        return False

def run():
    try:
        print(divisors(int(input("Ingresa un número:"))))    
        print("End.")
    except ValueError:
        print("Caracter invalido.")

if __name__ == '__main__':
    run()