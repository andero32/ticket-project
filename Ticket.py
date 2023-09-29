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

# Close the browser
driver.quit()

#Navigate to the checkout page URL

#Generic editable part that IDK how to do, the actual checkout and buying process

#use Selenium to interact with elements on the page, fill out forms, click buttons, etc.


#Example idk:
#driver.find_element_by_id('input_field_id').send_keys('your_data')
#driver.find_element_by_id('submit_button_id').click()


#At this point, the browser window will be open at the checkout page,
#and the specific automation code you add will execute.

#To close the browser when you're done:
#driver.quit() 

