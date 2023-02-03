"""
Description: 
For UO's CS 422 Project 1. A graphical user interface to interact with the data
in the EasyA project. Allows input from students, system admins, and displays 
data in bar graph form.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class GUI:
    # Initialize the landing page
    def __init__(self):
        self.root = tk.Tk()             
        self.root.title("EasyA")

        # New data file
        self.fp = None

        # Natural Science department options
        self.department = ["Anthropology", "Biology", "Chemistry and Biochemistry", "Computer Science", "Data Science", 
                        "Earth Sciences", "Geography", "Human Physiology", "Mathematics", "Neuroscience", "Physics", "Psychology"]
        # Department codes
        self.dept_code = ["ANTH", "BI", "CH", "CIS", "DSC", "GEOL", "GEOG", "HPHY", "MATH", "NEUR", "PHYS", "PSY"]

        # Course level options
        self.course_levels = ["All 100-Level", "All 200-Level", "All 300-Level", "All 400-Level", "All 500-Level", "All 600-Level"]
        self.specific_course = tk.StringVar()

        # Department and course level variables
        self.select_dept = tk.StringVar()
        self.select_level = tk.StringVar()
        
        # Graph mode radio button variable
        self.mode = tk.IntVar()
        self.fac_type = tk.IntVar()

        # Itroduction header of landing page
        self.headlabel1 = tk.Label(self.root, text="Hello! And Weclome To The EasyA Program", font=('Arial', 20))
        self.headlabel1.pack(padx=10, pady=10)

        # Header explaining where data came from, how its limited, and the years included
        self.headlabel2 = tk.Label(self.root, text="The data included in this program was initially copied from https://emeraldmediagroup.github.io/grade-data/," + 
        " the data was copied on 01/15/2023, it includes class data from 2013-2016", font=('Arial', 10))
        self.headlabel2.pack(padx=10, pady=10)

        # Header explaining where data came from, how its limited, and the years included
        self.headlabel3 = tk.Label(self.root, text='(ATTENTION) This data is limited, not all courses are included "If your class doesnt show up here, it means the data was redacted"', font=('Arial', 10))
        self.headlabel3.pack(padx=10, pady=10)

        # Header explaining where data came from, how its limited, and the years included
        self.headlabel3 = tk.Label(self.root, text='- cited from the landing page of https://emeraldmediagroup.github.io/grade-data/', font=('Arial', 10))
        self.headlabel3.pack(padx=10, pady=10)

        # Itroduction header of landing page
        self.headlabel4 = tk.Label(self.root, text="To Begin, Please Select Whether You Are A:", font=('Arial', 18))
        self.headlabel4.pack(padx=10, pady=10)

        # Button to select the student user and open student user page
        self.stuBtn = tk.Button(self.root, text="Student", font=('Arial', 18), command=self.studentPage)
        self.stuBtn.pack(padx=10, pady=10)

        # Button to select the system admin and open system admin page
        self.sysABtn = tk.Button(self.root, text="System Admin", font=('Arial', 18), command=self.adminPage)
        self.sysABtn.pack(padx=10, pady=10)

        # GUI main loop
        self.root.mainloop()

    # Function that generates graph
    def generateGraph(self):

        # Error checking for missing department
        if self.select_dept.get() == '':
            print("ERROR: Please select a department")
            return 0
        
        # Error checking for course level or specific course number
        if (self.select_level.get() == '') and (self.specific_course.get() == ''):
            print("ERROR: Please select a cource level or specific course number")
            return 0
        
        # Turning the selected department name into department code
        dept_code = self.department.index(self.select_dept.get())
        print(self.dept_code[dept_code])

        # Use course levels if no specific course number is given
        if self.specific_course.get() == '':
            print(self.course_levels.index(self.select_level.get())+1)

        # Using specific course level only if it is not blank
        if self.specific_course.get() != '':
            print(self.specific_course.get())
        
        # Mode and faculty type selection
        print(self.mode.get())
        print(self.fac_type.get())

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

        # Frame containing the info for course selection
        course_info_frame = tk.LabelFrame(UserPage, text="Course Selection", font=('Arial', 16))
        course_info_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        # Department 
        dept_label = tk.Label(course_info_frame, text="Department", font=('Arial', 20))
        dept_label.grid(row=0, column=0)

        # Dropdown menu for department selection including all natural science departments
        dept_dropdown = ttk.Combobox(course_info_frame, state='readonly', values=self.department, textvariable=self.select_dept)
        dept_dropdown.grid(row=1, column=0)

        # Course Level
        course_level_label = tk.Label(course_info_frame, text="Course Level", font=('Arial', 20))
        course_level_label.grid(row=0, column=1)

        # Dropdown menu for course level selection from 100 to 600
        course_level_dropdown = ttk.Combobox(course_info_frame, state='readonly', values=self.course_levels, textvariable=self.select_level)
        course_level_dropdown.grid(row=1, column=1)

        # Specific Course Level
        spec_course_level_label = tk.Label(course_info_frame, text="Specific Course Level", font=('Arial', 20))
        spec_course_level_label.grid(row=0, column=2)

        # Text entry box that allows a user to search for a specific course level (111, 112, ...)
        spec_course_level_entry = ttk.Entry(course_info_frame, textvariable=self.specific_course)
        spec_course_level_entry.grid(row=1, column=2)

        # Give all widgets in this frame the same padding
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
        instructor_checkbox = tk.Checkbutton(graph_filter_frame, text="Just Regular Faculty", font=('Arial', 12), variable=self.fac_type)
        instructor_checkbox.grid(row=1, column=0)

        # Graph mode label
        graph_mode_label = tk.Label(graph_filter_frame, text="Graph Mode", font=('Arial', 20))
        graph_mode_label.grid(row=0, column=1)

        # Radio buttons that toggle between graph data modes
        # EasyA mode radio button
        easyA_radio_btn = tk.Radiobutton(graph_filter_frame, text="EasyA - Only A's", font=('Arial', 12), variable=self.mode, value=0)
        easyA_radio_btn.grid(row=1, column=1)

        # Just Pass mode radio button
        justPass_radio_btn = tk.Radiobutton(graph_filter_frame, text="Just Pass - D's and F's", font=('Arial', 12), variable=self.mode, value=1)
        justPass_radio_btn.grid(row=2, column=1)

        # Give all widgets in this frame the same padding
        for widget in graph_filter_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

        #-----------------Generate Graph Button---------------------

        # Generate Graph Button
        generate_graph_btn = tk.Button(UserPage, text="Generate Graph", font=('Arial', 20), command=self.generateGraph)
        generate_graph_btn.grid(row=3, column=0, sticky="ns", padx=20, pady=20)

    # Function to open the uploaded csv file
    def open_file(self):
        self.fp = filedialog.askopenfilename(initialdir='/Desktop', title='Select A File', filetypes=[('JSON Files', '*.json')])

    # Function that enters data from the uploaded csv file
    def enter_data(self):
        if self.fp == None:
            print("Error: No file uploaded")
            return None
        fp = open(self.fp, "r")
        print(fp.read())
        fp.close()

    # Function contaning system admin page
    def adminPage(self):
        
        #System admin page
        SysAdminPage = tk.Toplevel()
        SysAdminPage.title("EasyA/System Admin")
        
        #-----------------Generate Graph Button---------------------

        # Frame containing the instructions for how to update data
        admin_info_frame = tk.LabelFrame(SysAdminPage, text="System Admin Instructions", font=('Arial', 16))
        admin_info_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        # Admin instructions
        instructions_intro = tk.Label(admin_info_frame, text='To add data to the system:', font=('Arial', 12))
        instructions_intro.pack()

        # Upload instructions
        upload_inst = tk.Label(admin_info_frame, text='- Click the "Upload" button to select the csv data file you want to add to the system', font=('Arial', 12))
        upload_inst.pack()

        # enter instructions
        enter_inst = tk.Label(admin_info_frame, text='- Click the "Enter Data" button to add the file data into the system', font=('Arial', 12))
        enter_inst.pack()

        #-----------------Data Entry Frame---------------------

        # Frame containing file selection and data entry
        data_entry_frame = tk.LabelFrame(SysAdminPage, text="Data Entry", font=('Arial', 16))
        data_entry_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        # Upload Button Label
        upload_label = tk.Label(data_entry_frame, text="Upload CSV File", font=('Arial', 20))
        upload_label.grid(row=0, column=0)

        # Upload Button
        upload_btn = tk.Button(data_entry_frame, text="Upload", font=('Arial', 20), command=self.open_file)
        upload_btn.grid(row=0, column=1)

        # Give all widgets in this frame the same padding
        for widget in data_entry_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

        #-----------------Enter Data Button---------------------

        # Enter Data Button
        enter_data_btn = tk.Button(SysAdminPage, text="Enter Data", font=('Arial', 20), command=self.enter_data)
        enter_data_btn.grid(row=3, column=0, sticky="ns", padx=20, pady=20)

GUI()
