class MainMenu:
    def __init__(self, add_student, search_student, print_all_student):
        # Initialize the main menu with instances of the add, search, and print functionalities
        self.add_students = add_student
        self.search = search_student
        self.print_all = print_all_student

    def add_student_option(self):
        # Method for adding student information
        while True:
            # Simulate clear by printing new lines
            print("\n")
            print('=====' , 'Add Student Information', '=====' )
            self.add_students.input_add_student()  # Call the method to handle input for new students
            rep = input('Do you want to add another student? (yes/no): ')
            # Check if the user wants to continue adding students
            if rep.lower() != 'yes':
                break

    def search_student_option(self):
        # Method for searching student information
        while True:
            # Simulate clear by printing new lines
            print("\n")
            print('=====' , 'Search Student Information', '=====' )
            required = input('\n\nEnter ID Number: ')  # Get the ID number to search
            print(self.search.search_student(required))  # Call search method and print the result
            rep = input('Do you want to search again? (yes/no): ')
            # Check if the user wants to continue searching
            if rep.lower() != 'yes':
                break

    def Main_menu(self, student):
        # Main menu display and option handling
        while True:
            # Simulate clear by printing new lines
            print("\n")
            print(f'Welcome, {student[0]}!\n', '=====', 'Main Menu', '=====')
            print("1. View your information")
            print("2. View other students' information")
            print("3. Register a new student")
            print("4. Print all students")
            print("5. Exit")
            choice = input('Your choice: ')  # Get the user's menu choice

            if choice == '1':
                # Option to view the current user's information
                print("\n")
                print('=====' , 'Your Information', '=====' )
                print(self.search.search_student(student[2]))  # Search for the current user's info using their ID
                input('Press Enter to go back to the main menu.')
            
            elif choice == '2':
                # Option to search for other students
                self.search_student_option()
            
            elif choice == '3':
                # Option to register a new student
                self.add_student_option()
            
            elif choice == '4':
                # Option to print all students' information
                print("\n")
                print('=====' , 'All Students', '=====' )
                self.print_all.print_all_students()  # Call the method to print all student information
                input('Press Enter to go back to the main menu.')
            
            elif choice == '5':
                # Option to exit the program
                print("\n")
                print('=====' , 'Why leave?...', '=====' , '\nokay...i guess.')
                break  # Exit the loop and end the program
            
            else:
                # Handle invalid input
                print("\nInvalid choice, please choose a valid option.")
                input('Press Enter to try again.')
