
import time
from selenium.webdriver.common.by import By
from Features.PageObjects.BasePage import BasePage
import mysql.connector



class ReportsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.reports_xpath = "//*[@id='main_nav']/li[4]/a/span"


    def fetch_records(self):

        time.sleep(5)

        ele = self.driver.find_element(By.XPATH, self.reports_xpath)

        ele.click()
