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
    html_doc = requests.get(
        "https://emeraldmediagroup.github.io/grade-data/gradedata.js")
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    json_text = extract_json(soup.text)
    site_dict = json.loads(json_text)

    return site_dict

    


if __name__ == "__main__": # TEST THIS PROGRAM
    test_dict = get_class_dict()
    i = 0
    print("BEGIN TESTING...")
    for class_code in test_dict:
        if i > 2:
            print("END TESTING...")
            break
        print("The current class code is: " + str(class_code))
        print("It has the contents: " + str(test_dict[class_code]))
        print("The dictionary contains: " + str(test_dict[class_code][0]['TERM_DESC']))
        i += 1





    


