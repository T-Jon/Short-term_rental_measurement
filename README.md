# Property Scraper

This Python script automates the process of scraping property listings from a specified webpage using Selenium and BeautifulSoup. 
It's designed to navigate through the listings, extract relevant information, and save the data to a CSV file for further analysis.

## Background
**Areas of Focus**
- Location: Sandpoint, ID
- Website: Expidia.com
- Accomodation Filters: 2 people, Flexible nights stay between 2-3 nights
- Includes Guest Satisfaction scores

## Setup Instructions
### WebDriver Setup
This script uses Selenium, which requires a WebDriver to interface with the chosen browser. 
Make sure you have the WebDriver for your browser of choice installed and correctly placed.
After downloading, extract the executable and place it in a known location on your system.

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
