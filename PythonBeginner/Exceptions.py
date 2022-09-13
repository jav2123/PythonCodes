from csv import excel_tab


try:
    age=int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')
#regular try catch pa que no crashe :c
try:
    age=int(input('Age: '))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')
    #Se puede poner multiples excepciones
    #
    #