""" scrape_data.py
Description:
For UO's CS 422 Project 1. Extracts data from UO grades data webpage 
and returns it as a python dictionary.
-by Alder French """

from bs4 import BeautifulSoup
import requests
import json
import time
import random
from urllib3.exceptions import NewConnectionError


def extract_json(text):  # takes string and returns text sliced from first bracket to last bracket
    bracket_counter = 0
    started = False
    start_pos = 0
    end_pos = 0
    counter = 0
    for character in text:
        if character == "{":
            bracket_counter += 1
            if not started:
                started = True
                start_pos = counter
            started = 1
        if character == "}":
            bracket_counter -= 1
        if started and bracket_counter == 0:
            end_pos = counter + 1
            break
        counter += 1
    #print("Start pos: " + str(start_pos) + " End pos: " + str(end_pos))
    return text[start_pos:end_pos] 

def get_class_dict():
    # Load Webpage, turn it into soup, then extract json from js var, 
    # and then RETURN a python dictionary from that json where
    # each element in the dictionary uses a class code e.g. "AA508" as a key
    # and each element contains a list of dictionaries where each of those 
    # dictionaries contains data about a specific term of that class
    grade_data_url = "https://emeraldmediagroup.github.io/grade-data/gradedata.js"
    html_doc = requests.get(grade_data_url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    json_text = extract_json(soup.text)
    site_dict = json.loads(json_text)

    return site_dict

def write_class_dict_db(db_file_name, class_dict):
    # write the class dictionary to a .json file for use as our database
    # NOTE: see "json.load()" to convert db back to dictionary!
    with open(db_file_name, "w") as outfile:
        json.dump(class_dict, outfile)

def get_faculty_names():
    '''
    Input: (No input)
    Returns: List of faculty names?
    '''
    faculty_names_url = "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/"
    html_doc = requests.get(faculty_names_url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    # finding departments table <ul> tag
    depts_table = soup.find("body").find("ul", id="/arts_sciences/")
    # finding all <li> tags
    departments = depts_table.find_all("li")
    # iterate through deptartment paragraphs and extract their page URLs
    dept_page_urls = []
    for dept in departments:
        url = dept.find("a")['href']
        full_url = "https://web.archive.org" + url
        dept_page_urls.append(full_url)
    # next iterate though department page URLs and collect their faculty names
    faculty_names_list = []
    dept_number = 1
    for dept_page_url in dept_page_urls:
        print("TESTING: Currently scraping from department #" + str(dept_number))
        dept_page_names = scrape_faculty_names(dept_page_url)
        time.sleep(random.randrange(3, 7, 1)) # This is to avoid "Error 54 - Connection Reset By Peer" (server blocks scraping)
        dept_number += 1
        for name in dept_page_names:
            faculty_names_list.append(name)
    return faculty_names_list



def scrape_faculty_names(dept_page_url):
    '''
    Input: a specific departments page URL
    Output: a list of the faculty professor's names on that page
    How: gets all names from "p.facultylist" in html with bs4
    '''
    try:
        html_doc = requests.get(dept_page_url)
    except Exception as e:
        print("ERROR - manually caught an Exception, error is: " + str(e))
        return []
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    faculty_paragraphs = soup.find_all("p", class_="facultylist")
    faculty_names = []
    for paragraph in faculty_paragraphs:
        #print("Test paragraphs: " + str(paragraph))
        if "," in str(paragraph):
            first_comma_pos = str(paragraph).index(",")
            first_alligator_pos = str(paragraph).index(">")
        else:
            continue
        faculty_name = str(paragraph)[first_alligator_pos+1:first_comma_pos]
        print("Test names: " + faculty_name)
        faculty_names.append(faculty_name)
    return faculty_names


def write_faculty_list(faculty_names):
    '''
    Input: faculty_names - list of faculty names
    Output: Returns nothing, but writes faculty names to .txt file,
    with 1 name per line. 
    '''
    faculty_file_name = "regular_faculty_names.txt"
    with open(faculty_file_name, "w") as outfile:
        for name in faculty_names:
            outfile.write(f"{name}\n")


def add_regular_faculty_to_db(faculty_file_name, database_file_name):
    '''
    Input: Nothing
    Output: Returns nothing, but reads regular faculty names from faculty names
    .txt list in form "First M. Last" and uses them to iterate through the
    classes in the database and adds the key-value pair:
    "Regular_faculty: true/false (boolean)" to each classes dictionary
    '''
    #open database, convert to python dictionary, add all regular faculty then
    # after thats all done, rewrite the database from scratch with the updated db.
    with open(database_file_name, "r") as db_file:
        db = json.loads(db_file) # convert database.json to python dictionary
        with open(faculty_file_name, "r") as fac_name_file:
            # first get a teacher's name from the faculty list in form "First M. Last"
            for fac_name in fac_name_file:
                name_tok = fac_name.split()
                # Next iterate through each class in the database by iterating
                # through each class_code in outer_dic, then iterate through
                # each class in the outer_dics list, and then check each inner_dic 
                # (which are the class elements in the outer_dic's list) to see if
                # their teacher is regular faculty, if so add:
                # "fregular: True" to the classes dictionary,
                # if else add: "fregular: False"
                for class_code in db:
                    for class_list_element in db[class_code]:
                        db_teacher_name = class_list_element["instructor"]
                        toks_in_name = 0
                        for tok in name_tok:
                            if tok in db_teacher_name:
                                toks_in_name += 1
                        if toks_in_name > 1: # at least 2 name parts match so mark regular
                            class_list_element["fregular"] = "True"
                        else:
                            class_list_element["fregular"] = "False"
    write_class_dict_db(database_file_name, db)
                                




def test_class_dict():
    test_dict = get_class_dict()
    i = 0
    print("BEGIN TESTING...")
    for class_code in test_dict:
        if i > 2:
            print("END TESTING...")
            break
        print("The current class code is: " + str(class_code))
        print("It has the contents: " + str(test_dict[class_code]))
        print("The dictionary contains: " +
              str(test_dict[class_code][0]['TERM_DESC']))
        i += 1


if __name__ == "__main__": # Write class dictionary to json database file
    #class_dict = get_class_dict()
    #write_class_dict_db(class_dict)
    #faculty_names = get_faculty_names()
    #write_faculty_list(faculty_names)

    # Test Update DB by adding regular faculty to its copy
    faculty_file_name = "regular_faculty_names.txt"
    database_file_name = "class_database_copy.json"
    add_regular_faculty_to_db(faculty_file_name, database_file_name)


    '''
    print("Testing faculty name scraping")
    i = 1
    for name in faculty_names:
        i += 1
        print("Faculty member's name: " + name)
        if i > 5:
            break
    '''




    


