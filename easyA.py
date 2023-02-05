"""
Description: 
For UO's CS 422 Project 1. A graphical user interface to interact with the data
in the EasyA project. Allows input from students, system admins, and displays 
data in bar graph form.
Author: Connor Maclachlan
Group: Group #4
Created: 01/25/2023
Last Updated: 02/04/2023
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json
import create_graph as cg

class GUI:
    """Graphical User Interface class that creates an interface for the 
        student and system admins users to interact with the EasyA program"""

    def __init__(self):
        """Initialization of the GUI landing page"""
        self.root = tk.Tk()
        self.root.title("EasyA")

        # Landing, User, and Admin frames
        self.LandingPage = tk.Frame(self.root)
        self.UserPage = tk.Frame(self.root)
        self.SysAdminPage = tk.Frame(self.root)           

        # New data file
        self.fp = None

        # Natural Science department names
        self.department = ["Anthropology", "Biology", "Chemistry and Biochemistry", "Computer Science", "Data Science", 
                        "Earth Sciences", "Geography", "Human Physiology", "Mathematics", "Physics", "Psychology"]
        # Department codes
        self.dept_code = ["ANTH", "BI", "CH", "CIS", "DSC", "GEOL", "GEOG", "HPHY", "MATH", "PHYS", "PSY"]

        # Course level options
        self.course_levels = ["All Department", "All 100-Level", "All 200-Level", "All 300-Level", "All 400-Level", "All 500-Level", "All 600-Level"]
        self.specific_course = tk.StringVar()

        # Department and course level variables
        self.select_dept = tk.StringVar()
        self.select_level = tk.StringVar()
        
        # Graph mode radio button variable
        self.mode = tk.IntVar()
        self.fac_type = tk.IntVar()
        self.class_count = tk.IntVar()

        self.LandingPage.pack(fill="both", expand=1)
        self.LandingPage.config(bg='green')

        # Itroduction header of landing page
        self.headlabel1 = tk.Label(self.LandingPage, text="Weclome To The EasyA Program", font=('Arial', 20), bg='green')
        self.headlabel1.pack(padx=10, pady=10)

        # Itroduction header of landing page
        self.headlabel2 = tk.Label(self.LandingPage, text="To Begin, Please Select Whether You Are A:", font=('Arial', 18), bg='green')
        self.headlabel2.pack(padx=10, pady=10)

        # Button to select the student user and open student user page
        self.stuBtn = tk.Button(self.LandingPage, text="Student", font=('Arial', 18), command=self.studentPage, highlightbackground='yellow')
        self.stuBtn.pack(padx=10, pady=10)

        # Button to select the system admin and open system admin page
        self.sysABtn = tk.Button(self.LandingPage, text="System Admin", font=('Arial', 18), command=self.adminPage, highlightbackground='yellow')
        self.sysABtn.pack(padx=10, pady=10)
    
        # Header explaining where data came from, how its limited, and the years included
        self.cite_label1 = tk.Label(self.LandingPage, text="(ATTENTION) The data included in this program was copied from https://emeraldmediagroup.github.io/grade-data/", font=('Arial', 8), bg='green')
        self.cite_label1.pack(padx=10, pady=10)

        self.cite_label2 = tk.Label(self.LandingPage, text='The data was initially copied on 01/15/2023, it includes class data from 2013-2016', font=('Arial', 8), bg='green')
        self.cite_label2.pack(padx=10, pady=10)

        # Header explaining where data came from, how its limited, and the years included
        self.cite_label3 = tk.Label(self.LandingPage, text='This data is limited, not all courses are included "If your class doesnt show up here, it means the data was redacted"', font=('Arial', 8), bg='green')
        self.cite_label3.pack(padx=10, pady=10)

        # Header explaining where data came from, how its limited, and the years included
        self.cite_label4 = tk.Label(self.LandingPage, text='- cited from the landing page of https://emeraldmediagroup.github.io/grade-data/', font=('Arial', 8), bg='green')
        self.cite_label4.pack(padx=10, pady=10)

        # GUI main loop
        self.root.mainloop()

    # Function that generates graph
    def generateGraph(self):
        """ Function calls the graph visualizing script and passes
            in user provided input as variables to determine what data to display in the graphs
        """

        # Error checking for missing department
        if self.select_dept.get() == '':
            messagebox.showerror('Error', 'Please Select a Department')
            return 0
        
        # Error checking for course level or specific course number
        if (self.select_level.get() == '') and (self.specific_course.get() == ''):
            messagebox.showerror('Error', 'Please Select a Couse Level or Specific Course Number')
            return 0
        
        # Turning the selected department name into department code
        dept_code = self.department.index(self.select_dept.get())

        # Use course levels if no specific course number is given
        if self.specific_course.get() == '':
            if self.course_levels.index(self.select_level.get()) != 0:
                cg.class_search(self.dept_code[dept_code] + str(self.course_levels.index(self.select_level.get())), self.mode.get(), self.fac_type.get(), self.class_count.get())
            else:
                cg.class_search(self.dept_code[dept_code], self.mode.get(), self.fac_type.get(), self.class_count.get())

        # Using specific course level only if it is not blank
        if self.specific_course.get() != '':

            # Error checking for valid course number
            if len(self.specific_course.get()) != 3 or int(self.specific_course.get()) > 699:
                messagebox.showerror('Error', 'Invalid Course Number: Please Enter A 3 Digit Number Between 100-699')
                return 0

            cg.class_search(self.dept_code[dept_code] + self.specific_course.get(), self.mode.get(), self.fac_type.get(), self.class_count.get())

    # Function containing student page
    def studentPage(self):
        """Function that contains the student user page data for the GUI"""
        
        # Student Page
        self.UserPage.pack(fill="both", expand=1)
        self.LandingPage.pack_forget()
        self.SysAdminPage.pack_forget()
        self.UserPage.config(bg='green')

        #-----------------Course Selection Info Frame---------------------

        # Frame containing the info for course selection
        course_info_frame = tk.LabelFrame(self.UserPage, text="Course Selection", font=('Arial', 16))
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
        graph_filter_frame = tk.LabelFrame(self.UserPage, text="Graph Data Filter", font=('Arial', 16))
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

        # Instructor selection label
        instructor_label = tk.Label(graph_filter_frame, text="Include Class Count", font=('Arial', 20))
        instructor_label.grid(row=0, column=2)

        # Class count checkbox
        class_count_check = tk.Checkbutton(graph_filter_frame, text="Include Class Count", font=('Arial', 12))
        class_count_check.grid(row=1, column=2)

        # Class count checkbox
        class_count_check = tk.Checkbutton(graph_filter_frame, text="Include Class Count", font=('Arial', 12), variable=self.class_count)
        class_count_check.grid(row=1, column=2)

        # Give all widgets in this frame the same padding
        for widget in graph_filter_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

        #-----------------Generate Graph Button---------------------

        # Generate Graph Button
        generate_graph_btn = tk.Button(self.UserPage, text="Generate Graph", font=('Arial', 20), command=self.generateGraph, highlightbackground='yellow')
        generate_graph_btn.grid(row=3, column=0, sticky="ns", padx=20, pady=20)

        # Back Button
        back_btn = tk.Button(self.UserPage, text="Back", font=('Arial', 20), command=self.backButton, highlightbackground='yellow')
        back_btn.grid(row=4, column=0, sticky="ns", padx=20, pady=20)

    def open_file(self):
        """Function that allows the user to select and open a JSON file from their computer"""
        self.fp = filedialog.askopenfilename(initialdir='/Desktop', title='Select A File', filetypes=[('JSON Files', '*.json')])

    def enter_data(self):
        """Function that reads in new data from a user selected JSON file and adds it to or modifies the 
            old Easy A database"""

        # Error checking to make sure a file was selected
        if self.fp == None or self.fp == '':
            messagebox.showerror('Error', 'Please Select A File To Upload')
            return 0

        # Opening selected file and database to edit
        database = open(self.fp, "r")
        with open("class_database.json", "r") as newDataFile:
            oldData = json.load(newDataFile)
            newData = json.load(database)

        # Adding new data to old database dictionary
        for key in newData:
            oldData[key] = newData[key]
    
        # Adding dictionary changes to database
        with open("class_database.json", "w") as newDataFile:
            json.dump(oldData, newDataFile)

        # Closing file
        database.close()
        messagebox.showinfo('Info', 'Data Successfully Uploaded!')

    def adminPage(self):
        """Function that contains the system admin page data of the GUI"""
        
        #System admin page
        self.SysAdminPage.pack(fill="both", expand=1)
        self.LandingPage.pack_forget()
        self.UserPage.pack_forget()
        self.SysAdminPage.config(bg='green')

        #-----------------Data Entry Frame---------------------

        # Frame containing file selection and data entry
        data_entry_frame = tk.LabelFrame(self.SysAdminPage, text="Data Entry", font=('Arial', 16))
        data_entry_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        # Upload Button Label
        upload_label = tk.Label(data_entry_frame, text="Upload JSON File", font=('Arial', 20))
        upload_label.grid(row=0, column=0)

        # Upload Button
        upload_btn = tk.Button(data_entry_frame, text="Upload", font=('Arial', 20), command=self.open_file)
        upload_btn.grid(row=0, column=1)

        # Give all widgets in this frame the same padding
        for widget in data_entry_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

        #-----------------Enter Data Button---------------------

        # Enter Data Button
        enter_data_btn = tk.Button(self.SysAdminPage, text="Enter Data", font=('Arial', 20), command=self.enter_data, highlightbackground='yellow')
        enter_data_btn.grid(row=3, column=0, sticky="ns", padx=20, pady=20)
        
        # Back Button
        back_btn = tk.Button(self.SysAdminPage, text="Back", font=('Arial', 20), command=self.backButton, highlightbackground='yellow')
        back_btn.grid(row=4, column=0, sticky="ns", padx=20, pady=20)


    def backButton(self):
        """Function to return to the landing page"""
        self.LandingPage.pack(fill="both", expand=1)
        self.SysAdminPage.pack_forget()
        self.UserPage.pack_forget()

GUI()
