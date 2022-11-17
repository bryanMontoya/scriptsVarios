my_set1 = {3,4,5,True,3}
my_set2 = {13,14,15,True,13}

#Union.
my_set3 = my_set1 | my_set2
print(my_set3)

#Intersección.
my_set3 = my_set1 & my_set2
print(my_set3)

#Diferencia.
my_set3 = my_set1 - my_set2
print(my_set3)

my_set3 = my_set2 - my_set1
print(my_set3)

#Diferencia simétrica.
my_set3 = my_set1 ^ my_set2
print(my_set3)
