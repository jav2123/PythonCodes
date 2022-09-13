numbers=[5,2,1,7,4]
numbers.append(20)
print(numbers)
numbers.insert(0,10)#Inserta al inicio de la lista
numbers.insert(4,25)#Inserta en indice
print(numbers)
numbers.remove(5)#Remueve el item
numbers.clear()#Vacia la lista
print(numbers)
numbers.append(20)
numbers.append(50)
numbers.append(12)
numbers.pop()#Remueve el ultimo item de la lista
print(numbers.index(50))#Esta implementacion puede regresar error si no esta en 
#la lista
print(50 in numbers)
print(numbers.count(12))#Regresa el numero de veces que aparece cierto item
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2=numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)
items=[1,2,3,1,2,5,4,6]
print(items)
for item in items:
    if items.count(item)>1:
        for count in range(items.count(item)-1):
            items.remove(item)
print(items)