**Game Time Scraper for HowLongToBeat.com**

**Overview**
This project is a Python script that scrapes HowLongToBeat.com to extract the playtime information for various video games. The script retrieves hours needed to beat each game in four different categories and stores the collected data in an Excel file. This project provides a practical solution for gamers looking to manage and track their gaming backlog effectively.

**File
main.py**

This script performs the following tasks:

**User Input**: Prompts the user to enter the game name and the corresponding page number from HowLongToBeat.com.
**Web Scraping**: Uses requests and BeautifulSoup to scrape the playtime information from the specified URL.
**Data Extraction**: Parses the HTML content to find the playtime for four categories: Main Story, Main + Sides, Completionist, and All Styles.
**Data Processing**: Converts the scraped time values to floats, handles fractional times, and accumulates the total playtime for each category.
**Excel Export**: Stores the collected data in a pandas DataFrame and exports it to an Excel file named BackLog.xlsx.

**How to Run**
**Install Dependencies**:
pip install requests pandas beautifulsoup4 openpyxl

**Run the Script**:
python main.py

**What I Learned**
**Web Scraping**: Gained experience with web scraping using requests and BeautifulSoup, learning how to handle HTML content and extract specific data.
**Data Processing**: Enhanced my skills in data manipulation with Python, including converting string values to floats and handling fractional numbers.
**Automation**: Learned how to automate the process of collecting and storing data, making it easier to manage and track gaming progress.
**Excel Integration**: Used pandas to create and export DataFrames to Excel, providing a structured and easily accessible format for the scraped data.
