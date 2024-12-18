from tkinter import *

class Add_Student:
    def __init__(self, student_info):
        """
        Initializes Add_Student class with access to student_info data storage.
        """
        self.student_info = student_info
        self.read_from_file()  # Load existing students from file

    def add_student(self, name, age, idnum, email, phone):
        """
        Adds a new student, updates in-memory list, and appends to file.
        """
        # Validate data types before proceeding
        if not age.isdigit():
            self.lblerrors.config(text="Age must be a valid number.", fg="red")
            return

        # Set data to the student_info object
        self.student_info.setName(name)
        self.student_info.setAge(age)
        self.student_info.setIDNum(idnum)
        self.student_info.setEmail(email)
        self.student_info.setPhoneNum(phone)

        # Append student info to the in-memory list
        student_data = [name, age, idnum, email, phone]
        self.student_info.allstudents.append(student_data)

        # Save the new student to the file
        self.write_to_file(student_data)
        self.lblerrors.config(text="Student added successfully!", fg="green")

    def write_to_file(self, student):
        """
        Appends a student's information to the file.
        """
        with open("student_data.txt", "a") as file:
            file.write(', '.join(student) + '\n')

    def read_from_file(self):
        """
        Reads all students from file and loads into in-memory list.
        """
        try:
            with open("student_data.txt", "r") as file:
                for line in file:
                    student = line.strip().split(", ")
                    if len(student) == 5:
                        self.student_info.allstudents.append(student)
        except FileNotFoundError:
            print("No existing student data found. Initializing empty data.")

    def show_registration_ui(self, reg_frame):
        """
        Creates the 'Add Student' registration UI dynamically with a modern aesthetic.
        """
        # Error message label
        self.lblerrors = Label(reg_frame, text="", font=("Poppins", 16), fg="red", bg="#2d3b5d")
        self.lblerrors.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        # Title for Add Student Form (similar to 'My Information' and 'Search Student')
        title_label = Label(reg_frame, text="Add Student", font=("Poppins", 16), fg="white", bg="#2d3b5d")
        title_label.grid(row=0, column=0, columnspan=2, pady=15, padx=20, sticky="ew")

        # Form labels and entry fields
        labels = ["Name", "Age", "ID Number", "Email", "Phone"]
        self.entries = []  # Store Entry widgets for later access

        # Create form dynamically with flat, rounded entry style
        for i, label in enumerate(labels):
            # Label for each field
            Label(reg_frame, text=label, font=("Poppins", 16), fg="white", bg="#2d3b5d", anchor="w").grid(
                row=i + 2, column=0, padx=20, pady=10, sticky="w"
            )

            # Entry field with consistent styling
            entry = Entry(reg_frame, font=("Poppins", 16), width=30, bd=0, relief="flat", highlightthickness=2,
                          highlightbackground="#4169e1", highlightcolor="#4169e1")
            entry.grid(row=i + 2, column=1, padx=20, pady=10, sticky="ew")
            self.entries.append(entry)

        # Submit button with consistent styling
        submit_button = Button(
            reg_frame, text="Add Student", font=("Poppins", 16), bg="#4169e1",
            fg="white", width=20, height=2, relief="flat", command=self.submit_form
        )
        submit_button.grid(row=len(labels) + 3, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

        # Centering the frame's content
        reg_frame.grid_rowconfigure(0, weight=0)
        reg_frame.grid_rowconfigure(1, weight=0)
        reg_frame.grid_rowconfigure(len(labels) + 3, weight=0)
        reg_frame.grid_columnconfigure(0, weight=1)
        reg_frame.grid_columnconfigure(1, weight=1)

    def submit_form(self):
        """
        Handles the form submission for adding a new student.
        """
        # Extract data from entry fields
        name = self.entries[0].get().strip()
        age = self.entries[1].get().strip()
        idnum = self.entries[2].get().strip()
        email = self.entries[3].get().strip()
        phone = self.entries[4].get().strip()

        # Input validation
        if not all([name, age, idnum, email, phone]):
            self.lblerrors.config(text="Please fill in all fields.", fg="red")
        else:
            # Add student
            self.add_student(name, age, idnum, email, phone)

            # Clear input fields after success
            for entry in self.entries:
                entry.delete(0, END)