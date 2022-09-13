#Tupla ()
numbers=(1,2,3) #Tupla de numeros
'''numbers.count numbers.index'''
#No se puede modificar una tupla de objetos
#Puedes acceder a la informacion pero no modificarla
print(numbers[0])
coordinates=(1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
#Unpacking
x,y,z=coordinates
#Exactamente lo mismo
print(f'{x},{y},{z}')