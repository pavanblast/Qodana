# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Set up Chrome options for mobile emulation
# chrome_options = Options()
# chrome_options.add_argument("--window-size=360,640")
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")
#
# # Path to your chromedriver executable
# chromedriver_path = "/path/to/chromedriver"
#
# # Initialize Chrome browser
# driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#
# # Open the website
# website_url = "https://appqa.signulu.com"
# driver.get(website_url)
#
#
# # Do whatever automation you need here
# # For example, you can interact with elements on the page using Selenium's methods
#
# # Close the browser
# #driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=chrome_options)
driver.maximize_window()
time.sleep(3)
driver.get("https://appqa.signulu.com/account/register")
time.sleep(3)
driver.find_element(By.XPATH, "//body/div[1]/div[1]/div/div/div[2]/form/div[1]/input").send_keys("mitisphere2@gmail.com")

# Perform any additional operations as needed
time.sleep(20)
#driver.quit()


