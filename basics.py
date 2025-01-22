name=str(input("Enter your name:"))
pin=int(input("Enter your pin:"))
initial_balance=float(input("Enter your initial balance:"))

desposit=float(input("Enter the amount you want to deposit:"))
initial_balance+=desposit
print("Your balance is:",initial_balance)

withdraw=float(input("Enter the amount you want to withdraw:"))
initial_balance-=withdraw
print("Your balance is:",initial_balance)