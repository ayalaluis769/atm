def show_balance(balance):
    print("Current Balance: $", float(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return float(balance + amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    return float(balance - amount)

def logout(name):
    print("Goodbye", name)