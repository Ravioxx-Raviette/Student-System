class PrintAllStudent:
    def __init__(self, student):
        # Initialize the class with a student data object
        self.student_data = student

    def print_all_students(self):
        # Method to print all students' information
        header = '=' * 15 + " All Students' Information " + '=' * 15
        print(header)  # Header for the student information section

        # Check if there are any students to display
        if not self.student_data.allstudents:
            print("No students found.")  
        else:
            # Iterate over all students in the student data
            for student in self.student_data.allstudents:
                self._print_student_info(student)  # Call a helper method to print each student's details

        footer = '=' * 20 + " Nothing Follows " + '=' * 20  
        print(footer)
        # Prompt the user to go back to the previous menu
        input('\nPress Enter to go back.')

    def _print_student_info(self, student):
        # Helper method to print individual student information
        name, age, idnum, email, phone = student  # Unpack student information
        print(f'\nName: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}\n')
