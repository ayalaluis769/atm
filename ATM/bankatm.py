print('Welcome to the Python Bank ATM')

restart = ('Y')
chances = 3
balance = 999.99

while chances >= 0:
    pin = int(input('Please enter your 4 digit Pin: '))
    if pin == (1234):
        print('You enetered your pin Correctly')
        print('Please press 1 for your Balance')
        print('Please press 2 to make a Withdrawal')
        print('Please press 3 to make a Deposit')
        print('Please press 4 to Return your Card\n')
        while restart not in ('n','NO','no','N'):
           print('Please press 1 for your Balance')
           print('Please press 2 to make a Withdrawal')
           print('Please press 3 to make a Deposit')
           print('Please press 4 to Return your Card\n') 
           option = int(input('What would you like to choose?: '))
           if option == 1:
              print('Your Balance is $',balance)
              restart = input('Would you like to go back? ')
              if restart in ('n','NO','no','N'):
                  print('Thank You!') 
                  break
           elif option == 2:
               option2 = ('y')
               withdrawal = float(input('How much would you like to withdraw? 10,20,30,40,50,60,70,80,90,100 for other enter 1: '))
        if withdrawal in [10,20,30,40,50,60,70,80,90,100]:
            balance = balance - withdrawal
            print ('\nYour Balance is now $',balance)
            restart = input('Would you like to go back? ')
            if restart in ('n','NO','no','N'):
                print('Thank You')
                break
            elif withdrawal != [10,20,30,40,50,60,70,80,90,100]:
                print('Invalid Amount, Please Re-try\n')
                restart = ('y')
            elif withdrawal == 1:
                withdrawal = float(input('Please Enter Desired Amount: '))  
        elif option == 3:
            Deposit_in = float(input('How much would you like to Deposit? '))
            balance = balance + Deposit_in
            print ('\nYour Balance is now $',balance)
            restart = input('Would you like to go back? ')
            if restart in ('n','NO','no','N'):
                print('Thank You!') 
                break
        elif option == 4:
            print('Please wait while your card is Returned...\n')
            print('Thank you for banking with us!')
            break
        else:
            print('Please Enter a correct number. \n')
            restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Code')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break                                     