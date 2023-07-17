import subprocess
import pyautogui
import time
import os
from selenium.webdriver.common.by import By

from Features.PageObjects.BasePage import BasePage


class LiteuserValidDocumentsUploadVerification(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.home_page_card_class = "create-card-box-item"
        self.upload_btn_xpath = "//button[contains(text(),'upload')]"
        self.upload_btn_on_popup_xpath = "//h3[contains(text(),'Click To Upload or Drag & Drop Your File Here')]"
        self.next_btn_xpath = "//*[text()='NEXT']"
        self.uploaded_document_count_xpath = "//*[@id='firstTab']/div[1]/h3[2]"
        self.uploaded_document_count_xpath_1 = "//*[@id='firstTab']/div[1]/h3"
        self.document_name = "//h3[contains(text(),'10 Pages document with fields')]"
        self.back_btn_xpath = "//button[contains(text(),'BACK')]"
        self.clear_all_btn_xpath = "//body/div/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/button[2]"

    def document_add_page(self):
        UploadCard = self.driver.find_element(By.CLASS_NAME, self.home_page_card_class)
        UploadCard.click()
        time.sleep(4)

    def upload_files(self):
        UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
        UploadBtn.click()
        # Document Count validation
        UploadedDocCount = self.driver.find_element(By.XPATH, self.uploaded_document_count_xpath)
        text = UploadedDocCount.text
        arr = text.split(' ')
        assert int(arr[2]) == 0, 'Uploaded documents count mis-matched in add document page.'

        # Clear all button visibility check
        try:
            ClearAllBtn = self.driver.find_element(By.XPATH, self.clear_all_btn_xpath)
            assert ClearAllBtn.is_displayed(), "Test case Failed : Clear All button visible on the Add document page"
        finally:
            print(
                "=========> (Before file upload) Test Case passed: Clear All button not visible on Add document page <=========")

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

            # Clear all button visibility check
            try:
                ClearAllBtn = self.driver.find_element(By.XPATH, self.clear_all_btn_xpath)
                assert ClearAllBtn.is_displayed(), "Test case Failed : Clear All button was not visible on the Add document page"
            finally:
                print(
                    "=========> (After file upload) Test Case Failed : Clear All button not visible on Add document page <=========")

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # Docx file uploading
            DocxFileUpload = current_directory + "\\Features\\InputFiles\\fields_document_docx.docx"
            pyautogui.write(DocxFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # Doc file uploading
            DocFileUpload = current_directory + "\\Features\\InputFiles\\file_sample_doc.doc"
            pyautogui.write(DocFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # JPG file uploading
            JpgFileUpload = current_directory + "\\Features\\InputFiles\\Image_jpg.jpg"
            pyautogui.write(JpgFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # JPEG file uploading
            JpegFileUpload = current_directory + "\\Features\\InputFiles\\Image_jpeg.jpeg"
            pyautogui.write(JpegFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(17)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            self.driver.execute_script("arguments[0].click();", UploadBtn)
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # PNG file uploading
            PngFileUpload = current_directory + "\\Features\\InputFiles\\Images_png.png"
            pyautogui.write(PngFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # XLS file uploading
            XlsFileUpload = current_directory + "\\Features\\InputFiles\\Document_xls.xls"
            pyautogui.write(XlsFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_xpath)
            UploadBtn.click()
            UploadBtn = self.driver.find_element(By.XPATH, self.upload_btn_on_popup_xpath)
            UploadBtn.click()
            time.sleep(1)
            # XLSX file uploading
            XlsxFileUpload = current_directory + "\\Features\\InputFiles\\Document_xlsx.xlsx"
            pyautogui.write(XlsxFileUpload)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(14)

            # Document Count validation
            UploadedDocCount = self.driver.find_element(By.XPATH, self.uploaded_document_count_xpath_1)
            text = UploadedDocCount.text
            arr = text.split(' ')
            assert int(arr[2]) == 8, 'Uploaded documents count mis-matched in add document page.'

            # Document name validation
            DocumentName = self.driver.find_element(By.XPATH, self.document_name)
            assert DocumentName.text == "10 Pages document with fields", "File Name mis-matched in add document page."

            NextBtn = self.driver.find_element(By.XPATH, self.next_btn_xpath)
            NextBtn.click()
            time.sleep(14)

            BackBtn = self.driver.find_element(By.XPATH, self.back_btn_xpath)
            BackBtn.click()
            time.sleep(14)

            # Document Count validation
            UploadedDocCount = self.driver.find_element(By.XPATH, self.uploaded_document_count_xpath_1)
            text = UploadedDocCount.text
            arr = text.split(' ')
            assert int(arr[2]) == 8, 'Uploaded documents count mis-matched in add document page.'

            # Document name validation
            DocumentName = self.driver.find_element(By.XPATH, self.document_name)
            assert DocumentName.text == "10 Pages document with fields", "File Name mis-matched in add document page."

            # Clear all button visibility check
            try:
                ClearAllBtn = self.driver.find_element(By.XPATH, self.clear_all_btn_xpath)
                assert ClearAllBtn.is_displayed(), "Test case Failed : Clear All button visible on the Add document page"
            finally:
                print("=========> Test Case passed: Clear All button not visible on Add document page <=========")

    def lite_user_file_upload_from_local_machine(self):
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

    def next_button_click(self):
        time.sleep(3)
        NextBtn = self.driver.find_element(By.XPATH, self.next_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", NextBtn)
        time.sleep(2)
        NextBtn.click()
        time.sleep(14)
