#Podemos iterar sobre strings
for item in 'Python':
    print(item)
print('--------')
#Podemos definir una lista con []
for item in ['Mosh','John','Sara']:
    print(item)
print('--------')
for item in [1,2,3,4,5,6,7]:
    print(item)
print('--------')
#Tenemos la funcion range built-in python
for item in range(10):#Desde 0 hasta 9
    print(item)
print('--------')
for item in range(5,10):#Desde 5 hasta 9
    print(item)
print('--------')
for item in range(5,10,2):#Desde 5 hasta 9 en pasos de 2 unidades
    print(item)
print('--------')
prices=range(10,31,10)
total=0
for item in prices:
    total+=item
print(total)