"""
GradeBook Analyzer - Assignment 2
Name: <YOUR NAME>
Date: <DATE>
Course: Programming for Problem Solving Using Python
"""

import csv

# ------------------ Task 1: Welcome & Menu ------------------

def print_menu():
    print("\n========== GradeBook Analyzer ==========")
    print("1. Enter student marks manually")
    print("2. Load marks from CSV file")
    print("3. Exit")
    print("========================================")


print("Welcome to the GradeBook Analyzer!")
print_menu()


# ------------------ Task 2: Data Input Methods ------------------

def manual_input():
    marks = {}
    n = int(input("How many students? "))

    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score

    return marks


def load_from_csv():
    marks = {}
    file = input("Enter CSV file name (example: data.csv): ")

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                name = row[0]
                score = float(row[1])
                marks[name] = score
        print("CSV loaded successfully.")
    except:
        print("Error reading CSV file!")

    return marks


# ------------------ Task 3: Statistical Functions ------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    mid = n // 2
    return values[mid] if n % 2 != 0 else (values[mid - 1] + values[mid]) / 2

def find_max_score(marks_dict):
    student = max(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]

def find_min_score(marks_dict):
    student = min(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]


# ------------------ Task 4: Grade Assignment ------------------

def assign_grades(marks_dict):
    grades = {}

    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        grades[name] = grade

    return grades


def count_grade_distribution(grades):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades.values():
        dist[g] += 1
    return dist


# ------------------ Task 5: Pass / Fail using List Comprehension ------------------

def pass_fail_list(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed


# ------------------ Task 6: Table Output & Loop ------------------

def print_table(marks, grades):
    print("\nName\tMarks\tGrade")
    print("-----------------------------------------")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")


# ------------------ Main Loop ------------------

while True:
    choice = input("\nChoose an option (1/2/3): ")

    if choice == "1":
        marks = manual_input()

    elif choice == "2":
        marks = load_from_csv()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
        continue

    # Statistics
    print("\n--- Statistical Analysis ---")
    print(f"Average: {calculate_average(marks):.2f}")
    print(f"Median: {calculate_median(marks):.2f}")
    max_name, max_score = find_max_score(marks)
    print(f"Highest Score: {max_name} ({max_score})")
    min_name, min_score = find_min_score(marks)
    print(f"Lowest Score: {min_name} ({min_score})")

    # Grades
    grades = assign_grades(marks)
    dist = count_grade_distribution(grades)

    print("\n--- Grade Distribution ---")
    for g, count in dist.items():
        print(f"{g}: {count}")

    # Pass / Fail
    passed, failed = pass_fail_list(marks)
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    # Table
    print_table(marks, grades)

    # Loop
    again = input("\nDo you want to run again? (y/n): ")
    if again.lower() != "y":
        print("Exiting program...")
        break