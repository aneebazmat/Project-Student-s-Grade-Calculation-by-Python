
# Lab Final ICT
# Problem 2 Solve by Python

# Program to process results of 5 students

for i in range(1, 6):                               # Use Loop to process result of 5 students
    print(f"\nEnter details for Student {i}")
    name = input("Enter name : ")
    
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    total = mark1 + mark2 + mark3
    average = total / 3

    # Determine grade of Students 

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Display result
    print("--- Result ---")
    print("Name    :", name)
    print("Total   :", total)
    print("Average :", format(average, ".2f"))
    print("Grade   :", grade)

print()
print("================== Thanks ========================")

