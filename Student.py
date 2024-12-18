class StudentInfo:
    def __init__(self):
        # Initialize student attributes and a list to hold all students
        self.name = ''
        self.age = ''
        self.idnum = ''
        self.email = ''
        self.phone = ''
        self.allstudents = []  # List to store all student information
       
    
    def setName(self, name):
        # Set the student's name
        self.name = name
    
    def setAge(self, age):
        # Set the student's age
        self.age = age
        
    def setIDNum(self, idnum):
        # Set the student's ID number
        self.idnum = idnum
        
    def setEmail(self, email):
        # Set the student's email address
        self.email = email
        
    def setPhoneNum(self, phone):
        # Set the student's phone number
        self.phone = phone

    @property
    def getName(self):
        # Return the student's name
        return self.name

    @property
    def getAge(self):
        # Return the student's age
        return self.age

    @property
    def getIDNum(self):
        # Return the student's ID number    
        return self.idnum

    @property
    def getEmail(self):
        # Return the student's email address
        return self.email

    @property
    def getPhoneNum(self):
        # Return the student's phone number
        return self.phone

    def __str__(self):
        # Return a formatted string representation of the student's information
        return (f'\nName: {self.name}\n'
                f'Age: {self.age}\n'
                f'ID Number: {self.idnum}\n'
                f'Email Address: {self.email}\n'
                f'Phone Number: {self.phone}\n')

    