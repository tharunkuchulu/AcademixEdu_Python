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

def result_status(total):
    if total >= 250:
        return "Pass"
    else:
        return "Fail"

def subject_grade(marks):
    if marks > 100:
        return "Invalid Input"
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def percentage(total):
    return (total / 500) * 100

def results(name, id, total, percent, grade, 
            maths, physics, chemistry, biology, english, status):
    print(f"\nStudent Name: {name}")
    print(f"Student ID: {id}")
    print("\nIndividual Subject Grades:")
    print(f"Maths: {maths} - {subject_grade(maths)}")
    print(f"Physics: {physics} - {subject_grade(physics)}")
    print(f"Chemistry: {chemistry} - {subject_grade(chemistry)}")
    print(f"Biology: {biology} - {subject_grade(biology)}")
    print(f"English: {english} - {subject_grade(english)}")
    print(f"\nTotal Marks: {total}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Overall Grade: {grade}")
    print(f"Assessment Status: {status}")
    
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
    status = result_status(total)

    results(name, id, total, percent, grade, maths, physics, chemistry, biology, english, status)

main()
