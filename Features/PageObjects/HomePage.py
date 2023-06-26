import time

from selenium.webdriver.common.by import By
import mysql.connector
from Features.PageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.side_bar_menu_xpath = "//*[@id='sidebar-nav']/div/div/div[2]/button/img"
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
        self.draft_count_xpath = "//*[text()='Drafts']/../h5"
        self.to_count_xpath = ""
        self.language_icon_xpath = "//div[contains(text(),'EN')]"

    def home_page_title(self):
        HomePage_title = self.driver.find_element(By.XPATH, self.home_page_title_xpath)
        assert HomePage_title.is_displayed(), "Home page title is not displayed"
        assert HomePage_title.text == "What would you like to do?", "Home page title mis-matched"

    def multi_lang_test_on_home_page(self):
        SideBar = self.driver.find_element(By.XPATH, self.side_bar_menu_xpath)
        SideBar.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[2]").click()
        time.sleep(1)
        txt = self.driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div[2]/div[1]/div/h3")
        print("Language ======> ", txt.text)
        assert txt.text == "ماذا تريد ان تفعل؟", "Language mis-matched"

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
                        WHERE p.user_id = """ + userId + """ AND ds.name in ('Draft');"""
        cursor.execute(query1)

        # Fetch the query results
        results1 = cursor.fetchall()
        print(results1)
        DraftDocumentsCount = results1[0][1]
        print(query1)
        print("Draft Documents Count = ", DraftDocumentsCount)

        # Execute a query
        query2 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                       FROM signattqadb.ad_document d
                       INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                       INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                       INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                       WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                       AND ds.name in ('Rejected');"""
        cursor.execute(query2)

        # Fetch the query results
        results2 = cursor.fetchall()
        ToSignDocumentsCount = results2[0][1]
        print(query2)
        print("To Sign Documents Count = ", ToSignDocumentsCount)

        # Execute a query
        query3 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                              FROM signattqadb.ad_document d
                              INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                              INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                              INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                              WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                              AND ds.name in ('Rejected');"""
        cursor.execute(query3)

        # Fetch the query results
        results3 = cursor.fetchall()
        WaitingForOthersDocumentsCount = results3[0][1]
        print(query3)
        print("Waiting for others Documents Count = ", WaitingForOthersDocumentsCount)

        # Execute a query
        query4 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                                   FROM signattqadb.ad_document d
                                   INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                                   INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                                   INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                                   WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                                   AND ds.name in ('Rejected');"""
        cursor.execute(query4)

        # Fetch the query results
        results4 = cursor.fetchall()
        MyDocumentsCount = results4[0][1]
        print(query4)
        print("My Documents Documents Count = ", MyDocumentsCount)

        # Execute a query
        query5 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                                          FROM signattqadb.ad_document d
                                          INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                                          INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                                          INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                                          WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                                          AND ds.name in ('Rejected');"""
        cursor.execute(query5)

        # Fetch the query results
        results5 = cursor.fetchall()
        TotalCompletedDocumentsCount = results5[0][1]
        print(query5)
        print("My Documents Documents Count = ", TotalCompletedDocumentsCount)

        # Execute a query
        query6 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                WHERE (p.user_id = """ + userId + """ OR p.email_address = '""" + Email + """' AND ds.code = 'Rejected')
                AND ds.name in ('Rejected');"""
        cursor.execute(query6)

        # Fetch the query results
        results6 = cursor.fetchall()
        RejectedDocumentsCount = results6[0][1]
        print(query6)
        print("Rejected Documents Count = ", RejectedDocumentsCount)

        # Execute a query
        query7 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                WHERE p.user_id = """ + userId + """ AND ds.name in ('Cancelled');"""
        cursor.execute(query7)

        # Fetch the query results
        results7 = cursor.fetchall()
        print(results7)
        CancelledDocumentsCount = results7[0][1]
        print(query7)
        print("Cancelled Documents Count = ", CancelledDocumentsCount)

        # Execute a query
        query8 = """SELECT ds.name AS Name, COUNT(DISTINCT d.ad_document_id) AS RecordCount
                        FROM signattqadb.ad_document d
                        INNER JOIN signattqadb.ad_document_status ds ON d.status_id = ds.ad_document_status_id
                        INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                        INNER JOIN signattqadb.ad_document_status dp ON p.status_id = dp.ad_document_status_id
                        WHERE p.user_id = """ + userId + """ AND ds.name in ('Cancelled');"""
        cursor.execute(query8)

        # Fetch the query results
        results8 = cursor.fetchall()
        print(results8)
        UnderRivewDocumentsCount = results8[0][1]
        print(query8)
        print("Under Rivew Documents Count = ", UnderRivewDocumentsCount)

        # Getting actual cards count on application.
        DraftsCountAct = int(self.driver.find_element(By.xpath("//*[text()='Drafts']/../h5")).getText().toString());
        int
        ToSignCountAct = Integer.parseInt(
            driver.findElement(By.xpath("//*[text()='To Sign']/../h5")).getText().toString());
        int
        PendingCountAct = Integer.parseInt(
            driver.findElement(By.xpath("//*[text()='Waiting for Others']/../h5")).getText().toString());
        int
        MyDocumentsCountAct = Integer.parseInt(
            driver.findElement(By.xpath("//*[text()='My Documents']/../h5")).getText().toString());
        int
        TotalDocumentCountAct = Integer.parseInt(
            driver.findElement(By.xpath("//*[text()='Total Signed Documents']/../h5")).getText().toString());
        int
        RejectedCountAct = Integer.parseInt(driver.findElement(
            By.xpath("//*[text()='Rejected/Cancelled/Under Review']/../div[1]/div[1]/h5")).getText().toString());
        int
        CancelledCountAct = Integer.parseInt(driver.findElement(
            By.xpath("//*[text()='Rejected/Cancelled/Under Review']/../div[1]/div[2]/h5")).getText().replace("/ ",
                                                                                                             "").toString());
        int
        UnderreviewCountAct = Integer.parseInt(driver.findElement(
            By.xpath("//*[text()='Rejected/Cancelled/Under Review']/../div[1]/div[3]/h5")).getText().replace("/ ",
                                                                                                             "").toString());

        time.sleep(50)
        cursor.close()
        connection.close()
