import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Features.PageObjects.BasePage import BasePage


class RegistrationPageOnMobile(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.menubar_xpath = "//body/header[2]/nav/div/button/span"
        self.start_trail_bt_xpath = "//a[contains(text(),'Start Trial')]"
        self.email_input_xpath = "//input[@type='email']"
        self.create_free_account_btn_xpath = "//button[contains(text(),'Create free account')]"
        self.email_exist_msg_xpath = "//*[contains(text(),'Email Address already exists.')]"
        self.okay_btn_xpath = "//button[contains(text(),'OKAY')]"


    def mobile_registration_page_navigation(self):
        MenuBar = self.driver.find_element(By.XPATH, self.menubar_xpath)
        MenuBar.click()
        time.sleep(1)
        StartFreeTrailBtn = self.driver.find_element(By.XPATH, self.start_trail_bt_xpath)
        StartFreeTrailBtn.click()
        time.sleep(3)

    def enter_email_and_ciclk_on_btn(self):
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys("mitisphere2@gmail.com")
        self.driver.find_element(By.XPATH, self.create_free_account_btn_xpath).click()
        time.sleep(4)

    def thank_you_page_verification(self):
        try:
            Message = self.driver.find_element(By.XPATH, self.email_exist_msg_xpath)
            assert Message.text == "Email Address already exists.", "Message is mismatched on email exist popup"
            OkayBtn = self.driver.find_element(By.XPATH, self.okay_btn_xpath)
            assert OkayBtn.is_displayed(), "Okay button not displayed"
        except NoSuchElementException:
            pass


