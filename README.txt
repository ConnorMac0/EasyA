###CS 442 EASYA GROUP PROJECT DESCRIPTION
This system allows students to check grade percentages from professors of a chosen course or course level and outputs a graph comparing professors or courses.
The system also allows administrators to add new data to the system.

##AUTHORS
Garrett Bunkers, Alder French , Connor Maclachlan, Juan Rios, Blake Skelly

##DATE_CREATED
1/25/2023

##SOFTWARE_DEPENDENCIES
Python 3.8+

##SETUP
Go to Installation_Instructions.pdf for how to compile and run the program
##DIRECTORY COMPONENTS

    #READ_FILES
    SRS.pdf - Software Requirements Specification
    SDS.pdf - Software Design Specification
    Project_Plan.pdf - Description of how the meetings, policies and system were planned
    README.txt - This File!
    Installation_Instructions.pdf - Guide to compiling and running the program
    Programmer_Documentation.pdf - describes how the system works and major data structures
    User_Documentstion.pdf - descirbes how to accomplish specific tasks with the system
    CS 422 - SM - EasyA - Group #4 - Meeting Notes.pdf - Notes on meeting attendance and discussion
    class_database.json - file that contains UO grade data
    regular_faculty_names.txt - includes only the regular faculty names from UO

    #.py FILES
    scrape_data.py - Python script that scrapes data from the UO class data webpage and puts it in a .txt file that contains all the class data in JSON format.
    easyA.py -  Python script that contains the code for the interface of our EasyA system.
    create_graph.py - Python script that grabs and sorts data from class_database.json and plots it on a bar graph
