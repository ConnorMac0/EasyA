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
    # Setup variables for data
    values = []
    names = []
    ints = 0

    # Setup dictionaries for data
    class_dictionary = {}
    grade_dictionary = {}

    # Load the JSON data from a file
    with open("class_database.json", "r") as file:
        data = json.load(file)

    # Check to see how many integers are in the given class code
    for i in code:
        if i in ['1', '2', '3', '4', '5', '6']:
            ints += 1

    # Check the data set for the given input
    for key, value in data.items():
        # Explicit exclusion of "ARCH" (Architecture) classes for when we search for "CH" (Chemistry)
        if "ARCH" in key:
            continue

        # If the given class code matches a class in the dataset
        if code in key:

            # If there is only 1 integer in the given class code, we search for all classes
            # in that department at the level of the integer given
            if ints == 1:

                # Check each course in given class code
                for item in value:

                    # If we are only looking for regular faculty
                    if faculty:
                        if item["fregular"] == "True":

                            # Add their name to the list
                            names.append(key)

                            # Check if we want % As or % Ds/Fs
                            if aorf:
                                values.append(str(float(item["dprec"]) + float(item["fprec"])))

                            else:
                                values.append(item["aprec"])

                    # If we are looking for all faculty
                    else:

                        # Add their name to the list
                        names.append(key)

                        # Check if we want % As or % Ds/Fs
                        if aorf:
                            values.append(str(float(item["dprec"]) + float(item["fprec"])))

                        else:
                            values.append(item["aprec"])

            # If there are 0 or 3 integers
            else:

                # Check each course in given class code
                for item in value:

                    # If we are only looking for regular faculty
                    if faculty:
                        if item["fregular"] == "True":

                            # Add their name to the list
                            names.append(item["instructor"])

                            # Check if we want % As or % Ds/Fs
                            if aorf:
                                values.append(str(float(item["dprec"]) + float(item["fprec"])))

                            else:
                                values.append(item["aprec"])

                    # If we are looking for all faculty
                    else:

                        # Add their name to the list
                        names.append(item["instructor"])

                        # Check if we want % As or % Ds/Fs
                        if aorf:
                            values.append(str(float(item["dprec"]) + float(item["fprec"])))

                        else:
                            values.append(item["aprec"])

    # Filling a dictionary with teachers and how many classes they teach
    for per in names:
        if per in class_dictionary:
            class_dictionary[per] += 1

        else:
            class_dictionary[per] = 1

    # List to hold the last names of teachers
    split_names = []

    # Getting the last names of the teachers
    for name in names:

        split_name = name.split(',')[0]

        # Check if we want to display the number of classes they teach,
        # and if we do we add it to their name in the list
        if num_classes:
            split_name = f'{split_name} ({class_dictionary[name]})'

        split_names.append(split_name)

    # Removing duplicate names from the original list
    split_names_list = list(set(split_names))

    # If we have 0 or 3 integers we calculate the average % As or Ds/Fs
    # to get the overall % of As or Ds/Fs that teachers give to students
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

    # Close the file
    file.close()

    # Create a figure and a set of subplots
    fig, ax = plt.subplots(figsize=(20, 8))
    plt.xticks(rotation=90)
    width = 0.5

    # Check for what the label on the y-axis should say
    if aorf:
        plt.ylabel("% Ds / Fs")

    else:
        plt.ylabel("%\nAs")

    # Check for what the label on the x-axis should say
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

    # Display the graph
    plt.show()
