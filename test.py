students=[]
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    students.append({
        "name": name,
        "age": age,
        "marks": marks
    })
    print("Student added!")

def view_students():
    if len(students) == 0:
       print("No students found")
    else:
        for s in students:
            print(s)	
    

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
import numpy as np

marks = np.array([45, 67, 89, 56, 90, 38, 72])

print("\n--- NUMPY ANALYSIS ---")
print("Marks:", marks)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

percentage = (np.sum(marks) / (len(marks) * 100)) * 100
print("Class Percentage:", percentage)

import pandas as pd

df = pd.read_csv("students.csv")

print("\n--- PANDAS ANALYSIS ---")

# View data
print(df)

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Top students
print("\nTop Performers:")
print(df[df["Marks"] > 75])

# Failed students
print("\nFailed Students:")
print(df[df["Marks"] < 40])

# Age-wise grouping
print("\nAge-wise average marks:")
print(df.groupby("Age")["Marks"].mean())



