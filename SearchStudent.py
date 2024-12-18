class SearchStudent:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, keyword):
        # Search for a student by ID number
        for student in self.student_data.allstudents:
            if student[2] == keyword:
                return student  # Found the student, return their data

        return None  # Return None if no student is found

    def display_student_info(self, student):
        # Format student details to display in the UI
        name, age, idnum, email, phone = student
        return f"Name: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}"

    def print_student_info(self, student):
        # Print the details of a found student
        name, age, idnum, email, phone = student
        filler = '=' * 23
        print(f'\nStudent Info Found:\n{"=" * 20} Student\'s Information {"=" * 20}')
        print(f'\nName: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}\n')

    def verify_login(self, idnum):
        # Verify if the ID number exists in the student data
        for student in self.student_data.allstudents:
            if student[2] == idnum:
                return student  # Return the entire student record
        return None  # Return None if no match found


class SearchStudentUI:
    def __init__(self, student_data, parent_frame):
        self.student_data = student_data  # StudentInfo instance
        self.parent_frame = parent_frame  # The frame where the UI will be placed

        # Call the method to create the search UI
        self.create_search_ui()

    def create_search_ui(self):
        # Label for the search UI
        label = Label(self.parent_frame, text="Enter Student ID to Search", font=("arial", 16), pady=15)
        label.pack()

        # Entry field for student ID
        self.entry_id = Entry(self.parent_frame, font=("arial", 14), width=25, relief="solid", bd=2)
        self.entry_id.pack(pady=10)

        # Button to trigger search
        search_button = Button(self.parent_frame, text="Search", font=("arial", 14), command=self.search_student)
        search_button.pack(pady=10)

        # Label to display search results
        self.result_label = Label(self.parent_frame, text="", font=("arial", 12), justify=LEFT)
        self.result_label.pack(pady=10)

    def search_student(self):
        student_id = self.entry_id.get()

        # Search for the student in the data
        student = self.student_data.search_student(student_id)

        if student:
            # Display student info if found
            student_info = self.student_data.display_student_info(student)
            self.result_label.config(text=student_info)
        else:
            # If not found
            self.result_label.config(text="Student not found. Please check the ID and try again.")
