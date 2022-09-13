price=10
price+=1
price*=10
print(price)#imprimir el valor
price=54.3
print(price)#Al asignar valores cambia el tipo de dato
price='Yes Me TOO'
print(price)
price=True
print(price)#Paso de booleano a entero suponiendo True = 1 y False = 0 
price*=10#La multiplicacion lo toma entero/flotante
print(price)#imprimir el valor
price=54.3
price*=10#El Flotante lo maneja igual con la multiplicacion
print(price)#Al asignar valores cambia el tipo de dato
price='Yes Me TOO '
price*=10#Repeticion de la cadena 10 veces
print(price)
price=True
price*=10#Convierte bool a int
print(price)
Patient_name='John Smith'
Patient_age=20
Patient_isnew=True
print('El paciente '+Patient_name+', con la edad de '+str(Patient_age)+
    ' anios')
if Patient_isnew==  True:
    print('Es un nuevo paciente')
else:
    print('Es una paciente ya registrado')