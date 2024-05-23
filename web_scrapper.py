import os
import requests
from bs4 import BeautifulSoup
import json
import PyPDF2
import io
import pandas as pd
import tabula
from tabula import read_pdf
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
'''
This script scrapes course data from the Sabanci University website and saves it in JSON format.
Developed by: Zeynep Kurtuluş 12.03.2024 for ENS492 Graduation Project Spring 2023-2024
'''
json_file_storage = []
course_mapping = {}
def main():
    faculties = [1, 2, 3, 4]

    course_mapping = suchedule_scrapper()
    for faculty in faculties:
        major_codes = []
        course_types = []

        if faculty == 1:
            major_codes = ["BSCS", "BSEE", "BSMS", "BSMAT", "BSME", "BSBIO"]
            course_types = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "Basic Science and Engineering Courses", "University Courses"]
        elif faculty == 2:
            major_codes = ["BAECON", "BAVACD"]
            course_types = ["Area Courses", "Required Courses", "Core Courses", "Free Courses",  "University Courses"]
        elif faculty == 3:
            major_codes = ["BAMAN"]
            course_types = ["Area Courses", "Required Courses", "Core Courses", "Free Courses",  "University Courses"]
        elif faculty == 4:
            major_codes = ["BAPSY"]
            course_types = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "Philosophy Requirement Courses",  "University Courses"]

        for major_code in major_codes:
            for course_type in course_types:
                #print(f"Scraping data for {major_code} - {course_type}")
                scrapper_caller(major_code, course_type)


def scrapper_caller(major_code, course_type):
    #print("major code: ", major_code, "course type: ", course_type)
    for year in range(2018, 2024):
        for semester in range(1, 3):
            year_semester = f"{year}0{semester}"

            if major_code == "BSEE":
                if course_type == "Area Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA=BSEE_ARE&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                elif course_type == "Required Courses" or course_type == "University Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_degree_detail?P_TERM={year_semester}&P_PROGRAM=BSEE&P_SUBMIT=&P_LANG=ENG&P_LEVEL=UG"
                elif course_type == "Core Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA=BSEE_CEL&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                elif course_type == "Free Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA=BSEE_FRE&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                elif course_type == "Basic Science and Engineering Courses":
                    url = f"https://mysu.sabanciuniv.edu/sr/sites/mysu.sabanciuniv.edu.sr/files/fens_course_catalog_basicscienceengineering_-_ects_okya_giden25.01.2024.pdf"


            elif major_code == "BSCS" or major_code == "BSMS" or major_code == "BSMAT" or major_code == "BSME" or major_code == "BSBIO":
                if course_type == "Area Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_AEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                elif course_type == "Required Courses" or course_type == "University Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=TR&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={year_semester}"
                elif course_type == "Core Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_CEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
               
                elif course_type == "Free Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_FEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                elif course_type == "Basic Science and Engineering Courses":
                    url = f"https://mysu.sabanciuniv.edu/sr/sites/mysu.sabanciuniv.edu.sr/files/fens_course_catalog_basicscienceengineering_-_ects_okya_giden25.01.2024.pdf"
            
            elif major_code == "BAECON"  or major_code == "BAVACD" :
                if course_type == "Required Courses" or course_type == "University Courses" or course_type == "Core Courses" or course_type == "Philosophy Requirement Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=TR&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={year_semester}"
                elif course_type == "Area Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_ARE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"

                elif course_type == "Free Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_FRE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
            
            elif major_code == "BAMAN" or major_code == "BAPSY":
                if course_type == "Required Courses" or course_type == "University Courses" or course_type == "Core Courses" or course_type == "Philosophy Requirement Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=TR&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={year_semester}"
                elif course_type == "Area Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_ARE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                
                elif course_type == "Free Courses":
                    url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={year_semester}&P_AREA={major_code}_FRE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"


                   

            #print("url is: ", url)
            scraper(url, year_semester, major_code)


