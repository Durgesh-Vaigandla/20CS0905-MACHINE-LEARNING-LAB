from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
# and specify the path to your ChromeDriver
chromedriver_path = r"C:\path\to\chromedriver.exe"  # Update with your path to chromedriver

# Set up options for Chrome
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Set up the Selenium WebDriver using Chrome
service = Service(chromedriver_path)

print(f"Attempting to start Chrome")
print(f"Using chromedriver at: {chromedriver_path}")

try:
    driver = webdriver.Chrome(service=service, options=options)
    print("Chrome browser started successfully")
    
    # Navigate to a simple webpage
    driver.get("https://www.example.com")
    print(f"Navigated to example.com. Current URL: {driver.current_url}")
    
    # Wait for and print the title of the page
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text
    print(f"Page title: {title}")
    
    # Wait for a moment
    time.sleep(5)
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    if 'driver' in locals():
        driver.quit()
        print("Browser closed.")

print("Test script execution completed.")