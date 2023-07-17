import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Features.PageObjects.BasePage import BasePage
import autoit


class InPersonSign(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.upload_btn_xpath = "//*[contains(text(),'Upload Files')]"
        self.upload_btn_on_popup_xpath = "//*[contains(text(),'Click To Upload or Drag & Drop Your File Here')]"
        self.side_bar_xpath = "//*[@id='sidebar-nav']/div/div/div[2]/button/img"
        self.add_new_recip_btn_xpath = "//button[@id='new_recipient_add']"
        self.first_name_input_xpath = "//textarea[@id='FirstName']"
        self.last_name_input_xpath = "//textarea[@id='LastName']"
        self.email_input_xpath = "//textarea[@id='EmailAddress']"
        self.signatory_toggle_xpath = "//*[@id='new_recipient']/div[2]/div/div[6]/div/div[1]/label/span"
        self.add_btn_xpath = "//button[contains(text(),'ADD')]"
        self.dropdown_xpath = "//*[@id='sidebar']/div/div[3]/div[2]/div[1]/div[2]/select"

    def normal_user_file_upload_from_local_machine(self):
        #element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.upload_btn_xpath)))
        #element.click()
        time.sleep(8)
        UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
        UploadBtn.click()
        time.sleep(1)
        UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
        self.driver.execute_script("arguments[0].click();", UploadBtn)
        time.sleep(2)
        # To get current working directory path
        current_directory = os.getcwd()
        # Use pyautogui to enter the file path and press Enter

        # Pdf file uploading
        PdfFileUpload = current_directory + "\\Features\\InputFiles\\10 Pages document with fields.pdf"
        pyautogui.write(PdfFileUpload)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(10)

    def select_page_adding_recipient_selecting_notary(self):
        SideBarMenu = self.driver.find_element(By.XPATH, self.side_bar_xpath)
        SideBarMenu.click()
        time.sleep(1)

        # Adding recipient from add from contacts popup.
        self.driver.find_element(By.XPATH, self.add_new_recip_btn_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.first_name_input_xpath).send_keys("Bheem")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.last_name_input_xpath).send_keys("B")
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys("mitisphere6@gmail.com")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.signatory_toggle_xpath))
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.signatory_toggle_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.add_btn_xpath).click()
        time.sleep(3)

        # Selecting Notary for the recipient.
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//*[@id='sidebar']/div/div[3]/div[2]/div[3]/div[1]/label/span"))
        DropDown = Select(self.driver.find_element(By.XPATH, self.dropdown_xpath))
        DropDown.select_by_value("inPerson")
        time.sleep(2)

    def drop_controls_for_both_recipients(self):
        time.sleep(10)
        SideBarMenu = self.driver.find_element(By.XPATH, self.side_bar_xpath)
        SideBarMenu.click()
        time.sleep(1)
        autoit.mouse_click_drag(180,711,600,700,"left",5)