def parse_crn_info(crn_info):
    current_course = None
    current_section = None

    for line in crn_info:
        if " - " in line:
            # This line contains a course name
            current_course = line.split(" - ")[0].strip()
            course_mapping[current_course] = {'sections': {}}
        elif " " not in line:
            # This line contains a course section
            current_section = line.strip()
            if current_section not in course_mapping[current_course]['sections']:
                course_mapping[current_course]['sections'][current_section] = {'times': []}
        elif ":" in line or "TBA" in line:
            # This line contains a time info or TBA
            # Check if current_course and current_section are set before appending time
            if current_course is not None and current_section is not None:
                course_mapping[current_course]['sections'][current_section]['times'].append(line.strip())
                
            else:
                # If either current_course or current_section is None, print a warning message
                print("Warning: Time information found before course name or section.")

    return course_mapping


def suchedule_scrapper():
    # Launch the Chrome browser
    driver = webdriver.Chrome()
    
    # Load the webpage
    driver.get("https://aburakayaz.github.io/suchedule/")
    
    try:
        selected_course_sections = driver.find_elements_by_css_selector(".course-name , .section-day , .section-group")
        # Extract text from course sections
        crns = [" ".join(section.get_attribute("innerHTML").split()) for section in selected_course_sections]

        with open("crn.txt", "a", encoding='utf-8') as text_file:
            for crn in crns:
                text_file.write(f"{crn}\n")

        # Print the scraped data
        #print("CRN Information:", crns)
        course_mapping = parse_crn_info(crns)

        with open("course_mapping.txt", "a", encoding='utf-8') as file:
            for course_name, course_info in course_mapping.items():
                file.write(f"course_name: {course_name}\n")
                for section, section_info in course_info['sections'].items():
                    file.write(f"\tSection: {section}\n")
                    for time in section_info['times']:
                        file.write(f"\t\tTime: {time}\n")
                file.write("\n")

        return course_mapping

    finally:
        # Close the browser
        driver.quit()


