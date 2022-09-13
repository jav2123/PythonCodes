from email import message


course="Python's Course for Beginners"
course2='Python Course for "Beginners"'
print(course)
print(course2)
course_message='''
Hi John,

Here is our first email to you.

Thank you,

The support team
'''
print(course_message)
#'''Puedes acceder a los strings como arreglos'''
print(course[1])#Segundo caracter
print(course[-1])#Ultimo caracter
print(course[-2])#Penultimo caracter
print(course[0:3])#Desde el primer caracter hasta el 3er caracter 0-2 = 3 
print(course[10:])#Desde el caracter hasta el final de la cadena
print(course[:5])#Python asumira el primer caracter hasta el 5to caracter
print(course[:])#Python asumira desde el primer caracter 
#hasta el final de la cadena
name='Jennifer'
print(name[1:-1])#Imprime desde el segundo caracter hasta el penultimo
#excluye el caracter de index -1