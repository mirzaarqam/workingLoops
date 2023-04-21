import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from prettytable import PrettyTable

# create tkinter root window
root = tk.Tk()

# Hide tkinter root window
root.withdraw()

# Define the path to the data directory and the CSV file name
data_dir = os.path.join(os.path.expanduser("~"), "Desktop", "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
csv_file = os.path.join(data_dir, "students.csv")

# num_students = int(input("Enter the number of students: "))
num_students = simpledialog.askinteger(title="Students Count", prompt="Enter the Total Number of Students")

# Initialize an empty dictionary to store student data
student_data = {}

# Assign temporary roll numbers starting from 210423
roll_num = 210423

# Input each student's name, class, and store their data in the dictionary
for i in range(num_students):
    # name = input(f"Enter the name of student {i+1}
    name = simpledialog.askstring(title="Student Name", prompt=f"Enter the name of student {i + 1}: ")
    # class_name = input(f"Enter the class of student {i+1}: ")
    class_name = simpledialog.askstring(title="Class Name", prompt=f"Enter the name of Class {i + 1}: ")
    if class_name not in student_data:
        student_data[class_name] = []
    student_data[class_name].append({"name": name, "roll_num": roll_num})
    roll_num += 1


# Define a function to search for a student by name
def search_by_name():
    # name = input("Enter the name of the student to search: ")
    name = simpledialog.askstring(title="Search", prompt="Enter the name of the student to search: ")
    for class_name, students in student_data.items():
        for student in students:
            if student["name"] == name:
                # print(f"Roll no: {student['roll_num']}, Class: {class_name}")
                messagebox.showinfo(title="Result", message=f"Roll no: {student['roll_num']}, Class: {class_name}")
                return
    print("Student not found.")


# Define a function to search for a student by roll number
def search_by_roll_num():
    # roll_num = int(input("Enter the roll number of the student to search: "))
    roll_num = simpledialog.askinteger(title="Search", prompt="Enter the roll number of the student to search: ")
    for class_name, students in student_data.items():
        for student in students:
            if student["roll_num"] == roll_num:
                # print(f"Name: {student['name']}, Class: {class_name}")
                messagebox.showinfo(title="Result", message=f"Name: {student['name']}, Class: {class_name}")
                return
    print("Student not found.")


# Define a function to search for the number of students in a given class and print a table of students
def search_class_size():
    # class_name = input("Enter the name of the class to search: ")
    class_name = simpledialog.askstring(title="Class Name", prompt="Enter the name of the class to search: ")

    if class_name in student_data:
        students = student_data[class_name]
        table = PrettyTable()
        table.field_names = ["Name", "Roll No."]
        for student in students:
            table.add_row([student["name"], student["roll_num"]])
        print(f"Students in class {class_name}:")

        # Will show the table in Console
        print(table)

        # Will Show the table in GUI (Message Dialog box)
        messagebox.showinfo(title="Results", message=table)
    else:
        print("Class not found.")


# Define a function to save the student data to a CSV file
def save_data_to_csv():
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll No.", "Class"])
        for class_name, students in student_data.items():
            for student in students:
                writer.writerow([student["name"], student["roll_num"], class_name])
    print(f"Student data saved to {csv_file}")


# Main program loop
while True:
    # print("\nChoose a search method:")
    # print("1. Search by name")
    # print("2. Search by roll number")
    # print("3. Search class size")
    # print("4. Save data to CSV file")
    # print("5. Exit")
    # choice = input("Enter your choice: ")

    choice = simpledialog.askstring(title="Choices",
                                    prompt="\nChoose a search method: \n1. Search by name \n2. Search by roll number "
                                           "\n3. Search class size \n4. Save data to CSV file \n5. Exit ")

    if choice == "1":
        search_by_name()
    elif choice == "2":
        search_by_roll_num()
    elif choice == "3":
        search_class_size()
    elif choice == "4":
        save_data_to_csv()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
