from os import name
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")



print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0

print(name, "has been registered with a starting balance of $" + str(balance))

while True:
    
    print("          === Automated Teller Machine ===          ")
    print("\nLOGIN")
    user_name = input("Enter name: ")
    user_pin = input("Enter PIN: ")

    if (user_name == name) and (user_pin == pin):
        print("Login successful!")
        break
    else:
        print("Invalid Credentials!")
    
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)    
    elif option == "2":
        
        balance = account.deposit(balance)
        account.show_balance(balance)

    elif option == "3":
        
        balance = account.withdraw(balance)
        account.show_balance(balance)
        
    elif option == "4":       
       account.logout(name)
       break 
    else:
        print("Wrong Choice!")