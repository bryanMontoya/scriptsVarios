my_list = [1,4,5,6,8,13,19,21]

#Map
odd = list(filter(lambda x: x%2 !=0, my_list))
#print(odd)

#Filter
odd = list(map(lambda x: x**2, my_list))
#print(odd)

#Reduce
from functools import reduce
odd = reduce(lambda a,b: a*b, my_list)
print(odd)
