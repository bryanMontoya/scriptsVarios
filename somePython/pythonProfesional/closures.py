#Condiciones closures.
#1) Funcion nested.
#2) Que se retorne la función nested.
#3) Que se referencie un valor de un scope superior.

def make_multiplier(x):
    
    #Nested function
    def multiplier(n):
        #Se referencia valor de scope superior.
        return x * n
    
    #Se retorna función nested.
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))