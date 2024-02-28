# Property Scraper

This Python script automates the process of scraping property listings from a specified webpage using Selenium and BeautifulSoup. 
It's designed to navigate through the listings, extract selected relevant information, and save the data to a CSV file for further analysis.
This Python script is built to lightly interact and gather details from a popular hotel and short-term rental platform. 
Programmatically running this script will be flagged by the site as bot activity as a violation of site usage outlined in the robot.txt use guidelines.

## Background

### Areas of Focus
- Location: Sandpoint, ID
- Website (link to robot.txt file): [Expidia.com](https://www.expedia.com/robots.txt)
- Accommodation Filters: 2 people, Flexible nights stay between 2-3 nights
- Includes: Property Titles, Hot Tub status, Property Type, Property Details like quantity of beds, Guest Satisfaction scores, List Price, Taxes & Fees, Etc.

## Setup Instructions

### WebDriver Setup
This script uses Selenium, which requires a WebDriver to interface with the chosen browser. 
Make sure you have a WebDriver for your browser of choice installed and correctly placed.
After downloading, extract the executable and place it in a known location on your system. This PATH must be entered where noted in the script.

### Running the Script
1. Open the PropertyScraper.py file with your favorite text editor.
2. Modify the base_url, driver_path, start_date, and end_date variables in the __main__ section to fit your scraping needs.
3. Save your changes and close the editor.
4. Run the script from your terminal:

python ExPropertyScraper.py

The script will start, navigate to the specified URL, and begin the scraping process. 
Once completed, the extracted data will be saved in a CSV file in the same directory as the script.

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installing Dependencies

1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### License

This project is open source and available under the MIT License.

