from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random
import logging
import re

# Initializes logging with a specific format for timestamp, log level, and message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PropertyScraper:
    def __init__(self, base_url, driver_path, start_date, end_date):
        """
        Initializes the PropertyScraper with base URL, path to the Chrome WebDriver, 
        and date range for the search.
        Args:
            - base_url (str): The base URL for the scraping.
            - driver_path (str): The file path to the Chrome WebDriver.
            - start_date (str): The start date for the search range.
            - end_date (str): The end date for the search range.
        """
        self.base_url = base_url
        self.driver_path = driver_path
        self.start_date = start_date
        self.end_date = end_date
        self.properties = []


    def construct_url(self):
        """
        Construct the URL with dynamic date ranges for search.
        Returns:
            str: The constructed URL with the search range included.        
        """
        return f"{self.base_url}&searchRange={self.start_date}_{self.end_date}"


    def setup_driver(self):
        """
        Sets up the Selenium WebDriver with Chrome options for scraping.
        """
        try:
            service_obj = Service(self.driver_path)  # initializes a 'Service' object from the Selenium library.
            options = webdriver.ChromeOptions()  # setup for Chrome options.

            # options.add_argument('--no-sandbox') #Disables security feature or sandbox.

            # ***Check and log the current User_Agent being used by the WebDriver. 
            # For testing purposes to pull and log the Device User Agent.
            # user_agent = self.driver.execute_script("return navigator.userAgent;")
            # logging.info(f"Current User Agent: {user_agent}")

            # *** Option to hard-code UA string.
            # options.add_argument(user-agent=replace_with_desired_UA)

            # *** Option to run in headless mode. Un-comment the below lines to run headless.
            # options.add_argument('--headless')
            # options.add_argument('--window-size=1920,1080') #makes sure the headless window is sized appropriately
            # options.add_argument('--disable-gpu') #disables GPU hardware acceleration. 
            # Disabling GPU is useful for running in headless mode as no graphic processing is needed.

            # ***Disable Extentions. This prevents any installed extensions from affecting scraping.
            # options.add_argument('--disable-extensions')

            options.add_argument('--incognito')
            self.driver = webdriver.Chrome(service=service_obj, options=options)
        except Exception as e:
            logging.error(f"Failed to initialize WebDriver: {e}")
            exit(1)           


    def navigate_to_url(self, url):
        """
        Navigates to a URL using the WebDriver.
        """
        try:
            self.driver.get(url)
            logging.info(f"Successfully navigated to {url}")
        except Exception as e:
            logging.error(f"Failed to navigate to {url}: {e}")
            return False  
        return True 


    def random_sleep(self, min_seconds=4, max_seconds=8):
        """ 
        'Random_sleep' pauses execution for a random interval between "min_seconds" and "max_seconds" (Adjustable)
        This is for mimicking human behavior and to avoid detection by any anti-scraping mechanisms.
        """
        time.sleep(random.uniform(min_seconds, max_seconds))


    def smart_scroll(self):
        """ 
        'Smart_Scroll' scrolls down the page, pausing between scrolls, to ensure that dynamic content is loaded.
        This is built for websites that load more content as the user scrolls down the page.
        """
        max_scroll_pause = 8  # Max pause time in seconds
        min_scroll_pause = 3  # Min pause time in seconds
        max_scroll_height = 600  # Max scroll distance in pixels (FYI 600 pixels @96 PPI is approx 6 1/4")
        min_scroll_height = 300  # Min scroll distance in pixels
        attempts = 0  # Initialize an attempt counter to track consecutive attempts without new content being loaded.
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")  # Record the initial height of the webpage.

        while True:
            # Calculate a random scroll distance within the specified range and a random pause time.
            scroll_distance = random.randint(min_scroll_height, max_scroll_height)
            pause_time = random.uniform(min_scroll_pause, max_scroll_pause)

            # Scroll the page by the determined distance.
            self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            time.sleep(pause_time)  # Pause for the randomly determined duration.

            # Check the new height of the webpage after scrolling.
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # If the new height matches the last recorded height, it may indicate the bottom of the page has been reached.
            if new_height == last_height:
                attempts += 1  # Increment the attempt counter since no new content was loaded.
                if attempts >= 3:  # After X attempts, consider that we've reached the bottom
                    break
            else:
                attempts = 0  # Reset attempts counter if we successfully scrolled further
            last_height = new_height  # Update the last recorded height with the new height for the next iteration.


    def click_show_more_multiple_times(self, times=2):
        """
        Click the 'Show More' button specified number of times=X. 
        """
        for _ in range(times):
            # Random sleep before attempting to click to simulate natural user pause
            # Adjust these values based on page response time and expected user behavior
            self.random_sleep(5, 10)  # Waits between (A,B) in seconds
            try:
                # Wait up to 10 (or "B" above) seconds for the 'Show More' button to become clickable
                # This wait time can be adjusted based on observed network speed and server response time
                show_more_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-stid='show-more-results']"))
                )
                show_more_button.click()
                logging.warning("Clicked 'Show More' button.")
                # Wait for page to indicate it has fully loaded after clicking 'Show More'
                # This ensures that any dynamic content loaded as a result of the click has been rendered
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.execute_script("return document.readyState") == "complete"
                )
                # Perform a smart scroll and random sleep after each click to mimic human interaction
                self.smart_scroll()
                # Random sleep after click to simulate reading or viewing the loaded content
                # Adjust these intervals based on the amount of content typically loaded and user engagement time
                self.random_sleep(2, 5)  ## Waits between (A,B) seconds after scrolling and content load
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
                logging.warning(f"Could not click 'Show More' or no more content to load: {e}")
                break  # Exit if button cannot be clicked or is not found


    def has_hot_tub_features(self, title, offering, accommodation, location):
        # Combine all the relevant fields into a single string
        combined_text = " ".join([title, offering, accommodation, location]).lower()
        # Define keywords to search for
        keywords = ['hot tub', 'hottub', 'pool', 'hotel']
        # Check if any keyword is in the combined text
        return any(keyword in combined_text for keyword in keywords)


    def categorize_property_type(self, title):
        """
        Property Catigorization function for use in bucketing properties according to local groupings.
        """
        title_lower = title.lower()  # Convert to lowercase to make search case-insensitive
        keywords_to_category = {
            "waterfront": "Lakefront",
            "water front": "Lakefront",
            "lakefront": "Lakefront",
            "lake front": "Lakefront",
            "downtown": "DownTown",
            "down town": "DownTown",
            "hotel": "Hotel",
            "schweitzer": "Schweitzer",
            "cabin": "Cabin",
            "cottage": "Cabin",
            "ski-in": "Schweitzer",
            "resort": "Hotel",
            "lakeside": "Lakefront",
            "beach": "Lakefront"
        }
        for keyword, category in keywords_to_category.items():
            if keyword in title_lower:
                return category
        return "Other"


    def scrape_properties(self):
        """
        Main method to scrape properties from the website.
        """
        self.setup_driver()
        url = self.construct_url()
        if not self.navigate_to_url(url):
            logging.error("Failed to load the URL. Exiting...")
            self.driver.quit()
            return 
        logging.info(f"Accessing URL: {url}")
        self.random_sleep(6, 12)
        self.smart_scroll()
        self.click_show_more_multiple_times()
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        for container in soup.select('div.uitk-layout-flex.uitk-layout-flex-block-size-full-size'):

            title = container.find('h3', class_='uitk-heading').get_text(strip=True) if container.find('h3',
                                                                            class_='uitk-heading') else 'N/A'
            subheadings = container.find_all('div', class_='uitk-text')
            subheadings_texts = [sub.get_text(strip=True) for sub in subheadings[:3]]

            rating_score = container.find('span', class_='uitk-badge-base-text').get_text(strip=True) if container.find(
                'span', class_='uitk-badge-base-text') else 'N/A'
            rating_level = container.find('div', string=re.compile('Exceptional|Very Good|Good|Fair|Poor')).get_text(
                strip=True) if container.find('div',
                                              string=re.compile('Exceptional|Very Good|Good|Fair|Poor')) else 'N/A'

            property_type = self.categorize_property_type(title)

            hot_tub_present = self.has_hot_tub_features(
                title=title,
                offering=subheadings_texts[0] if len(subheadings_texts) > 0 else 'N/A',
                accommodation=subheadings_texts[1] if len(subheadings_texts) > 1 else 'N/A',
                location=subheadings_texts[2] if len(subheadings_texts) > 2 else 'N/A'
            )

            total_ratings_element = container.find('div', string=re.compile(r'\d+\sreviews'))

            quantity_of_reviews = re.search(r'\d+', total_ratings_element.get_text(strip=True)).group(
                0) if total_ratings_element else 'N/A'

            stay_dates_div = container.find('div',
                    class_='uitk-text uitk-type-end uitk-type-300 uitk-type-bold uitk-text-default-theme')
            stay_dates = stay_dates_div.get_text(strip=True) if stay_dates_div else 'N/A'

            nights_stayed = 0
            if stay_dates != 'N/A':
                dates = stay_dates.split(' - ')
                try:
                    start_date = datetime.strptime(dates[0], '%a, %b %d').replace(year=datetime.now().year)
                    end_date = datetime.strptime(dates[1], '%a, %b %d').replace(year=datetime.now().year)
                    if end_date < start_date:
                        end_date = end_date.replace(year=start_date.year + 1)
                    nights_stayed = (end_date - start_date).days
                except ValueError as e:
                    logging.error(f"Error parsing dates: {e}")
                    nights_stayed = 0  # 'Error parsing dates'

            accommodation_info = subheadings_texts[1] if len(subheadings_texts) > 1 else 'N/A'

            sleeps_match = re.search(r'Sleeps (\d+)', accommodation_info)
            sleeps = sleeps_match.group(1) if sleeps_match else '2'

            bedrooms_match = re.search(r'(\d+) bedroom(?:s)?', accommodation_info)
            bedrooms = bedrooms_match.group(1) if bedrooms_match else '1'

            price_text = container.find('div',
                            class_='uitk-text uitk-type-300 uitk-text-default-theme is-visually-hidden').get_text(
                strip=True) if container.find('div',
                            class_='uitk-text uitk-type-300 uitk-text-default-theme is-visually-hidden') else 'N/A'
            total_price_text = container.find('div',
                            class_='uitk-text uitk-type-end uitk-type-200 uitk-text-default-theme').get_text(
                strip=True) if container.find('div',
                            class_='uitk-text uitk-type-end uitk-type-200 uitk-text-default-theme') else 'N/A'
            price = int(re.sub(r'[^\d]', '', price_text)) if re.search(r'\$\d+', price_text) else 0
            total_price = int(re.sub(r'[^\d]', '', total_price_text)) if re.search(r'\$[\d,]+', 
                                                                                   total_price_text) else 0
            daily_rate_w_tf = total_price / nights_stayed if nights_stayed > 0 else 0
            taxes_fees_per_day = daily_rate_w_tf - price if price > 0 else 0
            tf_as_percent_of_daily_price = (taxes_fees_per_day / price) if price > 0 else 0

            if (title != 'N/A' or any(text != 'N/A' for text in subheadings_texts)) and (
                    price > 0 or total_price > 0 or nights_stayed > 0):
                self.properties.append({
                    'Property Title': title,
                    'Hot Tub': hot_tub_present,
                    'Property Type': property_type,
                    'Property Offering': subheadings_texts[0] if len(subheadings_texts) > 0 else 'N/A',
                    'Accommodation': accommodation_info,
                    'Sleeps': sleeps,
                    'Bedrooms': bedrooms,
                    'Location': subheadings_texts[2] if len(subheadings_texts) > 2 else 'N/A',
                    'Rating Score': rating_score,
                    'Rating Level': rating_level,
                    'Quantity of Reviews': quantity_of_reviews,
                    'Price': price,
                    'Total Price': total_price,
                    'Suggested Stay Dates': stay_dates,
                    'Nights Stayed': nights_stayed,
                    'Daily Rate w/T&F': round(daily_rate_w_tf, 2),
                    'Taxes & Fees per Day': round(taxes_fees_per_day, 2),
                    'T&F as a % of Listed Daily Price': round(tf_as_percent_of_daily_price, 2)
                })

        self.driver.quit()


    def save_to_csv(self):
        """
        Converts the list of dictionaries into a pandas DataFrame and saves it as a .csv file.
        Filters out entries where all fields are N/A.
        Adds a timestamp factor to the file names to help with multiple runs.
        """
        try:
            df = pd.DataFrame(self.properties)
            if not df.empty:
                df = df[(df != 'N/A').any(axis=1)]
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"EX_hotels_data_{timestamp}.csv"
                df.to_csv(filename, index=False)
                logging.info(f"Data saved to {filename}")
            else:
                logging.warning("DataFrame is empty. No data to save.")
        except Exception as e:
            logging.error(f"Failed to save data to CSV: {e}")



if __name__ == "__main__":
    base_url = (
        "https://www.{travel_site_base_URL}.com/Hotel-Search?"
        "adults=2&"
        "destination=Sandpoint%2C%20Idaho%2C%20United%20States%20of%20America&"
        "flexibility=2_DAY_LOWER&"
        "flexibility=3_DAY_UPPER&"
        "latLong=48.276577%2C-116.553467&"
        "regionId=9756&"
        "rooms=1&"
        "semdtl=&"
        "sort=RECOMMENDED&"
        "theme=&"
        "useRewards=false&"
        "userIntent="
    )
    driver_path = "C:\\Windows\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    start_date = "2024-05-01"
    end_date = "2024-05-31"
    scraper = PropertyScraper(base_url, driver_path, start_date, end_date)
    scraper.scrape_properties()
    scraper.save_to_csv()
