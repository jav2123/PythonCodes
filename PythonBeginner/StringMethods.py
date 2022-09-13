course='Python for Beginners'
print(len(course))#len es utilizado para muchas cosas en python es una funcion
#built-in
#course.upper()#Puedes acceder a los metodos del objeto en este caso str
print(course.upper())#crea una nueva cadena no modifica el contenido 
#si no es asignado a la variable
print(course.lower())
print(course)
print(course.find('P'))#Index of caracter
print(course.find('o'))#Index of caracter Case sensitive
print(course.find('0'))#Si no existe en la cadena regresa -1
print(course.find('Beginners'))
print(course.replace('Beginners','Absolute Begginers'))#Reemplaza la cadena vieja
#por una nueva
#No importa cual metodo uses si no sobreescribes el valor solo se genera la nueva cadena
print('Python' in course)#Regresa booleano si existe o no dentro de la cadena
'''
len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
'...' in course
'''