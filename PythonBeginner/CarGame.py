
help_message='''start - to start the car
stop - to stop the car
quit - to exit'''
while True:
    answer=input('>').lower()
    if answer=='start':
        print('Car started...Ready to go!')
        state='start'
    elif answer=='stop':
        print('Car stopped.')
        state='stop'
    elif answer=='help':
        print(help_message)
    elif answer=='quit':
        break
    else:
        print("I don't understand that...")
started=False
repeated=0
while True:
    answer=input('>').lower()
    if answer=='start':
        if started:
            repeated+=1
            print('Car already started!')
        else:
            print('Car started...Ready to go!')
            started=True
            repeated=0
    elif answer=='stop':
        if started:
            print('Car stopped.')
            started=False
            repeated=0
        else:
            repeated+=1
            print('Car already stopped!')
    elif answer=='help':
        print(help_message)
    elif answer=='quit':
        break
    else:
        print("I don't understand that...")
    if repeated>0:
        print('bruh!'*repeated)
