'''
while condition:
    ...
'''
i=1
while i<=5:
    print(i)
    i=i+1
print("Done")
i=1
while i<=5:
    print('*'*i)
    i=i+1
print("Done")
#Exercise
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess == secret_number:
        print("You won!")
        break
else: #esta parte del codigo no se ejecuta si sale del while con un break
    print("You failed!")
#Entra al codigo si el while termina