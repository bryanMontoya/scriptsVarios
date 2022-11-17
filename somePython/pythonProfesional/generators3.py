import time

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    while counter <= max:
        if counter == 0:            
            yield n1
        elif counter == 1:            
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux            
            yield aux
        counter += 1

if __name__ == '__main__':
    fibonacci = fibo_gen(max = 10)
    for n in fibonacci:
        print(n)
        time.sleep(0.5)