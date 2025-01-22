lastName: str = input("'ZZZ' to quit\nEnter students' last name: ")
while lastName != 'ZZZ':
    firstName: str = input("Enter students' first name: ")
    gpa: float = float(input("Enter students' GPA: "))
    if gpa >= 3.5:
        print(f"{firstName} {lastName} has made the Dean's List!")
        lastName: str = input("'ZZZ' to quit\nEnter students' last name: ")
    elif gpa >= 3.25 and gpa <= 3.49:
        print(f"{firstName} {lastName} has made Honor Roll!")
        lastName: str = input("'ZZZ' to quit\nEnter students' last name: ")
    elif gpa < 3.25:
        print(f"{firstName} {lastName} has not made Dean's List or Honor Roll.")
        lastName: str = input("'ZZZ' to quit\nEnter students' last name: ")
    else:
        break