def scraper(url, entry, major_code):
    # Define categories of courses
    #print("major code: ", major_code, "url: ", url, "entry: ", entry)
    if major_code == "BSEE" or major_code == "BSCS" or major_code == "BSMS" or major_code == "BSMAT" or major_code == "BSME" or major_code == "BSBIO":
        categories = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "Basic Science and Engineering Courses", "University Courses"]
    elif major_code == "BAECON" or major_code == "BAVACD":
        categories = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "University Courses"]
    elif major_code == "BAPSY":
        categories = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "Philosophy Requirement Courses", "University Courses"]
    elif major_code == "BAMAN": 
        categories = ["Area Courses", "Required Courses", "Core Courses", "Free Courses", "University Courses"]
    
    output_directory = major_code
    os.makedirs(output_directory, exist_ok=True)
    
    # Create subfolders for each category of courses
    for category in categories:
        category_folder = os.path.join(output_directory, category)
        os.makedirs(category_folder, exist_ok=True)

        file_path = f"{output_directory}/{category}/{major_code}_{entry}_CatReq.txt"
        json_path = f"{output_directory}/{category}/{major_code}_{entry}_CatReq.json"
        #print("file path: ", file_path)
        #print("category: ", category)
        json_file_storage.append(json_path)
        
        if os.path.exists(json_path):
            print(f"{file_path} already exists. Moving on.")
        else:
            try:
                if major_code == "BSEE":
                    if category == "Area Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA=BSEE_ARE&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Required Courses" or category == "University Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_degree_detail?P_TERM={entry}&P_PROGRAM=BSEE&P_SUBMIT=&P_LANG=EN&P_LEVEL=UG"
                       
                    elif category == "Core Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA=BSEE_CEL&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Free Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA=BSEE_FRE&P_PROGRAM=BSEE&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Basic Science and Engineering Courses":
                        url = f"https://mysu.sabanciuniv.edu/sr/sites/mysu.sabanciuniv.edu.sr/files/fens_course_catalog_basicscienceengineering_-_ects_okya_giden25.01.2024.pdf"


                elif major_code == "BSCS" or major_code == "BSMS" or major_code == "BSMAT" or major_code == "BSME" or major_code == "BSBIO":
                    if category == "Area Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_AEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Required Courses" or category == "University Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=TR&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={entry}"
                    elif category == "Core Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_CEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                
                    elif category == "Free Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_FEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Basic Science and Engineering Courses":
                        url = f"https://mysu.sabanciuniv.edu/sr/sites/mysu.sabanciuniv.edu.sr/files/fens_course_catalog_basicscienceengineering_-_ects_okya_giden25.01.2024.pdf"
            
                elif major_code == "BAECON"  or major_code == "BAVACD":
                    
                    #print("major code: ", major_code, "category: ", category)
                    if category == "Required Courses" or category == "University Courses" or category == "Core Course" or category == "Philosophy Requirement Course":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=EN&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={entry}"
                    elif category == "Area Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_AEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                    elif category == "Free Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_FEL&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                elif major_code == "BAMAN" or major_code == "BAPSY":
                    if category == "Required Courses" or category == "University Courses" or category == "Core Courses" or category == "Philosophy Requirement Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?P_LANG=EN&P_LEVEL=UG&P_PROGRAM={major_code}&P_SUBMIT=&SU_DEGREE_p_degree_detail%3FP_TERM={entry}"
                    elif category == "Area Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_ARE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"
                    
                    elif category == "Free Courses":
                        url = f"https://www.sabanciuniv.edu/en/prospective-students/degree-detail?SU_DEGREE.p_list_courses?P_TERM={entry}&P_AREA={major_code}_FRE&P_PROGRAM={major_code}&P_LANG=EN&P_LEVEL=UG"

                


                #print("inside try for url: ", url)
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
            
                # Find courses for the current category
                if category == "Area Courses":
                    num_columns = 5
                    #print("inside area courses: ", category)
                    rows = soup.select("td+ td")
                    data = {}
                    data_list = []
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        # print("index: ", index)
                        # print("course code: ", anchor_tag.text.strip())
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        data["course_type"] = "area"
                        # Assign names to the data elements based on their position in the row
                        if index % num_columns == 0:
                            data = {"course_code": cleaned_text}
                        elif index % num_columns == 1:
                            data["course_name"] = cleaned_text
                        elif index % num_columns == 2:
                            data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 3:
                            data["su_credits"] = int(cleaned_text)
                        elif index % num_columns == 4:
                            data["faculty_code"] = cleaned_text
                        
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    with open(json_path, "a", encoding='utf-8') as json_file:
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")

                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)

                
                #courses = soup.find_all("td", class_="")
                elif category == "Core Courses":
                    num_columns = 5
                    # print("inside core courses:", category)
                    if major_code == "BAECON" or major_code == "BAPSY" or major_code == "BAVACD":
                        rows = soup.select("tr:nth-child(17) tr td+ td")
                        # print("rows in if: ", rows)
                    else:
                        rows = soup.select("td+ td")
                    #rows = soup.select("td+ td")
                    data = {}
                    data_list = []
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        if major_code == "BAECON" or major_code == "BAPSY" or major_code == "BAVACD":
                            data["course_type"] = "core"
                            # Assign names to the data elements based on their position in the row
                            if index % num_columns == 0:
                                data = {"course_code": cleaned_text}
                            elif index % num_columns == 1:
                                data["course_name"] = cleaned_text
                            elif index % num_columns == 2:
                                data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                            elif index % num_columns == 3:
                                data["su_credits"] = int(cleaned_text)
                            elif index % num_columns == 4:
                                data["faculty_code"] = cleaned_text
                           
                        else:
                            data["course_type"] = "core"
                            # Assign names to the data elements based on their position in the row
                            if index % num_columns == 0:
                                data = {"course_code": cleaned_text}
                            elif index % num_columns == 1:
                                data["course_name"] = cleaned_text
                            elif index % num_columns == 2:
                                data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                            elif index % num_columns == 3:
                                data["su_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                            elif index % num_columns == 4:
                                data["faculty_code"] = cleaned_text
                          
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    with open(json_path, "a", encoding='utf-8') as json_file:
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")

                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)




                elif(category == "Free Courses"):
                    num_columns = 5
                    # print("inside area courses: ", category)
                    if major_code == "BAMAN":
                        rows = soup.select("thead+ tbody td")
                    else:
                        rows = soup.select("td+ td")
                    data = {}
                    data_list = []
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        data["course_type"] = "free"
                        # Assign names to the data elements based on their position in the row
                        if index % num_columns == 0:
                            data = {"course_code": cleaned_text}
                        elif index % num_columns == 1:
                            data["course_name"] = cleaned_text
                        elif index % num_columns == 2:
                            data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 3:
                            data["su_credits"] = int(cleaned_text)
                        elif index % num_columns == 4:
                            data["faculty_code"] = cleaned_text
                        data["course_time"] = []
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    with open(json_path, "a", encoding='utf-8') as json_file:
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")
                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)






                elif(category == "University Courses"):
                    num_columns = 6
                    rows = soup.select("tr:nth-child(8) tr td")
                    data = {}
                    data_list = []
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        data["course_type"] = "university"
                        # Assign names to the data elements based on their position in the row
                        if index % num_columns == 1:
                            data = {"course_code": cleaned_text}
                        elif index % num_columns == 2:
                            data["course_name"] = cleaned_text
                        elif index % num_columns == 3:
                            data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 4:
                            data["su_credits"] = int(cleaned_text)
                        elif index % num_columns == 5:
                            data["faculty_code"] = cleaned_text
                            
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    #
                    with open(json_path, "a", encoding='utf-8') as json_file:
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")
                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)





                            
                elif(category == "Required Courses"):
                    num_columns = 6
                    if major_code == "BAECON":
                        rows = soup.select("tr:nth-child(14) tr td , tr:nth-child(11) tr td")
                    else:
                        rows = soup.select("tr:nth-child(11) tr td")
                    data_list = []
                    data = {}
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        data["course_type"] = "required"
                        # Assign names to the data elements based on their position in the row
                        if index % num_columns == 1:
                            data = {"course_code": cleaned_text}
                        elif index % num_columns == 2:
                            data["course_name"] = cleaned_text
                        elif index % num_columns == 3:
                            data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 4:
                            data["su_credits"] = int(cleaned_text)
                        elif index % num_columns == 5:
                            data["faculty_code"] = cleaned_text
                        
                       
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    with open(json_path, "a", encoding='utf-8') as json_file:
                                
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")
                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)







                #print(f"Scraped data for {major_code} - {entry} - {category}")
                elif(category == "Philosophy Requirement Courses"):
                    num_columns = 5

                    rows = soup.select("tr:nth-child(14) tr:nth-child(1) td , td+ td td , tr:nth-child(14) tr td+ td")
                    data = {}
                    data_list = []
                    for index, anchor_tag in enumerate(rows):
                        # Clean the data by removing asterisks
                        cleaned_text = anchor_tag.text.strip().replace('*', '')
                        data["course_type"] = "philosophy"
                        # Assign names to the data elements based on their position in the row
                        if index % num_columns == 0:
                            data = {"course_code": cleaned_text}
                        elif index % num_columns == 1:
                            data["course_name"] = cleaned_text
                        elif index % num_columns == 2:
                            data["ects_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 3:
                            data["su_credits"] = int(cleaned_text) if cleaned_text.isdigit() else cleaned_text
                        elif index % num_columns == 4:
                            data["faculty_code"] = cleaned_text
                        
                        # Check if the index is divisible by the number of columns (to identify the end of a row)
                        if (index + 1) % num_columns == 0:
                            data_list.append(data)
                            # If it's the end of a row, write the data to the JSON file
                    with open(json_path, "a", encoding='utf-8') as json_file:
                        json.dump(data_list, json_file, indent=4, ensure_ascii=False)
                        if index < len(rows) - 1:
                            json_file.write(",")
                            json_file.write("\n")  # Write a newline character after each JSON object

                    # Add a newline character to separate different sections in the JSON file
                    with open(json_path, "a") as json_file:
                        json_file.write("\n")
                    for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)




                elif(category == "Basic Science and Engineering Courses"):
                    response = requests.get(url)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        # Open the PDF file in read-binary mode
                        with open("fens_course_catalog.pdf", "wb") as file:
                            # Write the content of the response (the PDF file) to the local file
                            file.write(response.content)
                        
                        # Read tables from the PDF file
                        tables = tabula.read_pdf("fens_course_catalog.pdf", pages="all", multiple_tables=True)
                        
                        df = tables[0] # the first table
                        df1 = tables[1] # the second table
                        df1 = df1.iloc[1:]
                        df2 = tables[2] # the third table
                        df2 = df2.iloc[1:]
                        df3 = tables[3] # the fourth table
                        df3 = df3.iloc[1:]
                        # with open("out.txt", "a") as text_file:
                        #     text_file.write(str(df1))
                        #     text_file.write("\n")  # Write a newline character after each JSON object

                        course_codes = df.iloc[:, 0].tolist()
                        #print("course codes: ", course_codes)
                        # Create a list of dictionaries with "course_code" as the key
                        data = []
                        data1 = []
                        data2 = []
                        data3 = []
                        for code in course_codes[9:]: # Skipping the first 9 course codes
                            
                            #  print("code: ", code)
                             course_info = code.split()
                             course_info = course_info[2:]
                             #print("course info before: ", course_info)
                             if 'FENS' in course_info:
                                 fens_index = course_info.index('FENS')
                                 #print("fens index: ", fens_index)   
                                 merged_info = ' '.join(course_info[1:fens_index])
                                 course_info[1:fens_index] = [merged_info]
                                 del course_info[3]
                                 del course_info[5:]
                                 #print("course info after: ", course_info)
                                 if len(course_info) == 5:
                                    match = re.search(r'\d', course_info[0])
                                    first_digit_index = match.start()
                                    # Insert a space just before the first digit
                                    modified_course_code = course_info[0][:first_digit_index] + " " + course_info[0][first_digit_index:]
                                    engineering_credits = int(course_info[3].split(',')[0])
                                    science_credits = int(course_info[4].split(',')[0])
                                    data.append({
                                    
                                         "course_code": modified_course_code,
                                         "course_type": "science_engineering",
                                         "course_name": course_info[1],
                                         
                                         "engineering_credits": engineering_credits,
                                         "science_credits": science_credits,
                                         "faculty_code": course_info[2]
                     })
                        for index, row in df1.iterrows():
                            #print("Row:", row)
                            match = re.search(r'\d', row[2])
                            first_digit_index = match.start()
                            modified_course_code = row[2][:first_digit_index] + " " + row[2][first_digit_index:]
                            engineering_credits = int(row[6].split(',')[0])
                            science_credits = int(row[7].split(',')[0])
                            data1.append({
                               
                                "course_code": modified_course_code, 
                                "course_type": "science_engineering",
                                "course_name": row[3],
                               
                                "engineering_credits": engineering_credits,
                                "science_credits": science_credits,
                                "faculty_code": row[4]
                            })

                        for index, row in df2.iterrows():
                                match = re.search(r'\d', row[2])
                                first_digit_index = match.start()
                                modified_course_code = row[2][:first_digit_index] + " " + row[2][first_digit_index:]
                                engineering_credits = int(row[6].split(',')[0])
                                science_credits = int(row[7].split(',')[0])
                                #print("Row:", row)
                                data2.append({
                                    "course_code": modified_course_code, 
                                     "course_type": "science_engineering",
                                    "course_name": row[3],
                                   
                                    "engineering_credits":engineering_credits,
                                    "science_credits": science_credits,
                                    "faculty_code": row[4]
                                })
                              
                        for index, row in df3.iterrows():
                                    match = re.search(r'\d', row[2])
                                    first_digit_index = match.start()
                                    modified_course_code = row[2][:first_digit_index] + " " + row[2][first_digit_index:]
                                    #print("Row:", row)
                                    engineering_credits = int(row[6].split(',')[0])
                                    science_credits = int(row[7].split(',')[0])
                                    data3.append({
                                        
                                        "course_code": modified_course_code, 
                                        "course_type": "science_engineering",
                                        "course_name": row[3],
                                        "engineering_credits": engineering_credits,
                                        "science_credits": science_credits,
                                        "faculty_code": row[4]
                                    })
                            
                        #print("data1: ", data1)
                        merged_data = data + data1 + data2 + data3
                    
                        with open(json_path, "a", encoding='utf-8') as json_file:
                            
                            json.dump(merged_data, json_file, indent=4, ensure_ascii=False)
                            # Check if merged_data is not empty
                            if merged_data:
                                #json_file.write(",")  # Write comma only if merged_data is not empty
                                json_file.write("\n")  # Write a newline character after the list




                    # Add a newline character to separate different sections in the JSON file
                        with open(json_path, "a") as json_file:
                            json_file.write("\n")
                        for course_name, course_info in course_mapping.items():
                            for section, section_info in course_info['sections'].items():
                                times = section_info['times']
                                #print("course_name:", course_name, "section:", section, "times:", times)
                                search_course_code_and_update(course_name, times, section, json_path)
                                search_course_for_preq(json_path)





                    else:
                        print("Failed to download the PDF:", response.status_code)





            except requests.exceptions.RequestException as e:
                print(f"Error scraping data for {major_code} - {entry} - {category}: {e}")



