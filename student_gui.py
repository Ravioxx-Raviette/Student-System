from tkinter import *
from functools import partial
from tkinter import messagebox
from tkinter import ttk

# Assuming the required imports for Student, SearchStudent, AddStudent, etc.
from Student import *
from SearchStudent import *
from print_all_students import *
from Main_menu import *
from AddStudent import *

win = Tk()
win.geometry("1280x800+{}+{}".format((win.winfo_screenwidth()-1280)//2, (win.winfo_screenheight()-800)//2))
win.title("Student Information System")
win.configure(bg="#1f2a44")

# Font settings
main_font = ("Poppins", 16)
title_font = ("Poppins", 20, "bold")
header_font = ("Poppins", 18, "bold")
button_font = ("Poppins", 16)
info_font = ("Poppins", 16)

# Button texts
button_texts = ["My Info", "Search Student", "Add Student", "View All Students", "Logout"]

# Assuming StudentInfo and Add_Student are properly defined elsewhere
student_info = StudentInfo()
add_student_form = Add_Student(student_info)
search_student = SearchStudent(student_info)
current_student = None
login_attempts = 0  # Counter for login attempts

def confirm_login():
    global current_student, login_attempts
    student_id = login_entry.get().strip()
    current_student = search_student.verify_login(student_id)
    
    if current_student:
        messagebox.showinfo("Login", f"Welcome {current_student[0]}!")
        login_frame.pack_forget()  # Hide login frame
        main_frame.pack(fill="both", expand=True)  # Show main frame
        display_my_info()
        login_attempts = 0  # Reset login attempts on successful login
    else:
        login_attempts += 1
        if login_attempts >= 4:
            messagebox.showerror("Login Failed", "You have reached the maximum number of login attempts.")
            login_entry.config(state="disabled")  # Disable the login entry field
            login_button.config(state="disabled")  # Disable the login button
        else:
            messagebox.showerror("Login Failed", f"Invalid Student ID. You have {4 - login_attempts} attempts remaining.")

def confirm_logout():
    global current_student, login_attempts
    current_student = None
    login_attempts = 0  # Reset login attempts on logout
    login_entry.delete(0, END)
    main_frame.pack_forget()  # Hide main frame
    login_frame.pack(fill="both", expand=True)  # Show login frame

def open_frame(frame_to_open, frames_to_close):
    for frame in frames_to_close:
        frame.pack_forget()
    frame_to_open.pack(side="right", fill="both", expand=True)

def display_my_info():
    if current_student:
        # Clear the previous info if any
        for widget in container[0].winfo_children():
            widget.destroy()
        
        # Title
        title_label = Label(container[0], text="My Information", font=title_font, bg="#2d3b5d", fg="white")
        title_label.pack(pady=10)
        
        # Display student information in a cleaner format
        info_frame = Frame(container[0], bg="#2d3b5d")
        info_frame.pack(pady=20, padx=20, fill="x")
        
        # Using a grid layout for better alignment
        Label(info_frame, text="Name:", font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=0, column=0, sticky="w", pady=8)
        Label(info_frame, text=current_student[0], font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=0, column=1, sticky="w", pady=8)

        Label(info_frame, text="Age:", font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=1, column=0, sticky="w", pady=8)
        Label(info_frame, text=current_student[1], font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=1, column=1, sticky="w", pady=8)

        Label(info_frame, text="ID:", font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=2, column=0, sticky="w", pady=8)
        Label(info_frame, text=current_student[2], font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=2, column=1, sticky="w", pady=8)

        Label(info_frame, text="Email:", font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=3, column=0, sticky="w", pady=8)
        Label(info_frame, text=current_student[3], font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=3, column=1, sticky="w", pady=8)

        Label(info_frame, text="Phone:", font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=4, column=0, sticky="w", pady=8)
        Label(info_frame, text=current_student[4], font=info_font, bg="#2d3b5d", fg="white", anchor="w").grid(row=4, column=1, sticky="w", pady=8)

        # Add spacing between the content
        Label(container[0], text="", bg="#2d3b5d").pack(pady=10)

    else:
        myinfo_label.config(text="No user is logged in.")

def search_for_student():
    def perform_search():
        student = search_student.verify_login(search_entry.get().strip())
        if student:
            search_result_label.config(text=f"Name: {student[0]}\nAge: {student[1]}\nID: {student[2]}\nEmail: {student[3]}\nPhone: {student[4]}")
        else:
            search_result_label.config(text="Student not found.")
    
    # Clear the previous widgets in container[1] (search container)
    for widget in container[1].winfo_children():
        widget.destroy()

    # Title for the search section (similar to 'My Information')
    title_label = Label(container[1], text="Search Student", font=title_font, bg="#2d3b5d", fg="white")
    title_label.pack(pady=10)

    # Search Entry and Button for searching
    search_frame = Frame(container[1], bg="#2d3b5d")
    search_frame.pack(pady=20, padx=20, fill="x")
    
    Label(search_frame, text="Enter Student ID:", font=main_font, bg="#2d3b5d", fg="white").pack(pady=15)
    search_entry = Entry(search_frame, font=main_font, width=30, bd=0, relief="flat", highlightthickness=2, highlightbackground="#4169e1", highlightcolor="#4169e1")
    search_entry.pack(pady=15)
    
    Button(search_frame, text="Search", font=button_font, bg="#4169e1", fg="white", bd=0, relief="flat", width=20, height=2, command=perform_search).pack(pady=15)
    
    # Label to display search result
    search_result_label = Label(container[1], text="", font=main_font, bg="#2d3b5d", fg="white", anchor="w")
    search_result_label.pack(pady=20)

# Set up initial frames for login
login_frame = Frame(win, bg="#2d3b5d", padx=20, pady=20)
login_frame.pack(fill="both", expand=True)

login_form = Frame(login_frame, bg="#2d3b5d", padx=40, pady=40)
login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Login", font=title_font, bg="#2d3b5d", fg="white").pack(pady=20)
Label(login_form, text="Enter Student ID:", font=main_font, bg="#2d3b5d", fg="white").pack(pady=15)
login_entry = Entry(login_form, font=main_font, bd=0, relief="flat", highlightthickness=2, highlightbackground="#4169e1", highlightcolor="#4169e1")
login_entry.pack(pady=15)

login_button = Button(login_form, text="Login", bg="#4169e1", font=button_font, fg="white", bd=0, relief="flat", width=20, height=2, command=confirm_login)
login_button.pack(pady=15)

Button(login_form, text="Exit", bg="#4169e1", font=button_font, fg="white", bd=0, relief="flat", width=20, height=2, command=win.destroy).pack(pady=15)

# Main frame for after login
main_frame = Frame(win, bg="#1f2a44", padx=20, pady=20)
container = [Frame(main_frame, bg="#2d3b5d", padx=20, pady=20) for _ in button_texts]
[frame.pack_forget() for frame in container]  # Initially hide all containers

myinfo_label = Label(container[0], text="", font=main_font, bg="#2d3b5d", fg="white")
myinfo_label.pack(pady=30)

button_functions = [
    partial(open_frame, container[0], container[1:]), 
    partial(open_frame, container[1], container[:1] + container[2:]), 
    partial(open_frame, container[2], container[:2] + container[3:]), 
    partial(open_frame, container[3], container[:3] + container[4:]), 
    confirm_logout
]

menu_container = Frame(main_frame, bg="#1f2a44", padx=20, pady=20)
menu_container.pack(side="left", fill="y")

for i in range(len(button_texts)):
    Button(menu_container, text=button_texts[i], bg="#4169e1", font=button_font, fg="white", bd=0, relief="flat", width=20, height=2, command=button_functions[i]).pack(pady=15)

add_student_form.show_registration_ui(container[2])



def display_all_students():
    # Clear container[3] and prepare to display students
    for widget in container[3].winfo_children():
        widget.destroy()

    # Create a Frame to hold the Treeview
    display_frame = Frame(container[3], bg="#2d3b5d")
    display_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Create Treeview widget for displaying student data
    treeview = ttk.Treeview(display_frame, columns=("Name", "Age", "ID", "Email", "Phone"), show="headings", selectmode="browse")

    # Define the column headers and widths
    treeview.heading("Name", text="Name")
    treeview.heading("Age", text="Age")
    treeview.heading("ID", text="ID")
    treeview.heading("Email", text="Email")
    treeview.heading("Phone", text="Phone")

    # Set column properties: Widths and Alignment
    treeview.column("Name", width=200, anchor="w")
    treeview.column("Age", width=50, anchor="center")
    treeview.column("ID", width=100, anchor="center")
    treeview.column("Email", width=250, anchor="w")
    treeview.column("Phone", width=150, anchor="w")

    # Apply font style for the content of Treeview
    treeview.tag_configure("oddrow", background="#3a4e73", foreground="white", font=("Poppins", 12))
    treeview.tag_configure("evenrow", background="#2d3b5d", foreground="white", font=("Poppins", 12))

    # Insert data into the Treeview (student data)
    for index, student in enumerate(student_info.allstudents):
        # Alternate row colors
        if index % 2 == 0:
            treeview.insert("", "end", values=student, tags=("evenrow",))
        else:
            treeview.insert("", "end", values=student, tags=("oddrow",))

    # Add a scrollbar to Treeview if needed (optional)
    scrollbar = Scrollbar(display_frame, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    # Pack the treeview to the frame
    treeview.pack(fill="both", expand=True)

    # Add Refresh Button
    refresh_button = Button(container[3], text="Refresh", font=button_font, bg="#4169e1", fg="white", bd=0, relief="flat", width=20, height=2, command=display_all_students)
    refresh_button.pack(pady=15)




display_all_students()
search_for_student()

win.mainloop()
