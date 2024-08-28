from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Specify the path to your Edge WebDriver
msedgedriver_path = r"C:\SeleniumDrivers\msedgedriver.exe"  # Update with your path to msedgedriver

# Set up options for Edge
options = Options()
options.use_chromium = True  # Ensure compatibility with Chromium-based Edge

# Set up the Selenium WebDriver using Edge
service = Service(msedgedriver_path)
driver = webdriver.Edge(service=service, options=options)

# Function to extract company details from LinkedIn company page
def get_company_details(company_linkedin):
    driver.get(company_linkedin)
    time.sleep(3)  # Wait for the page to load

    # Close login pop-up if it appears
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Dismiss"]'))
        )
        close_button.click()
        time.sleep(1)  # Wait briefly after closing the pop-up
    except Exception as e:
        print("No login pop-up found or unable to close it.")

    # Extract company name
    try:
        company_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(@class, "top-card-layout__title")]'))
        ).text.strip()
    except Exception as e:
        print(f"Error extracting company name: {e}")
        company_name = 'Not found'
    
    # Extract company website link
    try:
        website_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(@data-tracking-control-name, "about_website")]'))
        )
        # Get the href attribute from the anchor element
        redirect_url = website_section.get_attribute('href')
        # Navigate to the redirect URL to get the final link
        driver.get(redirect_url)
        time.sleep(3)  # Wait for the redirected page to load
        # Get the final URL
        company_website = driver.current_url
    except Exception as e:
        print(f"Error extracting company website: {e}")
        company_website = 'Not found'
    
    return company_name, company_website

# Example list of company LinkedIn links
company_links = [
    "https://sg.linkedin.com/company/amore-fitness?trk=public_jobs_topcard-org-name",
    "https://www.linkedin.com/company/duetto-research?trk=public_jobs_topcard-org-name",
]

# Data collection
company_data = []
for link in company_links:
    company_name, company_website = get_company_details(link)
    company_data.append({'Company Name': company_name, 'Company Website': company_website})

# Save to CSV
df = pd.DataFrame(company_data)
df.to_csv('company_details.csv', index=False)

# Close the driver
driver.quit()

print("Data scraping complete! Check the 'company_details.csv' file.")