def search_course_code_and_update(course_code, course_time, course_section, file_path):
    # Check if the file path exists
    if os.path.exists(file_path):
        # Open and load the JSON file
        with open(file_path, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Flag to check if the course code is found
            course_found = False
            # Iterate through each entry in the JSON data
            for entry in data:
                entry["condition"] = {"prerequisite": [], "general": []}    
                # Check if sections is an array, if not initialize it as an empty list
                if not isinstance(entry.get("sections"), list):
                    entry["sections"] = []
                # Check if the course code matches
                if entry["course_code"] == course_code:
                    print(f"Course code {course_code} found in file: {file_path}")
                    print("Updating course_time field...")
                    # Check if the section already exists
                    section_dict = next((section for section in entry["sections"] if section.get("section") == course_section), None)
                    if section_dict is None:
                        # If the section does not exist, create a new section dictionary
                        section_dict = {"section": course_section, "times": []}
                        entry["sections"].append(section_dict)
                        entry["condition"] = {"prerequisite": [], "general": []}    
                    # Append course_time to the times list in the section dictionary
                    section_dict["times"].append(course_time)
                    # Set flag to True since course code is found

            # Rewrite the updated JSON data to the file
            with open(file_path, "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print("Course time updated successfully.")
    else:
        print(f"File not found: {file_path}")

def search_course_for_preq(file_path):
    # Check if the file path exists
    if os.path.exists(file_path):
        # Open and load the JSON file
        with open(file_path, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Open and load the SuGrad.CourseInfo.json file
        with open("SuGrad.CourseInfo.json", "r", encoding='utf-8') as req_file:
            req_data = json.load(req_file)
        
        # Initialize a list to store conditions for each course
        course_conditions = []
        for course in req_data:
            course_conditions.append(course["condition"].copy())  # Store condition for each course
        
        # Iterate over entries in data and update conditions based on matching course_code
        for entry in data:
            # Check if entry's course_code matches any course in req_data
            course_found = False
            for course, condition in zip(req_data, course_conditions):
                if entry.get("course_code") == course["course_code"]:
                    # Update the condition dictionary entirely
                    entry["condition"] = condition.copy()
                    course_found = True
                    break
            
            # If entry's course_code doesn't match any course, set default condition
            if not course_found:
                entry["condition"] = {"prerequisite": [], "general": []}
        
        # Write updated data back to the file_path
        with open(file_path, "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            print("Course time updated successfully.")
    else:
        print(f"File not found: {file_path}")





if __name__ == "__main__":
    main()


