import mysql.connector
import self as self
from selenium.webdriver.common.by import By

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="attainica.cq1yuvwrfsbo.us-east-1.rds.amazonaws.com",
    user="signattqadb",
    password="4rfs897sQrpA",
    database="signattqadb"
)

cursor = connection.cursor()

# Execute a query
sql4 = """SELECT COUNT(DISTINCT d.ad_document_id) as Count
        FROM signattqadb.ad_document d
        INNER JOIN signattqadb.ad_party p ON p.ad_document_id = d.ad_document_id 
        INNER JOIN signattqadb.user u ON p.user_id = u.user_id 
        INNER JOIN signattqadb.ad_document_status s ON s.ad_document_status_id = d.status_id
        WHERE s.code = 'APPROVED'
        AND YEAR(d.created_date) = """ + "2023" + """
        AND MONTH(d.created_date) = """ + "06" + """ 
        AND d.company_id = """ + "52" + """ order by d.ad_document_id desc;"""

cursor.execute(sql4)
results = cursor.fetchall()
print(results)
MonthlyUsedDocument = results[0][0]
print("MonthlyUsedDocument = ", MonthlyUsedDocument)