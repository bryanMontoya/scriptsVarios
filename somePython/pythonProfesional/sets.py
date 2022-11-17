#Set: Coleccion desordenada de elementos unicos e inmutables.
#Python elimina los repetidos.
my_set = {3,4,5, "hola", 22.3, False, True, 3}
print("my set =", my_set  )

my_set.add(10)
print("my set =", my_set  )

my_set.update([1,2,4])
print("my set =", my_set)

my_set.update({7,8,9})
print("my set =", my_set)

my_set.discard(99)
print("my set =", my_set) #Borrar exista o no.

#Se trata como diccionario.
empty_set = {}
print(type(empty_set))

#Se trata como set.
empty_set = set()
print(type(empty_set))

#Lista es un elemento mutable.
my_set = {3,4,5, "hola", 22.3, False, True, [1,2,6]} #TypeError
print("my set =", my_set  )

