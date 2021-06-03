#7001ICT Programming Principles, Workshop 9, 3.1 Problem 1

#def assign ():

vars = {}

print('Welcome to the Adder REPL.')

while True:
    userInput = input('??? ')
    if userInput == 'quit':
        print('Goodbye.')
        break
    
    userInputList = userInput.split()

    if not userInput:
        print('Please enter a valid command.')
    
    elif (len(userInputList) < 2):
        print ('Syntax error.')

    
    elif userInputList[0] == 'print':
        if userInputList[1].isalpha():
            if userInputList[1] in vars:
                print (userInputList[1],'equals',vars[userInputList[1]])
            else:
                print (userInputList[1],'is undefined.')
        elif userInputList[1].isdigit():
            print (userInputList[1])
        else:
            print ('Syntax error.')
    elif userInputList[0] == 'input':
        if userInputList[1].isalpha():
            print ('Enter a value for', userInputList[1], end = '')
            vars[userInputList[1]] = int(input(': '))
    elif len(userInputList[0])==1:
        if userInputList[0].isalpha():
            if userInputList[1]== 'gets':
                if userInputList[2].isdigit():
                    vars[userInputList[0]] = userInputList[2]
                elif userInputList[2] in vars:
                    vars[userInputList[0]] = vars[userInputList[2]]
                else:
                    print ('Syntax error.')
            elif userInputList[1]== 'adds':
                if userInputList[2].isdigit() or userInputList[2].isalpha():
                    vars[userInputList[0]] = int(vars[userInputList[0]]) + int(vars[userInputList[2]])
                else:
                    print ('Syntax error.')
        else:
            print ('Syntax error.')
    else:
        print ('Syntax error.')


