#List []
names=['John','Bob','Mosh','Sarah','Mary']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[2:])#Exactamente igual al string
print(names[2:4])
names[0]='JOn' #Accesamos los valores individualmente
#Exercise
numbers=[3,6,2,4,6,10]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(f"Max value: {max}")