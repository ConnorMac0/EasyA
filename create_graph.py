'''
Description:
CS 422 Project 1, this file will read data from a JSON file
and output a UI with a graph displaying the data for easy
comparison.
'''

# Import statements for creating and displaying graphs
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import json

# Arbitrary data
values = []
names = []

# Load the JSON data from a file
with open("class_database.json", "r") as file:
    data = json.load(file)

for key, value in data.items():
    if "MATH2" in key:
        for item in value:
            values.append(item["aprec"])
            names.append(item["instructor"])
            #print(key, item["TERM_DESC"], item["instructor"], item["aprec"], item["bprec"])
        values = sorted(values, key=float)
    print(values)
    print(names)

file.close()


root = tk.Tk()

# Create a figure and a set of subplots
fig = Figure(figsize=(5, 4))
ax = fig.add_subplot(111)

# Create the bar chart
ax.bar(names, values)

# Create the Tkinter canvas to display the chart
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()


def class_code_search(code):
    pass


def department_search(code):
    pass


def class_level_search(code):
    pass



