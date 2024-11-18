n=int(input("Enter the number of hours (12 or 24): "))
if n==12:
    for H in range(12):
        for M in range(60):
            for S in range(60):
                print(f"{H:02}:{M:02}:{S:02}")
elif n==24:
    for H in range(24):
        for M in range(60):
            for S in range(60):
                print(f"{H:02}:{M:02}:{S:02}")
else:
    print("Invalid input")