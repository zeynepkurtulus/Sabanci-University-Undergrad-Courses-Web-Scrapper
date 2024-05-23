This project is a Python-based web scraper designed to extract course data from the Sabanci University website and Suchedule website and save it in JSON format. The scraper handles multiple faculties and majors, organizing the data by course type. It also integrates prerequisite information into the course data.

Features

Web Scraping: Uses BeautifulSoup and Selenium to scrape course information from the Sabanci University website.
Data Storage: Saves scraped data in structured JSON format.
Course Mapping: Maps detailed course information including course codes, names, credits, faculty codes, and sections.
PDF Data Extraction: Extracts data from PDF files using tabula.
Prerequisite Integration: Updates course data with prerequisite information from an additional JSON file.

Important Notes

The script handles different faculties and majors, constructing appropriate URLs for each course type.
Data is saved in a structured JSON format, with separate folders for different categories of courses.
Prerequisite information is extracted from an additional JSON file (SuGrad.CourseInfo.json) and integrated into the course data.
