from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import ChromeOptions

# URL of the StubHub checkout page
checkout_url = 'https://www.stubhub.com/p-nk-arlington-tickets-9-29-2023/event/151219653/?quantity=2'

# Start purchase time (adjust this to your desired purchase time)
purchase_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)  # For 10:00:00 AM

# Calculate the time to wait in seconds until the purchase time
wait_time = (purchase_time - datetime.now()).total_seconds()

# Wait until the specified purchase time
if wait_time > 0:
    print(f"Waiting for {wait_time} seconds until 10:00:00 AM...")
    time.sleep(wait_time)

# Configure Chrome options
chrome_options = Options()

# Disable the "chrome is being controlled by automated test software" message
chrome_options.add_argument("disable-infobars")

# Open the browser (Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the StubHub checkout URL
driver.get(checkout_url)

# Wait for the page to load (you can adjust the time based on your internet speed)
time.sleep(5)

# Inpsecting checkout page and checking out
quantity_field = driver.find_element(By.NAME, 'quantity')
quantity_field.clear()
quantity_field.send_keys('2')

# Example -- Fill out other necessary information (adjust for your info and edit to fit ticket page)
driver.find_element(By.NAME, 'name').send_keys('Your Name')
driver.find_element(By.NAME, 'email').send_keys('Your Email')
driver.find_element(By.NAME, 'creditCardNumber').send_keys('Your Credit Card Number')
driver.find_element(By.NAME, 'expirationMonth').send_keys('MM')
driver.find_element(By.NAME, 'expirationYear').send_keys('YYYY')
driver.find_element(By.NAME, 'cvv').send_keys('CVV')

# Example -- Click the "Continue or Next" button to proceed 
driver.find_element(By.NAME, 'continueButton').click()

# Checking if it worked.
success_indicator = driver.find_element(By.ID, 'successMessage')  # Example locator for success message

if success_indicator and "Ticket purchased successfully" in success_indicator.text:
    print("Ticket bought successfully!")
else:
    print("Error: Ticket not purchased")

# Close the browser when you're done
driver.quit()

