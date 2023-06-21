from selenium.webdriver.support.wait import WebDriverWait


# In the base page we are creating an object of driver.
# We are using this driver in the other pages and environment page.
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.implicit_wait = 25
