from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # Set up the WebDriver for Edge
    edge_service = Service(executable_path="C:/Users/ProDesk/OneDrive/Desktop/drivers/msedgedriver.exe")
    options = Options()
    driver = webdriver.Edge(service=edge_service, options=options)

    # Open eBay signup page
    driver.get("https://signup.ebay.com/pa/crte?ru=https%3A%2F%2Fwww.ebay.com%2F%3Fmsockid%3D39174f64769f6feb2a335c6877686e2a")

    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)

    first_name_input = wait.until(EC.presence_of_element_located((By.ID, 'firstname')))
    first_name_input.send_keys('Aashitha')

    last_name_input = wait.until(EC.presence_of_element_located((By.ID, 'lastname')))
    last_name_input.send_keys('Rai')

    email_input = wait.until(EC.presence_of_element_located((By.ID, 'Email')))
    email_input.send_keys('deeksh10ramesh@gmail.com')

    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_input.send_keys('deeksh10ramesh@gmail.com')

    business_name_input = wait.until(EC.presence_of_element_located((By.ID, 'businessName')))
    business_name_input.send_keys('Samsung')

    business_email_input = wait.until(EC.presence_of_element_located((By.ID, 'businessEmail')))
    business_email_input.send_keys('Samsung@gamil.com')

    business_password_input = wait.until(EC.presence_of_element_located((By.ID, 'bizPassword')))
    business_password_input.send_keys('samsung')

    business_country_input = wait.until(EC.presence_of_element_located((By.ID, 'businessCountry')))
    business_country_input.send_keys('India')
    # Wait for user input to keep the browser open
    input("Press Enter to close the browser and end the script...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after user input
    driver.quit()