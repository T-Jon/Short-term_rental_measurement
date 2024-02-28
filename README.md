# Property Scraper

This project introduces a Python-based automation tool developed to enhance data collection processes for short-term rental analysis. Leveraging the capabilities of Selenium and BeautifulSoup, the script is meticulously engineered to navigate and extract crucial information from property listings on a renowned hotel and short-term rental platform. It systematically captures selected data points, facilitating their aggregation into a CSV file for comprehensive analysis. This initiative not only serves to augment previously acquired data from AirDNA, enriching insights for my short-term rental venture initiated over a year ago, but also marks a pivotal step in my career transition towards data analytics.

Embarking on this project was driven by a dual-purpose objective: to practically apply and deepen my Python programming skills and to derive actionable insights to optimize the performance of my rental property. It's noteworthy that while the script operates efficiently to simulate user interactions on the target website, it respects ethical considerations and compliance with digital conduct, acknowledging potential limitations posed by the site's robots.txt guidelines.

As my inaugural Python project, it reflects a rigorous learning journey and my commitment to leveraging technology for data-driven decision-making. Through this endeavor, I aim to showcase my growing proficiency in coding and data analytics, aspiring to contribute meaningfully in a professional setting.

## Background

### Areas of Focus
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

