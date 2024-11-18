print("Welcome to simple calculator")
a=float(input("enter the first number from numbers you want to operate: "))
b=float(input("enter the second number from numbers you want to operate: "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

choice=int(input("Enter your choice: "))

if choice==1:   
    print(a,"+",b,"=",a+b)
elif choice==2:
    print(a,"-",b,"=",a-b)
elif choice==3:
    print(a,"*",b,"=",a*b)
elif choice==4:
    print(a,"/",b,"=",a/b)
else:
    print("Invalid input")