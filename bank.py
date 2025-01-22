class bank():
    def __init__(s,account_holder,account_balance,account_pin):
        s.account_holder=account_holder
        s.account_balance=account_balance
        s.account_pin=account_pin
    def check_balance(account_balance):
        return f"Your current balance is: {account_balance}"
    def deposit(s,amount,account_balance):
        if amount>0:
            s.account_balance+=amount
            return f" ₹{amount} is deposited to your account successfully. Now your account balance is ₹{account_balance}"
        else:
            return "Deposit money should not be less than ₹1"
    def validate_pin(s,pin):
        return s.account_pin == pin
    def withdraw(s,amount,pin):
        if s.validate_pin(pin):
            if s.account_balance<=amount:
                s.account_balance-=amount
                return f" ₹{amount} is withdrawn successfully"
            else:
                return "Insufficient Balance in your account"
        else:
            return "Invalid PIN"
    def change_pin(s,pin,new_pin):
        if s.validate_pin(pin):
            if len(pin)==4 and new_pin.isdigit():
                s.account_pin=new_pin
                return "PIN changed successfully"
            else:
                return "PIN must contain 4 digits only"
        else:
            return "Invalid PIN"

def menu(customer):
    while True:
        print(" 1.Check account balance.\n 2.Deposit money.\n 3.Withdraw money.\n 4.Change PIN.\n 5.Exit.")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            print(customer.check_balance())
        elif choice == 2:
            amount=float(input("Enter the amount you want to deposit: "))
            print(customer.deposit(amount))
        elif choice == 3:
            amount=float(input("Enter the amount you want to withdraw: "))
            pin=int(input("Enter your PIN: "))
            print(customer.withdraw(amount,pin))
        elif choice == 4:
            pin=int(input("Enter the PIN: "))
            new_pin=int(input("Enter the New PIN: "))
            print(customer.change_pin(pin,new_pin))
        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Please select a valid choice.")

def main():
    print("--- ATM Machine ---")

    customer1= bank("Tharun",20000,2002)
    customer2= bank("Manas",40000,2004)
    customer3= bank("Vikas",50000,2003)
    customer4= bank("Charan",10000,2001)

    menu(customer1)
    
if __name__ == "__main__":
    main()