class bank:
    def __init__(self, account_number, account_holder, account_balance, account_pin):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance
        self.account_pin = account_pin

    def check_balance(self):
        return f"Your current balance is: ₹{self.account_balance}"

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"₹{amount} is deposited to your account successfully. Now your account balance is ₹{self.account_balance}"
        else:
            return "Deposit money should not be less than ₹1"

    def validate_pin(self, pin):
        return self.account_pin == pin

    def withdraw(self, amount, pin):
        if self.validate_pin(pin):
            if self.account_balance >= amount:
                self.account_balance -= amount
                return f"₹{amount} is withdrawn successfully. Remaining balance: ₹{self.account_balance}"
            else:
                return "Insufficient Balance in your account"
        else:
            return "Invalid PIN"

    def change_pin(self, pin, new_pin):
        if self.validate_pin(pin):
            if len(str(new_pin)) == 4 and str(new_pin).isdigit():
                self.account_pin = new_pin
                return "PIN changed successfully"
            else:
                return "New PIN must contain exactly 4 digits"
        else:
            return "Invalid PIN"


def find_by_account_number(customers, account_number):
    for customer in customers:
        if customer.account_number == account_number:
            return customer
    return None


def menu(customer):
    while True:
        print("\n1. Check account balance\n2. Deposit money\n3. Withdraw money\n4. Change PIN\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(customer.check_balance())
        elif choice == 2:
            amount = float(input("Enter the amount you want to deposit: "))
            print(customer.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter the amount you want to withdraw: "))
            pin = int(input("Enter your PIN: "))
            print(customer.withdraw(amount, pin))
        elif choice == 4:
            pin = int(input("Enter your current PIN: "))
            new_pin = int(input("Enter the new PIN: "))
            print(customer.change_pin(pin, new_pin))
        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Please select a valid choice.")


def main():
    print("--- ATM Machine ---")

    customers = [
        bank(1001, "Tharun", 20000, 2002),
        bank(1002, "Manas", 40000, 2004),
        bank(1003, "Vikas", 50000, 2003),
        bank(1004, "Charan", 10000, 2001)
    ]

    while True:
        account_number = int(input("\nEnter your account number: "))
        customer = find_by_account_number(customers, account_number)
        if customer:
            print(f"Welcome, {customer.account_holder}!")
            menu(customer)
            break
        else:
            print("Invalid account number. Please try again.")


if __name__ == "__main__":
    main()
