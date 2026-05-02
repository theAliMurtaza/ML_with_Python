students = {}
def add_students():
    name = input("Enter student name: ")
    marks = list(map(int , input("Enter the marks (space Separated):").split))
    students[name] = marks
    print("Student added successfully.")
def view_students():
    if not students:
        print("No Student available")
        return
    for name , marks in students.items():
        print(f"Name: {name}, Marks: {marks}")
def search_student():
    name =input("Enter the Student name to search: ")
    if name in students:
        print(f"Name: {name}, Marks: {students[name]}")
    else:
        print(f"Student '{name}' not found.")
def calculate_average():
    if not students:
        print("No Student available")
        return
    for name , marks in students.items():
        average = sum(marks) / len(marks)
        print(f"Name: {name}, Average Marks: {average:.2f}")
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()