a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Choose the swapping method: \n 1.exchange method\n 2.add method\n 3.subtraction method\n 4.multiplication method\n 5.division method\n")
method=int(input())
print("After swapping the numbers the a and b values are: ")

#method-1
# c=a
# print("a: ",b)
# b=a
# print("b: ",b)

# method-2
# c=a+b
# a=c-a
# b=c-b
# print("a: ",a)
# print("b: ",b)

# method-3
# c=a-b
# a=b
# b=c+a
# print("a: ",a)
# print("b: ",b)

# method-4
# c=a*b
# a=c/b
# b=c/a
# print("a: ",a)
# print("b: ",b)

# method-5
# c=a/b
# a=b
# b=c*a
# print("a: ",a)
# print("b: ",b)

def swap():
    global a, b

    if method==1:
        c=a
        print("a: ",b)
        b=a
        print("b: ",b)
    elif method==2:
        c=a+b
        a=c-a
        b=c-b
        print("a: ",a)
        print("b: ",b)
    elif method==3:
        c=a-b
        a=b
        b=c+a
        print("a: ",a)
        print("b: ",b)
    elif method==4:
        c=a*b
        a=c/b
        b=c/a
        print("a: ",a)
        print("b: ",b)
    elif method==5:
        c=a/b
        a=b
        b=c*a
        print("a: ",int(a))
        print("b: ",int(b))
    else:
        print("Invalid method selected!")    
swap()