"""
Description: 
For UO's CS 422 Project 1. A graphical user interface to interact with the data
in the EasyA project. Allows input from students, system admins, and displays 
data in bar graph form.
"""

import tkinter as tk
from tkinter import ttk

#--------------GOALS-------------
# Design admin layout
# Implement admin layout for data updating
# Change so multiple windows are opened, change main window after user selection

class GUI:
    # Initialize the landing page
    def __init__(self):
        self.root = tk.Tk()             
        self.root.title("EasyA")

        # Natural Science department options
        self.classes = ["Data Science", "Earth Sciences", "Human Physiology", "Neuroscience", "Psychology",
                        "Multidisciplinary Science", "Mathematics", "Physics", "Biology", "Computer Science", 
                        "Chemistry and Biochemistry"]
        
        # Course level options
        self.course_levels = ["All 100-Level", "All 200-Level", "All 300-Level", "All 400-Level", "All 500-Level", "All 600-Level"]

        # Graph mode radio button variable
        self.mode = tk.IntVar()

        # Itroduction header of landing page
        self.headlabel1 = tk.Label(self.root, text="Hello! And Weclome To The EasyA Program", font=('Arial', 20))
        self.headlabel1.pack(padx=10, pady=10)

        # Itroduction header of landing page
        self.headlabel2 = tk.Label(self.root, text="Please Select Whether You Are A:", font=('Arial', 18))
        self.headlabel2.pack(padx=10, pady=10)

        # Button to select the student user and open student user page
        self.stuBtn = tk.Button(self.root, text="Student", font=('Arial', 18), command=self.studentPage)
        self.stuBtn.pack(padx=10, pady=10)

        # Button to select the system admin and open system admin page
        self.sysABtn = tk.Button(self.root, text="System Admin", font=('Arial', 18), command=self.adminPage)
        self.sysABtn.pack(padx=10, pady=10)

        # GUI main loop
        self.root.mainloop()

    # Function containing student page
    def studentPage(self):
        # Student Page
        UserPage = tk.Toplevel()
        UserPage.title("EasyA/Student")

        #-----------------Program Use Description Frame---------------------

        # Frame containing the instructions for how to use the program
        user_info_frame = tk.LabelFrame(UserPage, text="User Instructions", font=('Arial', 16))
        user_info_frame.grid(row=0, column=0, padx=10, pady=10)

        # Selecting courses and department instructions
        select_instructions = tk.Label(user_info_frame, text='- Use the department and course level dropdown menus to view all the classes under that level or enter an exact course number in the "Specific Course Level" box', font=('Arial', 12))
        select_instructions.pack()

        # Selecting faculty type instructions
        instructor_instructions = tk.Label(user_info_frame, text='- Select the "Just Regular Faculty" checkbox to refine your graph data from all instructors (which includes graduate student instructors) to just the regular faculty', font=('Arial', 12))
        instructor_instructions.pack()

        # Toggling Mode Instructions
        mode_instructions = tk.Label(user_info_frame, text='- Use the radio buttons to toggle between the "EasyA" mode which generates graphs of the instructors A percentages', font=('Arial', 12))
        mode_instructions.pack()

        mode_instructions2 = tk.Label(user_info_frame, text='and "Just Pass" mode which generates graphs of instructors D and F percentages', font=('Arial', 12))
        mode_instructions2.pack()

        #-----------------Course Selection Info Frame---------------------

        #Frame containing the info for course selection
        course_info_frame = tk.LabelFrame(UserPage, text="Course Selection", font=('Arial', 16))
        course_info_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        #Department 
        dept_label = tk.Label(course_info_frame, text="Deptartment", font=('Arial', 20))
        dept_label.grid(row=0, column=0)

        #Dropdown menu for department selection including all natural science departments
        dept_dropdown = ttk.Combobox(course_info_frame, values=self.classes)
        dept_dropdown.grid(row=1, column=0)

        #Course Level
        course_level_label = tk.Label(course_info_frame, text="Course Level", font=('Arial', 20))
        course_level_label.grid(row=0, column=1)

        #Dropdown menu for course level selection from 100 to 600
        course_level_dropdown = ttk.Combobox(course_info_frame, values=self.course_levels)
        course_level_dropdown.grid(row=1, column=1)

        #Specific Course Level
        spec_course_level_label = tk.Label(course_info_frame, text="Specific Course Level", font=('Arial', 20))
        spec_course_level_label.grid(row=0, column=2)

        #Text entry box that allows a user to search for a specific course level (111, 112, ...)
        spec_course_level_entry = ttk.Entry(course_info_frame)
        spec_course_level_entry.grid(row=1, column=2)

        #Give all widgets in from that same padding
        for widget in course_info_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

        #-----------------Graph Filter Frame---------------------

        # Frame containing all options to refine graph data
        graph_filter_frame = tk.LabelFrame(UserPage, text="Graph Data Filter", font=('Arial', 16))
        graph_filter_frame.grid(row=2, column=0, sticky="news", padx=10, pady=10)

        # Instructor selection label
        instructor_label = tk.Label(graph_filter_frame, text="Instructors (All by Default)", font=('Arial', 20))
        instructor_label.grid(row=0, column=0)

        # Instructor selection checkbox
        instructor_checkbox = tk.Checkbutton(graph_filter_frame, text="Just Regular Faculty", font=('Arial', 12))
        instructor_checkbox.grid(row=1, column=0)

        # Graph mode label
        graph_mode_label = tk.Label(graph_filter_frame, text="Graph Mode", font=('Arial', 20))
        graph_mode_label.grid(row=0, column=1)

        # Radio buttons that toggle between graph data modes
        # EasyA mode radio button
        easyA_radio_btn = tk.Radiobutton(graph_filter_frame, text="EasyA - Only A's", font=('Arial', 12), variable=self.mode, value=1)
        easyA_radio_btn.grid(row=1, column=1)

        # Just Pass mode radio button
        justPass_radio_btn = tk.Radiobutton(graph_filter_frame, text="Just Pass - D's and F's", font=('Arial', 12), variable=self.mode, value=2)
        justPass_radio_btn.grid(row=2, column=1)

        # Generate Graph Label
        generate_label = tk.Label(graph_filter_frame, text="Generate Graph", font=('Arial', 20))
        generate_label.grid(row=0, column=2)

        # Generate Graph Button
        generate_label_btn = tk.Button(graph_filter_frame, text="Generate", font=('Arial', 16))
        generate_label_btn.grid(row=1, column=2)

        #Give all widgets in from that same padding
        for widget in graph_filter_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

    #Function contaning system admin page
    def adminPage(self):
        
        SysAdminPage = tk.Toplevel()
        SysAdminPage.title("EasyA/System Admin")
        SysAdminPage.geometry("400x400")
        
        headlabel1 = tk.Label(SysAdminPage, text="System Admin Page", font=('Arial', 25))
        headlabel1.pack(padx=10, pady=10)

GUI()
