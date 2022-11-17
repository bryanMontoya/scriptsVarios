def removeDuplicates(someList : list) -> list:
    withoutDuplicates = []
    for element in someList:
        if element not in withoutDuplicates:
            withoutDuplicates.append(element)
    return withoutDuplicates


print(removeDuplicates([1,2,3,4,5,6,6,7,5,1,1]))

lista = [5,4,3,3,2,5,6]

print(list(set(lista)))
