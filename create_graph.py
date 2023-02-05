"""
Description:
CS 422 Project 1, this file will read data from a JSON file
and output a UI with a graph displaying the data for easy
comparison.
"""

# Import statements for creating and displaying graphs
import json
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


def convert_to_floats(arr):
    # Use the map function to apply the float function to each element in the input list
    result = map(float, arr)

    # Return the resulting iterator as a list
    return list(result)


def class_search(code, aorf, faculty, num_classes):
    values = []
    names = []
    ints = 0

    class_dictionary = {}
    grade_dictionary = {}

    # Load the JSON data from a file
    with open("class_database.json", "r") as file:
        data = json.load(file)

    for i in code:
        if i in ['1', '2', '3', '4', '5', '6']:
            ints += 1

    for key, value in data.items():
        if "ARCH" in key:
            continue
        if code in key:
            if ints == 1:
                for item in value:
                    if faculty:
                        if item["fregular"] == "True":

                            names.append(key)

                            if aorf:
                                values.append(str(float(item["dprec"]) + float(item["fprec"])))

                            else:
                                values.append(item["aprec"])

                    else:

                        names.append(key)

                        if aorf:
                            values.append(str(float(item["dprec"]) + float(item["fprec"])))

                        else:
                            values.append(item["aprec"])

            else:

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

    sorted_values = sorted(values, key=float)

    for per in names:
        if per in class_dictionary:
            class_dictionary[per] += 1

        else:
            class_dictionary[per] = 1

    split_names = []

    for name in names:

        split_name = name.split(',')[0]

        if num_classes:
            split_name = f'{split_name} ({class_dictionary[name]})'

        split_names.append(split_name)
    split_names_list = list(set(split_names))

    if ints != 1:
        for i in range(len(values)):

            key = split_names[i]

            if key not in grade_dictionary:
                grade_dictionary[key] = [0, 0]

            grade_dictionary[key][0] += float(values[i])
            grade_dictionary[key][1] += 1

        for key in grade_dictionary:
            average = grade_dictionary[key][0] / grade_dictionary[key][1]
            grade_dictionary[key] = average

    #print(grade_dictionary)


    print(len(grade_dictionary.values()))
    print(grade_dictionary.values())
    print(len(split_names_list))
    #print(class_dictionary)

    file.close()

    # Create a figure and a set of subplots
    fig, ax = plt.subplots(figsize=(20, 8))
    plt.xticks(rotation=90)
    width = 0.5

    if aorf:
        plt.ylabel("% Ds / Fs")

    else:
        plt.ylabel("%\nAs")

    if ints == 1:
        plt.xlabel("Course")

    else:
        plt.xlabel("Teacher")

    # Create the bar chart
    if ints == 1:
        ax.bar(split_names, convert_to_floats(values), width)
    else:
        ax.bar(grade_dictionary.keys(), convert_to_floats(grade_dictionary.values()), width)
    ax.set_ylim([0, 100])
    plt.subplots_adjust(top=.98, bottom=.2)

    plt.show()


class_search("CH2", 0, 0, 0)
