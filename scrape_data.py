""" scrape_data.py
Description:
For UO's CS 422 Project 1. Extracts data from UO grades data webpage 
and returns it as a python dictionary.
-by Alder French """

from bs4 import BeautifulSoup
import requests
import json


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

def write_class_dict_db(class_dict):
    # write the class dictionary to a .json file for use as our database
    # NOTE: see "json.load()" to convert db back to dictionary!
    db_file_name = "class_database.json"
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
    for dept_page_url in dept_page_urls:
        dept_page_names = scrape_faculty_names(dept_page_url)
        for name in dept_page_names:
            faculty_names_list.append(name)
    return faculty_names_list



def scrape_faculty_names(dept_page_url):
    '''
    Input: a specific departments page URL
    Output: a list of the faculty professor's names on that page
    How: gets all names from "p.facultylist" in html with bs4
    '''
    html_doc = requests.get(dept_page_url)
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
        print("Test names: " + faculty_name) #TODO: left off here!
        faculty_names.append(faculty_name)
    return faculty_names


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
    faculty_names = get_faculty_names()
    print("Testing faculty name scraping")
    i = 1
    for name in faculty_names:
        i += 1
        print("Faculty member's name: " + name)
        if i > 5:
            break




    


