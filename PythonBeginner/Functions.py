#Para las funciones necesitan estar declaradas antes de la llamada
def greet_user():
    print('Hi there!')
    print("Welcome aboard")

print("Start")
greet_user()
print("Finish")

def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard!")

print("Start")
greet_user("John")
greet_user("Mary")
#greet_user() Esta secuencia no es valida por que esta pidiendo la funcion un valor
print("Finish")
def greet_user(first_name,last_name):
    print(f"Hi, {first_name} {last_name}")
    print("Welcome aboard")
print("Start")
#Esta implementacion se le llama keyword argument
greet_user(last_name="Smith",first_name="John")
#Para especificar claramente cual valor se le esta pasando
print("Finish")
def square(number):
    return number*number
result=square(3)#Si no tiene return la funcion la asignacion pone None
print(result)
print(square(3))