from student import Student, StudentManagement

print('Welcome to student management system')
student_management = StudentManagement()

while True:
    print("1. Add Student")
    print("2. Print All Students")
    print("3. Exit")
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        student_management.add_student()
    elif choice == '2':
        student_management.print_students()
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
