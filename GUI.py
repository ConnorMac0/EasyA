"""
Description: 
For UO's CS 422 Project 1. A graphical user interface to interact with the data
in the EasyA project. Allows input from students, system admins, and displays 
data in bar graph form.
"""

import tkinter as tk

#--------------GOALS-------------
#Finish user and admin layouts
#Determine how we want to accept inputs
#Change so multiple windows are opened, change main window after user selection

class GUI:
    #initialize the landing page
    def __init__(self):
        self.root = tk.Tk()             
        self.root.title("EasyA")        #Give title

        #Itroduction header of landing page
        self.headlabel1 = tk.Label(self.root, text="Hello! And Weclome To The EasyA Program", font=('Arial', 20))
        self.headlabel1.pack(padx=10, pady=10)

        #Itroduction header of landing page
        self.headlabel2 = tk.Label(self.root, text="Please Select Whether You Are A:", font=('Arial', 18))
        self.headlabel2.pack(padx=10, pady=10)

        #Button to select the student user and open student user page
        self.stuBtn = tk.Button(self.root, text="Student", font=('Arial', 18), command=self.userPage)
        self.stuBtn.pack(padx=10, pady=10)

        #Button to select the system admin and open system admin page
        self.sysABtn = tk.Button(self.root, text="System Admin", font=('Arial', 18), command=self.adminPage)
        self.sysABtn.pack(padx=10, pady=10)

        #GUI main loop
        self.root.mainloop()

    #Function that opens user page
    def userPage(self):
        
        UserPage = tk.Toplevel()
        UserPage.geometry("400x400")
        
        headlabel1 = tk.Label(UserPage, text="User Page", font=('Arial', 25))
        headlabel1.pack(padx=10, pady=10)

    #Function that opens system admin page
    def adminPage(self):
        
        SysAdminPage = tk.Toplevel()
        SysAdminPage.geometry("400x400")
        
        headlabel1 = tk.Label(SysAdminPage, text="System Admin Page", font=('Arial', 25))
        headlabel1.pack(padx=10, pady=10)

GUI()
