"""
Description:
CS 422 Project 1, this file will read data from a JSON file
and output a UI with a graph displaying the data for easy
comparison.
"""

# Import statements for creating and displaying graphs
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import json


def class_search(code, aorf, faculty, num_classes):
    values = []
    names = []

    dictionary = {}

    # Load the JSON data from a file
    with open("class_database.json", "r") as file:
        data = json.load(file)

    for key, value in data.items():
        if code in key:
            for item in value:
                if faculty:
                    if item["fregular"] == "True":
                        names.append(item["instructor"])
                        if aorf:
                            values.append(str(float(item["dprec"]) + float(item["fprec"])))
                        else:
                            values.append(item["aprec"])
                else:
                    names.append(item["instructor"])
                    if aorf:
                        values.append(str(float(item["dprec"]) + float(item["fprec"])))
                    else:
                        values.append(item["aprec"])

                # print(key, item["TERM_DESC"], item["instructor"], item["aprec"], item["bprec"])
            values = sorted(values, key=float)

    for per in names:
        if per in dictionary:
            dictionary[per] += 1
        else:
            dictionary[per] = 1

    split_names = []

    for name in names:
        split_name = name.split(',')[0]
        if num_classes:
            split_name = f'{split_name} ({dictionary[name]})'
        split_names.append(split_name)

    print(values)
    print(split_names)
    print(dictionary)

    file.close()

    root = tk.Tk()

    # Create a figure and a set of subplots
    fig, ax = plt.subplots(figsize=(15,8))

    plt.xticks(rotation=90)

    # Create the bar chart
    ax.bar(split_names, values)



    # Create the Tkinter canvas to display the chart
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    root.mainloop()


class_search("MATH1", 0, 0, 0)

