import time

from selenium.webdriver.common.by import By
import datetime

from Features.PageObjects.BasePage import BasePage
import mysql.connector


class ReportsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.reports_xpath = "//*[@id='main_nav']/li[4]/a/span"
        self.total_active_users_xpath = "//*[@id='main']/div[2]/div[1]/div[2]/div[3]/div/div/div/h5"
        self.total_users_xpath = "//*[@id='main']/div[2]/div[1]/div[2]/div[2]/div/div/div/h5"
        self.document_count_xpath = "//*[@id='main']/div[2]/div[1]/div[2]/div[1]/div/div/div/h5"
        self.documents_per_user_xpath = "//*[@id='main']/div[2]/div[1]/div[2]/div[4]/div/div/div/h5"
        self.dashboard_header_xpath = "//*[@id='main']/div[2]/div[1]/div[1]/div/div/h3[1]"
        self.doc_status_header_xpath = "//*[@id='main']/div[2]/div[2]/div[1]/div/h3"
        self.doc_volume_header_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div/div[1]/h3"
        self.transaction_reports_header_xpath = "//*[@id='main']/div[2]/div[3]/div/h3"
        self.donut_chart_xpath = "//*[@class='recharts-layer recharts-pie']"
        self.bar_chart_xpath = "//*[@class='recharts-wrapper']"
        self.transactions_reports_xpath = "//*[@id='main']/div[2]/div[4]/div/div/table/tbody/tr"

    def fetch_records(self, companyId):
        time.sleep(5)
        ele = self.driver.find_element(By.XPATH, self.reports_xpath)
        ele.click()

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="attainica.cq1yuvwrfsbo.us-east-1.rds.amazonaws.com",
            user="signattqadb",
            password="4rfs897sQrpA",
            database="signattqadb"
        )

        cursor = connection.cursor()

        # Execute a query
        sql1 = """SELECT COUNT(u.user_id) as TotalActiveUsers
            FROM signattqadb.user u
            INNER JOIN signattqadb.user_subscription us ON u.user_id = us.user_id
            WHERE us.company_id= """ + companyId + """ AND u.is_active = 1 AND current_date() 
            BETWEEN DATE_FORMAT(us.effective_from, '%Y-%m-%d') AND 
            IFNULL(DATE_FORMAT(us.effective_until, '%Y-%m-%d'), 
            current_date()) ORDER BY us.effective_from desc;"""

        cursor.execute(sql1)
        results = cursor.fetchall()
        print(results)
        TotalActiveUsers = results[0][0]
        print("TotalActiveUsers = ", TotalActiveUsers)
        TotalActiveUsersAct = self.driver.find_element(By.XPATH, self.total_active_users_xpath).text

        assert int(TotalActiveUsers) == int(TotalActiveUsersAct), "Total Active Users count not matching"

        sql2 = """SELECT COUNT(u.user_id) AS TotalInActiveUsers
                FROM signattqadb.user u
                INNER JOIN signattqadb.user_subscription us ON u.user_id = us.user_id
                WHERE us.company_id=""" + companyId + """ AND us.effective_until <= SYSDATE()
                ORDER BY us.effective_from desc;"""

        cursor.execute(sql2)
        results = cursor.fetchall()
        print(results)
        TotalInActiveUsers = results[0][0]
        print("TotalInActiveUsers = ", TotalInActiveUsers)

        TotalUsers = TotalActiveUsers + TotalInActiveUsers
        TotalUsersAct = self.driver.find_element(By.XPATH, self.total_users_xpath).text
        assert int(TotalUsers) == int(TotalUsersAct), "Total Users count not matching"

        today = datetime.date.today()
        year = today.year
        month = today.month

        sql3 = """SELECT COUNT(DISTINCT d.ad_document_id) as Count FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id
                INNER JOIN signattqadb.user u ON p.user_id = u.user_id
                INNER JOIN signattqadb.ad_document_status s ON s.ad_document_status_id = d.status_id
                WHERE s.code = 'APPROVED' AND YEAR(d.created_date) = """ + str(year) + """ 
                AND d.company_id = """ + companyId + """ order by d.ad_document_id desc;"""

        cursor.execute(sql3)
        results = cursor.fetchall()
        print(results)
        YearlyUsedDocument = results[0][0]
        print("YearlyUsedDocument = ", YearlyUsedDocument)

        sql4 = """SELECT COUNT(DISTINCT d.ad_document_id) as Count
                FROM signattqadb.ad_document d
                INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id 
                INNER JOIN signattqadb.user u ON p.user_id = u.user_id 
                INNER JOIN signattqadb.ad_document_status s ON s.ad_document_status_id = d.status_id
                WHERE s.code = 'APPROVED'
                AND YEAR(d.created_date) = """ + str(year) + """
                AND MONTH(d.created_date) = """ + str(month) + """ 
                AND d.company_id = """ + companyId + """ order by d.ad_document_id desc;"""

        cursor.execute(sql4)
        results = cursor.fetchall()
        print(results)
        MonthlyUsedDocument = results[0][0]

        x = self.driver.find_element(By.XPATH, self.document_count_xpath).text
        documents = x.split("/")
        MonthlyUsedDocumentAct = x[0]
        YearlyUsedDocumentAct = x[1]
        print("MonthlyUsedDocument = ", MonthlyUsedDocument)
        print("YearlyUsedDocumentAct = ", YearlyUsedDocumentAct)

        assert int(MonthlyUsedDocumentAct) == int(MonthlyUsedDocument), "MonthlyUsedDocument count not matching"
        assert int(YearlyUsedDocumentAct) == int(YearlyUsedDocument), "YearlyUsedDocument count not matching"
        docs_per_user = self.driver.find_element(By.XPATH, self.documents_per_user_xpath)
        assert int(docs_per_user) == round(YearlyUsedDocument / TotalUsers), "Document per user count not matching"

    def validate_headers(self):
        dashboard_header = self.driver.find_element(By.XPATH, self.dashboard_header_xpath)
        doc_status_header = self.driver.find_element(By.XPATH, self.doc_status_header_xpath)
        doc_volume_header = self.driver.find_element(By.XPATH, self.doc_volume_header_xpath)
        transaction_reports_header = self.driver.find_element(By.XPATH, self.transaction_reports_header_xpath)

        assert dashboard_header.is_displayed(), "dashboard_header not displayed"
        assert doc_status_header.is_displayed(), "doc_status_header not displayed"
        assert doc_volume_header.is_displayed(), "doc_volume_header not displayed"
        assert transaction_reports_header.is_displayed(), "transaction_reports not displayed"

    def validate_donut_chart(self):
        donut_chart = self.driver.find_element(By.XPATH, self.donut_chart_xpath)
        assert donut_chart.is_displayed(), "dashboard_header not displayed"

    def validate_bar_chart(self):
        donut_chart = self.driver.find_element(By.XPATH, self.bar_chart_xpath)
        assert donut_chart.is_displayed(), "dashboard_header not displayed"

    def transactions_reports(self):
        transactions_reports = self.driver.find_element(By.XPATH, self.transactions_reports_xpath)
        assert transactions_reports.is_displayed(), "transactions_reports are not displayed"
