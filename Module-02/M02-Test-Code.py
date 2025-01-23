DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
EXIT: str = 'ZZZ' 

lastName: str = ''
firstName: str = ''

lastName = input("'ZZZ' to quit\nEnter students' last name: ")
while lastName != EXIT:
    firstName = input("Enter students' first name: ")
    while True:
        try:
            gpa = input("Enter students' GPA: ")
            gpa = float(gpa)
            break
        except ValueError:
            print('Please enter float point numbers.') 
    if gpa >= DEANS_LIST:
        print(f"{firstName} {lastName} has made the Dean's List!")
        lastName = input("'ZZZ' to quit\nEnter students' last name: ")
    elif gpa >= HONOR_ROLL and gpa < DEANS_LIST:
        print(f"{firstName} {lastName} has made Honor Roll!")
        lastName = input("'ZZZ' to quit\nEnter students' last name: ")
    elif gpa < HONOR_ROLL:
        print(f"{firstName} {lastName} has not made Dean's List or Honor Roll.")
        lastName = input("'ZZZ' to quit\nEnter students' last name: ")
    else:
        break