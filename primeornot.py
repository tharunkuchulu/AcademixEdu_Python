n=int(input("Enter the number you want to check: "))
#method-1
# def prime():
#     for i in range(2,n+1//2):
#         if n%i==0:
#             print(f"{n} is not prime")
#             break
#     else:
#         print(f"{n} is a prime")

# method-2
m=0
def prime():
    global m
    for i in range(2,n+1//2):
        if n%i==0:
            m=m+1
            break
    if m==0:
        print(f"{n} is a prime")
    else:
        print(f"{n} is not a prime and had {m} factors")

prime()
