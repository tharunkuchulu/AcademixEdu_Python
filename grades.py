print("Welcome to the Grade Calculator")

def total_grade(total):
    if total > 500:
        return "Invalid Input"
    if total > 450:
        return "A+"
    if total >= 400:
        return "A"
    elif total >= 350:
        return "B"
    elif total >= 300:
        return "C"
    elif total >= 250:
        return "D"
    else:
        return "F"

def percentage(total):
    return (total / 500) * 100

def results(name, id, total, percent, grade):
    print(f"\nStudent Name: {name}")
    print(f"Student ID: {id}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Grade: {grade}")

def main():    
    name = input("Enter your name: ")
    id = input("Enter your ID: ")
    print("Enter your marks: ")
    maths = float(input("Maths: "))
    physics = float(input("Physics: "))
    chemistry = float(input("Chemistry: "))
    biology = float(input("Biology: "))
    english = float(input("English: "))

    total = maths + physics + chemistry + biology + english

    percent = percentage(total)
    grade = total_grade(total)

    results(name, id, total, percent, grade)

main()