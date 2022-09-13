temperature=int(input("What's the temperature? "))#Suponiendo celsius
if temperature>30:
    print("It's a hot day")
elif temperature<10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")
'''
mayor o igual/menor o igual/igual/diferente
<=/>=/==/!=
'''
#Exercise
name=input("What's your name? ")
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")