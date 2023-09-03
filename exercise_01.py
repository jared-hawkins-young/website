grade = input('Enter your grade from 0 to 100: ')

grade = int(grade)

if grade < 59:
    print("Your grade is F")

elif grade < 69:
    print("Your grade is D")

elif grade < 79:
    print("Your grade is C")

elif grade < 89:
    print("Your grade is B")

elif grade < 100:
    print("Your grade is A")
    