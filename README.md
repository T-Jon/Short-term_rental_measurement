# Short-Term Rental Property Scraper

## Project Overview and Purpose

This project introduces a Python-based automation tool developed to enhance data collection processes for short-term rental analysis. Leveraging the capabilities of Selenium and BeautifulSoup, the script is meticulously engineered to navigate and extract local information from property listings on a renowned hotel and short-term rental platform. It systematically captures selected data points, facilitating their aggregation into a CSV file for comprehensive analysis. This initiative not only serves to augment previously acquired data from a subscription measurement platform called AirDNA, enriching insights for my short-term rental venture initiated in 2022, but also marks a pivotal step in my career transition towards data analytics.

Embarking on this project was driven by a dual-purpose objective: to practically apply and deepen my Python programming skills and to derive actionable insights to optimize the performance of my rental property. It's noteworthy that while the script operates efficiently to simulate user interactions on the target website, it respects ethical considerations and compliance with digital conduct, acknowledging potential limitations posed by the site's robots.txt guidelines.

As my inaugural Python project, it reflects a rigorous learning journey and my commitment to leveraging technology for data-driven decision-making. Through this endeavor, I aim to showcase my growing proficiency in coding and data analytics, aspiring to contribute meaningfully in a professional setting.

## Areas of Focus
- **Location:** Sandpoint, ID
- **Website (link to robot.txt file):** [Expidia.com](https://www.expedia.com/robots.txt)
- **Accommodation Filters:** 2 people, Flexible nights stay between 2-3 nights
- **Includes:** Property Titles, Hot Tub status, Property Type, Property Details like quantity of beds, Guest Satisfaction scores, List Price, Taxes & Fees, Etc.

## Setup Instructions

### WebDriver Setup
This script uses Selenium, which requires a WebDriver to interface with the chosen browser. 
Make sure you have a WebDriver for your browser of choice installed and correctly placed.
After downloading, extract the executable and place it in a known location on your system. This PATH must be entered where noted in the script.

### Running the Script
1. Open the ExPropertyScraper.py file with your favorite text editor.
2. Modify the base_url, driver_path, start_date, and end_date variables in the __main__ section to fit your scraping needs.
3. Save your changes and close the editor.
4. Run the script from your terminal:

python ExPropertyScraper.py

The script will start, navigate to the specified URL, and begin the scraping process. 
Once completed, the extracted data will be saved in a CSV file in the same directory as the script.

## Configuration Options, considerations and limitations
- Base URL, Driver PATH, and Date ranges are adjustable. Please refer to "Running the Script."
- Setting up the WebDriver is built to accommodate various approaches. At this time it is "basic" (aka only in Incognito mode) but can be altered further.
  - Other driver options available:
    - Can be run headless. With sub-options to control window size, & disable GPU.
      - At this time it will run non-headless so as to allow the user to monitor the functionality visually. 
    - Can be set to adjust or simply log Device User Agent string.
    - Can be set to disable webpage extensions.
    - Can be set to not run in Sandbox environment.   
- Other aspects or area of focus can be manually changed through the aspects in the Base URL.
- Data collection horizon is 6 months. This is due to how the site is able to present data but also due to expected accurate data horizons.
- This project is a work in progress:
  - Engaging with the "Show More" button functions intermittently at this time.
    - This is currently limiting results to 100 rows of data. Area of focus is a small market and so this has not been too inhibitive. 
    - Theory: I believe this is due to how the script uses the "Smart Scroll" functionality and how the script engages with the page before the button can become "clickable"


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

