from Student import *
from SearchStudent import *
from print_all_students import *
from Main_menu import *
from AddStudent import *

# Create an instance of the StudentInfo class to manage student data
STU = StudentInfo()

# Instantiate classes for adding, searching, and printing student information
add_students = Add_Student(STU)
search_student = SearchStudent(STU)
print_all =  PrintAllStudent(STU)


# Create a main menu instance with the student operations
menu = MainMenu(add_students, search_student, print_all)

# This Used to add students to the system  (Is here so i no forgor)
'''add_students.add_student("Cheilou", "19", "2023-2-00487", "2023-2-00487@lpunetwork.edu.ph", "097234321"),
add_students.add_student("Frank", "19", "2023-2-00837", "2023-2-00837@lpunetwork.edu.ph", "09867543"),
add_students.add_student("Aundreka", "20", "2023-2-01597", "2023-2-01597@lpunetwork.edu.ph", "09347842"),
add_students.add_student("Mira", "20", "2023-2-01660", "2023-2-01660@lpunetwork.edu.ph", "09245382"),
add_students.add_student("Zenia", "20", "2023-2-00203", "2023-2-00203@lpunetwork.edu.ph", "09345456"),
add_students.add_student("Marjinel", "19", "2023-2-00412", "2023-2-00412@lpunetwork.edu.ph", "09565098"),
add_students.add_student("Andrew", "20", "2023-2-00892", "2023-2-00892@lpunetwork.edu.ph", "09345342"),
add_students.add_student("Issa", "20", "2023-2-00677", "2023-2-00677@lpunetwork.edu.ph", "09639328"),
add_students.add_student("Rebekah", "19", "2023-2-00460", "2023-2-00460@lpunetwork.edu.ph", "09345328")'''



max_attempts = 4
attempts = 0

# Simulating login attempts with a maximum of 4 tries
while attempts < max_attempts:
    print('=' * 10, "Login - Student Info System", '=' * 10)
    login_check = input('Student ID: ')  # Prompt user for their Student ID
    
    user = search_student.verify_login(login_check)  # Verify if the student ID exists
    
    if user:
        # Access the main menu for the logged-in user
        menu.Main_menu(user)  
        break  # Exit the loop upon successful login
    else:
        print("\n" * 20)  # Simulate clearing the console
        attempts += 1  # Increment the attempts counter
        print(f'The student with ID number {login_check} does not exist.\nAttempts left: {max_attempts - attempts}')
    
    if attempts >= max_attempts:  # If max attempts are reached
        print("\n" * 20)  # Simulate clearing the console again
        print('You have exceeded the maximum login attempts. Goodbye!')  # Inform the user and exit
