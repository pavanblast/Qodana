import time

from selenium.webdriver.common.by import By
import mysql.connector
from Features.PageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.home_page_title_xpath = "//h3[contains(text(),'What would you like to do?')]"
        self.create_document_card_xpath = "//*[text()='Create Document']"
        self.create_from_temp_card_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/div/h6"
        self.upload_files_card_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[3]/div[1]/h6"
        self.draft_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[1]"
        self.to_sign_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[2]"
        self.waiting_for_others_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[3]"
        self.my_documents_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[4]"
        self.completed_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[5]"
        self.reject_under_review_cancelled_card_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[6]"

    def home_page_title(self):
        HomePage_title = self.driver.find_element(By.XPATH, self.home_page_title_xpath)
        assert HomePage_title.is_displayed(), "Home page title is not displayed"
        assert HomePage_title.text == "What would you like to do?", "Home page title mis-matched"

    def home_page_cards_visibility_check(self):
        CreateDocument_card = self.driver.find_element(By.XPATH, self.create_document_card_xpath)
        assert CreateDocument_card.is_displayed(), "Create document card is not displayed"
        CreateTemp_card = self.driver.find_element(By.XPATH, self.create_from_temp_card_xpath)
        assert CreateTemp_card.is_displayed(), "Create from temp card is not displayed"
        UploadFiles_card = self.driver.find_element(By.XPATH, self.upload_files_card_xpath)
        assert UploadFiles_card.is_displayed(), "Upload files card is not displayed"

    def dash_board_cards_visibility_check(self):
        Draft_card = self.driver.find_element(By.XPATH, self.draft_card_xpath)
        assert Draft_card.is_displayed(), "Draft card is not displayed"
        ToSign_card = self.driver.find_element(By.XPATH, self.to_sign_card_xpath)
        assert ToSign_card.is_displayed(), "ToSign card is not displayed"
        WaitingForOthers_card = self.driver.find_element(By.XPATH, self.waiting_for_others_card_xpath)
        assert WaitingForOthers_card.is_displayed(), "Waiting For others card is not displayed"
        MyDocumentsCompleted_card = self.driver.find_element(By.XPATH, self.my_documents_card_xpath)
        assert MyDocumentsCompleted_card.is_displayed(), "My Documents completed card is not displayed"
        Completed_card = self.driver.find_element(By.XPATH, self.completed_card_xpath)
        assert Completed_card.is_displayed(), "Completed card is not displayed"
        Rejected_UnderReview_Cancelled_card = self.driver.find_element(By.XPATH,
                                                                       self.reject_under_review_cancelled_card_xpath)
        assert Rejected_UnderReview_Cancelled_card.is_displayed(), "Rejected_UnderReview_Cancelled card is not displayed"

    def dash_board_cards_count_validation(self, userId, companyID, Email):
        RejectedCount = 0
        ToSignCount = 0
        PendingCount = 0
        RevokedCount = 0
        UnderReviewCount = 0
        MyDocumentsCount = 0
        DraftsCount = 0
        TotalSignedCount = 0
        ApprovedCount = 0

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="attainica.cq1yuvwrfsbo.us-east-1.rds.amazonaws.com",
            user="signattqadb",
            password="4rfs897sQrpA",
            database="signattqadb"
        )

        cursor = connection.cursor()

        # Execute a query
        query1 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                AND ds.name in ('Rejected');"""
        cursor.execute(query1)

        # Fetch the query results
        results = cursor.fetchall()
        RejectedDocumentsCount = results[0][1]
        print(query1)
        print("Rejected Documents Count = ", RejectedDocumentsCount)

        # Execute a query
        query2 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                WHERE p.user_id = """ + userId + """ AND ds.name in ('Draft');"""
        cursor.execute(query2)

        # Fetch the query results
        results2 = cursor.fetchall()
        print(results2)
        DraftDocumentsCount = results2[0][1]
        print(query2)
        print("Draft Documents Count = ", DraftDocumentsCount)

        # Execute a query
        query3 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                WHERE p.user_id = """ + userId + """ AND ds.name in ('Cancelled');"""
        cursor.execute(query3)

        # Fetch the query results
        results3 = cursor.fetchall()
        print(results3)
        CancelledDocumentsCount = results3[0][1]
        print(query3)
        print("Draft Documents Count = ", CancelledDocumentsCount)

        # Execute a query
        query3 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                        FROM signattqadb.ad_document d
                        INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                        INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                        INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                        WHERE p.user_id = """ + userId + """ AND ds.name in ('Cancelled');"""
        cursor.execute(query3)

        # Fetch the query results
        results3 = cursor.fetchall()
        print(results3)
        CancelledDocumentsCount = results3[0][1]
        print(query3)
        print("Draft Documents Count = ", CancelledDocumentsCount)

        time.sleep(50)

        cursor.close()
        connection.close()
