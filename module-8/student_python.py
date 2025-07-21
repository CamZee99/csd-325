import json

with open("student.json", "r") as file:
    students = json.load(file)

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

print("Original Student List:")
print_students(students)

new_student = {
    "F_Name": "Cameron",
    "L_Name": "Zimmer",
    "Student_ID": 21503772,
    "Email": "czimmer@my365.bellevue.edu"
}
students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nstudent.json has been updated.")

# Opens the student.json file and loads its data into a Python list of dictionaries.
# Informs the user that the original list of students is about to be displayed.
# Iterates through each student in the list and prints their last name, first name, student ID, and email.
# Adds new student to the list.
# Informs the user that the student list has been updated and displays it.

