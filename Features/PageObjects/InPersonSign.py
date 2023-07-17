import os
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Features.PageObjects.BasePage import BasePage



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
        time.sleep(6)

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
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.signatory_toggle_xpath).click()
        self.driver.find_element(By.XPATH, self.add_btn_xpath).click()
        time.sleep(3)

        # Selecting Notary for the recipient.
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//*[@id='sidebar']/div/div[3]/div[2]/div[3]/div[1]/label/span"))
        DropDown = Select(self.driver.find_element(By.XPATH, self.dropdown_xpath))
        DropDown.select_by_value("inPerson")
        time.sleep(2)

    def drag_and_drop_controls(self):
        driver = self.driver
        driver.get("https://appqa.signulu.com/account/documentprepare/7797")
        time.sleep(10)
        # source1 = driver.find_element(By.ID, 'att-signature-icon-drag')
        # action = ActionChains(driver)
        # target_element = driver.find_element(By.XPATH, "//*[@id='scrollArea']/div/div/canvas")
        # action.click_and_hold(source1).move_by_offset(229, 156).release(target_element).perform()
        # time.sleep(5)

        # # Find the source element to drag
        # source_element = driver.find_element(By.XPATH, "att-signature-icon-drag")  # Replace with the actual source element ID
        #
        # # Find the destination element to drop
        # destination_element = driver.find_element_by_id("destination_element_id")  # Replace with the actual destination element ID
        # # Get the source element's coordinates
        # source_x = source_element.location['x']
        # source_y = source_element.location['y']
        # # Get the destination element's coordinates
        # destination_x = 603
        # destination_y = 396
        # # Perform the drag and drop using AutoIt
        # autoit.mouse_click_drag(source_x, source_y, destination_x, destination_y)

        dropDown = ActionChains(driver)
        signature = driver.find_element(By.XPATH, "//*[@id='docuemt_controls_area']/div[2]/ul/li[1]/button/img");
        time.sleep(1)

        canvas = driver.find_element(By.XPATH, "//*[@id='scrollArea']/div/div[1]/canvas");
        xoffset1 = signature.location['x']
        yoffset1 = signature.location['y']
        xoffset = canvas.location['x']
        yoffset = canvas.location['y']
        print(str(xoffset1)+"===>"+str(yoffset1))
        print(str(xoffset)+"===>"+str(yoffset))
        xoffset = (xoffset - xoffset1) + 573;
        yoffset = (yoffset - yoffset1) + 700;
        print(str(xoffset) + "===>" + str(yoffset))
        # message = f"My name is {xoffset1} and I am {yoffset1} years old.{xoffset} and {yoffset}"
        # # driver.execute_script("alert(message);")
        # # time.sleep(50)
        # dropDown.drag_and_drop_by_offset(signature, xoffset, yoffset).perform();
        # time.sleep(2);

        actions = ActionChains(driver)
        actions.move_to_element(signature)
        actions.click_and_hold()
        actions.move_by_offset(xoffset, yoffset)
        actions.release()
        actions.move_to_element(canvas)
        actions.click()
        actions.perform()





