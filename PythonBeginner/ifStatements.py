is_hot=False
if is_hot:#al ser booleano no es necesario preguntar si es igual a cierto valor
    print("It's a hot day")
    print('Drink plenty of Water!')
else:
    print("It's a cold day")
    print("Wear warm clothes!")
print('Enjoy your day!')
print('----------------')
is_cold=False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of Water!')
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes!")
else:
    print("It's a lovely day")
#Exercise
price=1000000
buyer_good_credit=False
if buyer_good_credit:
    print('You only have to put down: '+str(price*.1))
else:
    print('You only have to put down: '+str(price*.2))
#Another solution
if buyer_good_credit:
    money=price*.1
else:
    money=price*.2
print("You only have to put down: "+str(money))#Podemos usar formated string para
#evitar el uso del parser str() directamente en el codigo
print(f"Down payment: {money}")