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

while True:

    print("          === Automated Teller Machine ===          ")
    user = input("Enter name to register: ")
    pin = input("Enter PIN: ")

    balance = 0
    #print(user, "has been registered with a starting balance of $", balance)
    name_to_validate = user
    pin_to_validate = pin
    if (name_to_validate == user) and (pin_to_validate == pin):
        print("Login Succesful!")
        break
    elif (name_to_validate != user) and (pin_to_validate == pin):
        print("Invalid credentials")
    else:
        print("Invalid credentials") 

while True:
    atm_menu(user)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        account.deposit(balance) 
           
