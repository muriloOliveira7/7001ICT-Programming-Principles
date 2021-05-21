#7001ICT Programming Principles, Workshop 10, 3.1 Problem 1

class GoCard:
    def __init__(self, balance):
        self.balance = balance
        self.transactionList = [balance]
 
    def add_transaction(self, transaction):
        """Add new transaction to the Transaction list."""
        self.transactionList.append(transaction)
    
    def update_balance(self, transaction):
        """Update the GoCard balance with the new transction."""
        self.balance = self.balance + transaction

    def current_balance(self):
        """Print the GoCard current balance."""
        print ('Balance = $'+'%.2f' %self.balance)
    
    def full_statement(self):
        """Print the Transaction list with a balance update per transaction."""
        print ('Statement:')
        #Save the initial balance
        transactionBalance = self.transactionList[0]
        for i in range (len(self.transactionList)):
            #Print condition for the first line
            if i == 0:
                print ("{:<8} {:>20} {:>13}".format('event','amount ($)','balance ($)'))
                print ("{:<8} {:>27}".format('Initial Balance',"%.2f" % transactionBalance))
            #Print condition for the next lines
            else:
                #Update the balance with the current transaction
                transactionBalance = transactionBalance + self.transactionList[i]
                #Condition for Top up
                if self.transactionList[i]>0:
                    print ("{:<8} {:>20} {:>13}".format('Top up',"%.2f" % self.transactionList[i],"%.2f" % transactionBalance))
                #Condition for Ride
                else:
                    print ("{:<8} {:>20} {:>13}".format('Ride',"%.2f" % (self.transactionList[i]*-1),"%.2f" % transactionBalance))
            #Print the final balance in the last line
            if i == (len(self.transactionList)-1):
                print ("{:<8} {:>29}".format('Final Balance',"%.2f" % transactionBalance))

#Validate initial balance
while True:
    try:
        userInput = float(input('Creating account. Input initial balance: '))
        userGoCard = GoCard(userInput)
        break
    except:
        print ('Enter a valid number.')

while True:
    userInput = input('? ')
    # Exit condition
    if userInput == 'q':
        userGoCard.full_statement()
        break
    
    #Split input string
    userInputList = userInput.split()

    #Ride and Top up condition
    if len(userInputList) == 2:
        #Validate the input number
        try:
            if userInputList [0] == 'r':
                userGoCard.add_transaction(float(userInputList[1])*-1)
                userGoCard.update_balance(float(userInputList[1])*-1)
            elif userInputList [0] == 't':
                userGoCard.add_transaction(float(userInputList[1]))
                userGoCard.update_balance(float(userInputList[1]))
            else:
                print ('Bad command.')
        except:
            print ('Enter a valid value')
    #Print condition
    elif userInputList[0] == 'b':
        userGoCard.current_balance()
    else:
        print ('Bad command.')