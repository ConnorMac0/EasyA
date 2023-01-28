import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

data = [{'name': 'item1', 'value': 5},
        {'name': 'item2', 'value': 10},
        {'name': 'item3', 'value': 15},
        {'name': 'item4', 'value': 20}]

root = tk.Tk()

# Create a figure and a set of subplots
fig = Figure(figsize=(5, 4))
ax = fig.add_subplot(111)

# Extract the values and labels from the data
values = [d['value'] for d in data]
labels = [d['name'] for d in data]

# Create the bar chart
ax.bar(labels, values)

# Create the Tkinter canvas to display the chart
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()