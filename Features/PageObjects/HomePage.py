import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import mysql.connector
from selenium.webdriver.support.wait import WebDriverWait

from Features.PageObjects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

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
        self.en_language_icon_xpath = "//div[contains(text(),'EN')]"
        self.ar_language_icon_xpath = "//div[contains(text(),'AR')]"
        self.hn_language_icon_xpath = "//div[contains(text(),'HN')]"
        self.fr_language_icon_xpath = "//div[contains(text(),'FR')]"
        self.spn_language_icon_xpath = "//div[contains(text(),'SP')]"
        self.side_bar_home_xpath = "//*[@id='main_nav']/li[1]/a/span"
        self.side_bar_manage_xpath = "//*[@id='main_nav']/li[2]/a/span"
        self.side_bar_templates_xpath = "//*[@id='main_nav']/li[3]/a/span"
        self.side_bar_reports_xpath = "//*[@id='main_nav']/li[4]/a/span"
        self.side_bar_Admin_xpath = "//*[@id='sub_admin']/a/span"
        self.side_bar_Billing_xpath = "//*[@id='dropdown9']/div/ul/li[1]/a"
        self.side_bar_Signatures_xpath = "//*[@id='dropdown9']/div/ul/li[2]/a"
        self.side_bar_PersonalInfo_xpath = "//*[@id='dropdown9']/div/ul/li[3]/a"
        self.side_bar_Actprofile_xpath = "//*[@id='dropdown9']/div/ul/li[4]/a"
        self.side_bar_cloud_xpath = "//*[@id='dropdown9']/div/ul/li[5]/a"
        self.side_bar_users_xpath = "//*[@id='dropdown9']/div/ul/li[6]/a"
        self.side_bar_contacts_xpath = "//*[@id='dropdown9']/div/ul/li[7]/a"
        self.side_bar_userprefrences_xpath = "//*[@id='dropdown9']/div/ul/li[8]/a"
        self.side_bar_folders_xpath = "//*[@id='main_nav']/li[7]/a/span"
        self.bynow_btn_xpath = "//*[@id='main']/div[1]/div/div/div[1]/div/button"

        self.header1_lang_xpath = "//*[@id='main']/div[2]/div[2]/div[1]/div/h3"
        self.header2_lang_xpath = "//*[@id='main']/div[2]/div[3]/div[1]/div/h3"
        self.header3_lang_xpath = "//*[@id='main']/div[2]/div[4]/div[1]/div/h3"
        self.create_card_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/h6"
        self.create_card_para_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/p"
        self.create_template_card_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/div/h6"
        self.create_template_card_para_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/div/p"
        self.upload_card_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[3]/div[1]/h6"
        self.upload_card_para_language_xpath = "//*[@id='main']/div[2]/div[2]/div[2]/div[3]/div[1]/p"
        self.draft_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[1]/p"
        self.to_sign_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[2]/p"
        self.Waiting_for_others_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[3]/p"
        self.my_documents_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[4]/p"
        self.completed_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[5]/p"
        self.rejected_card_language_xpath = "//*[@id='main']/div[2]/div[3]/div[2]/div[6]/p"
        self.transaction_repo1_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[1]"
        self.transaction_repo2_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[2]"
        self.transaction_repo3_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[3]"
        self.transaction_repo4_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[4]"
        self.transaction_repo5_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[5]"
        self.transaction_repo6_language_xpath = "//*[@id='main']/div[2]/div[4]/div[2]/div/div/table/thead[2]/tr/th[6]"

    def home_page_title(self):
        HomePage_title = self.driver.find_element(By.XPATH, self.home_page_title_xpath)
        assert HomePage_title.is_displayed(), "Home page title is not displayed"
        assert HomePage_title.text == "What would you like to do?", "Home page title mis-matched"

    def validate_days_left_and_used_documents_count(self):
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
        DaysLeftCount = results1[0][1]
        print(query1)
        print("Draft Documents Count = ", DaysLeftCount)

    def multi_lang_test_for_arabic_on_home_page(self):
        # SideBar = self.driver.find_element(By.XPATH, self.side_bar_menu_xpath)
        # SideBar.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.en_language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[2]").click()
        time.sleep(1)
        # Sidebar elements language test.
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_home_xpath).text == "بيت", "Side bar home Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_manage_xpath).text == "يدير", "Side bar manage Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_templates_xpath).text == "القوالب", "Side bar templates Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_reports_xpath).text == "التقارير", "Side bar reports Arabic Language mis-matched"
        self.driver.find_element(By.XPATH,
                                 self.side_bar_Admin_xpath).click()
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_Admin_xpath).text == "مسؤل", "Side bar admin Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_Billing_xpath).text == "الفواتير والاستخدام", "Side bar Billing Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_Signatures_xpath).text == "التوقيعات", "Side bar Signatures Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_PersonalInfo_xpath).text == "معلومات شخصية", "Side bar personal info Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_Actprofile_xpath).text == "تعريف حساب", "Side bar Act profile Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_cloud_xpath).text == "سحابة التخزين", "Side bar cloud storage Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_users_xpath).text == "المستخدمون", "Side bar users Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_contacts_xpath).text == "جهات الاتصال", "Side bar contacts Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.side_bar_userprefrences_xpath).text == "خيارات المستخدم", "Side bar user prefrences Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.bynow_btn_xpath).text == "اشتري الآن", "Buynow button Arabic Language mis-matched"

        # Main cards
        assert self.driver.find_element(By.XPATH,
                                        self.header1_lang_xpath).text == "ماذا تريد ان تفعل؟", "Header-1 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_language_xpath).text == "إنشاء وثيقة", "Header-1 card -1 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_para_language_xpath).text == "قم بتأليف مستند جديد باستخدام ميزة تأليف المستند باستخدام أدوات التحرير المحسّنة.", "Header-1 card paragraph Arabic Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_language_xpath).text == "إنشاء من قالب", "Header-1 card-2 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_para_language_xpath).text == "قم بتأليف مستند جديد باستخدام القوالب المحددة مسبقًا من كتالوج القوالب.", "Header-1 card paragraph Arabic Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_language_xpath).text == "تحميل الملفات", "Header-1 card-3 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_para_language_xpath).text == "محرك جوجل ، ون درايف ودروببوإكس.", "Header-1 card paragraph Arabic Language mis-matched"

        # Sub cards
        assert self.driver.find_element(By.XPATH,
                                        self.header2_lang_xpath).text == "لوحة القيادة", "Header-2 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.draft_card_language_xpath).text == "المسودات", "Header-2 card -1 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.to_sign_card_language_xpath).text == "للتوقيع", "Header-2 card -2 Arabic Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.Waiting_for_others_card_language_xpath).text == "في انتظار الآخرين", "Header-2 card -3 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.my_documents_card_language_xpath).text == "مستنداتي", "Header-2 card -4 Arabic Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.completed_card_language_xpath).text == "إجمالي المستندات الموقعة", "Header-2 card-5 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.rejected_card_language_xpath).text == "مرفوض / ملغى / قيد المراجعة", "Header-2 card-6 Arabic Language mis-matched"

        # Transaction reports
        assert self.driver.find_element(By.XPATH,
                                        self.header3_lang_xpath).text == "تم تعديله مؤخرًا (آخر 10 سجلات)", "Header-3 Arabic Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo1_language_xpath).text == "وثيقة", "Transaction report document header Arabic language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo2_language_xpath).text == "مشترك مع", "Transaction report document header Arabic language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo3_language_xpath).text == "تم إنشاؤها على", "Transaction report document header Arabic language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo4_language_xpath).text == "تحديث في", "Transaction report document header Arabic language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo5_language_xpath).text == "مالك", "Transaction report document header Arabic language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo6_language_xpath).text == "حالة", "Transaction report document header Arabic language mis-matched"

    def multi_lang_test_for_hindi_on_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.ar_language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[3]").click()
        time.sleep(2)

        # Main cards
        assert self.driver.find_element(By.XPATH,
                                        self.header1_lang_xpath).text == "आप क्या करना चाहेंगे ?", "Header-1 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_language_xpath).text == "दस्तावेज़ बनाएँ", "Header-1 card -1 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_para_language_xpath).text == "उन्नत संपादन टूल के साथ दस्तावेज़ संलेखन सुविधा का उपयोग करके एक नया दस्तावेज़ लिखें।", "Header-1 card-1 paragraph Hindi Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_language_xpath).text == "टेम्पलेट से बनाएँ", "Header-1 card-2 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_para_language_xpath).text == "टेम्प्लेट कैटलॉग से पूर्व-निर्धारित टेम्प्लेट का उपयोग करके एक नया दस्तावेज़ लिखें।", "Header-1 card-2 paragraph Hindi Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_language_xpath).text == "फाइलें अपलोड करें", "Header-1 card-3 Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_para_language_xpath).text == "गूगल ड्राइव, वन ड्राइव और ड्रॉप बॉक्स।", "Header-1 card-3 paragraph Hindi Language mis-matched"

        # Sub cards
        assert self.driver.find_element(By.XPATH,
                                        self.header2_lang_xpath).text == "डैशबोर्ड", "Header-2 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.draft_card_language_xpath).text == "ड्राफ्ट", "Header-2 card -1 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.to_sign_card_language_xpath).text == "हस्ताक्षर करने के लिए", "Header-2 card -2 Hindi Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.Waiting_for_others_card_language_xpath).text == "दूसरों का इंतज़ार", "Header-2 card -3 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.my_documents_card_language_xpath).text == "मेरे दस्तावेज़", "Header-2 card -4 Hindi Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.completed_card_language_xpath).text == "कुल हस्ताक्षरित दस्तावेज", "Header-2 card-5 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.rejected_card_language_xpath).text == "अस्वीकृत/रद्द/समीक्षा के अधीन", "Header-2 card-6 Hindi Language mis-matched"

        # Transaction reports
        assert self.driver.find_element(By.XPATH,
                                        self.header3_lang_xpath).text == "हाल ही में संशोधित (नवीनतम 10 रिकॉर्ड)", "Header-3 Hindi Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo1_language_xpath).text == "दस्तावेज़", "Transaction report document header Hindi language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo2_language_xpath).text == "इसके साथ साझा किया गया", "Transaction report document header Hindi language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo3_language_xpath).text == "पर बनाया", "Transaction report document header Hindi language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo4_language_xpath).text == "को अपडेट", "Transaction report document header Hindi language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo5_language_xpath).text == "मालिक", "Transaction report document header Hindi language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo6_language_xpath).text == "दर्जा", "Transaction report document header Hindi language mis-matched"

    def multi_lang_test_for_french_on_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hn_language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[4]").click()
        time.sleep(2)

        # Main cards
        assert self.driver.find_element(By.XPATH,
                                        self.header1_lang_xpath).text == "Qu'est-ce que tu aimerais faire?", "Header-1 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_language_xpath).text == "Créer un document", "Header-1 card -1 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_para_language_xpath).text == "Créez un nouveau document à l'aide de la fonctionnalité de création de documents avec des outils d'édition améliorés.", "Header-1 card-1 paragraph French Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_language_xpath).text == "Créer à partir du modèle", "Header-1 card-2 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_para_language_xpath).text == "Créez un nouveau document à l'aide des modèles prédéfinis du catalogue de modèles.", "Header-1 card-2 paragraph French Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_language_xpath).text == "Télécharger les fichiers", "Header-1 card-3 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_para_language_xpath).text == "Google Drive, One Drive et Drop Box.", "Header-1 card-3 paragraph French Language mis-matched"

        # Sub cards
        assert self.driver.find_element(By.XPATH,
                                        self.header2_lang_xpath).text == "Tableau de bord", "Header-2 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.draft_card_language_xpath).text == "Brouillons", "Header-2 card -1 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.to_sign_card_language_xpath).text == "Signer", "Header-2 card -2 French Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.Waiting_for_others_card_language_xpath).text == "En attendant les autres", "Header-2 card -3 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.my_documents_card_language_xpath).text == "Mes documents", "Header-2 card -4 French Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.completed_card_language_xpath).text == "Nombre total de documents signés", "Header-2 card-5 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.rejected_card_language_xpath).text == "Rejeté/Annulé/En cours de révision", "Header-2 card-6 French Language mis-matched"

        # Transaction reports
        assert self.driver.find_element(By.XPATH,
                                        self.header3_lang_xpath).text == "Récemment modifié (les 10 derniers enregistrements)", "Header-3 French Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo1_language_xpath).text == "Document", "Transaction report document header French language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo2_language_xpath).text == "Partagé avec", "Transaction report document header French language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo3_language_xpath).text == "Créé sur", "Transaction report document header French language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo4_language_xpath).text == "Mis à jour le", "Transaction report document header French language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo5_language_xpath).text == "Propriétaire", "Transaction report document header French language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo6_language_xpath).text == "Statut", "Transaction report document header French language mis-matched"


    def multi_lang_test_for_spanish_on_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.fr_language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[5]").click()
        time.sleep(2)

        # Main cards
        assert self.driver.find_element(By.XPATH,
                                        self.header1_lang_xpath).text == "Que te gustaría hacer?", "Header-1 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_language_xpath).text == "Crear documento", "Header-1 card -1 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_para_language_xpath).text == "Cree un nuevo documento utilizando la función de creación de documentos con herramientas de edición mejoradas.", "Header-1 card-1 paragraph Spanish Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_language_xpath).text == "Crear desde plantilla", "Header-1 card-2 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_para_language_xpath).text == "Cree un nuevo documento utilizando las plantillas predefinidas del catálogo de plantillas.", "Header-1 card-2 paragraph Spanish Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_language_xpath).text == "Subir archivos", "Header-1 card-3 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_para_language_xpath).text == "Google Drive, One Drive y Drop Box.", "Header-1 card-3 paragraph Spanish Language mis-matched"

        # Sub cards
        assert self.driver.find_element(By.XPATH,
                                        self.header2_lang_xpath).text == "Panel", "Header-2 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.draft_card_language_xpath).text == "Borradores", "Header-2 card -1 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.to_sign_card_language_xpath).text == "Para firmar", "Header-2 card -2 Spanish Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.Waiting_for_others_card_language_xpath).text == "Esperando a otros", "Header-2 card -3 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.my_documents_card_language_xpath).text == "Mis documentos", "Header-2 card -4 Spanish Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.completed_card_language_xpath).text == "Total de documentos firmados", "Header-2 card-5 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.rejected_card_language_xpath).text == "Rechazado/Cancelado/En revisión", "Header-2 card-6 Spanish Language mis-matched"

        # Transaction reports
        assert self.driver.find_element(By.XPATH,
                                        self.header3_lang_xpath).text == "Recientemente modificada (últimos 10 registros)", "Header-3 Spanish Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo1_language_xpath).text == "Documento", "Transaction report document header Spanish language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo2_language_xpath).text == "Compartido con", "Transaction report document header Spanish language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo3_language_xpath).text == "Creado en", "Transaction report document header Spanish language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo4_language_xpath).text == "Actualizado en", "Transaction report document header Spanish language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo5_language_xpath).text == "Dueño", "Transaction report document header Spanish language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo6_language_xpath).text == "Estado", "Transaction report document header Spanish language mis-matched"

    def multi_lang_test_for_english_on_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.spn_language_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div/div[2]/div[1]/ul/li[1]").click()
        time.sleep(2)

        # Main cards
        assert self.driver.find_element(By.XPATH,
                                        self.header1_lang_xpath).text == "What would you like to do?", "Header-1 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_language_xpath).text == "Create Document", "Header-1 card -1 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_card_para_language_xpath).text == "Author a new document using the document authoring feature with enhanced editing tools.", "Header-1 card-1 paragraph English Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_language_xpath).text == "Create From Template", "Header-1 card-2 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.create_template_card_para_language_xpath).text == "Author a new document using the pre-defined templates from the template catalogue.", "Header-1 card-2 paragraph English Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_language_xpath).text == "Upload Files", "Header-1 card-3 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.upload_card_para_language_xpath).text == "Google Drive, One Drive And Drop Box.", "Header-1 card-3 paragraph English Language mis-matched"

        # Sub cards
        assert self.driver.find_element(By.XPATH,
                                        self.header2_lang_xpath).text == "Dashboard", "Header-2 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.draft_card_language_xpath).text == "Drafts", "Header-2 card -1 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.to_sign_card_language_xpath).text == "To Sign", "Header-2 card -2 English Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.Waiting_for_others_card_language_xpath).text == "Waiting for Others", "Header-2 card -3 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.my_documents_card_language_xpath).text == "My Documents", "Header-2 card -4 English Language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.completed_card_language_xpath).text == "Total Signed Documents", "Header-2 card-5 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.rejected_card_language_xpath).text == "Rejected/Cancelled/Under Review", "Header-2 card-6 English Language mis-matched"

        # Transaction reports
        assert self.driver.find_element(By.XPATH,
                                        self.header3_lang_xpath).text == "Recently Modified(Latest 10 Records)", "Header-3 English Language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo1_language_xpath).text == "Document", "Transaction report document header English language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo2_language_xpath).text == "Shared with", "Transaction report document header English language mis-matched"

        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo3_language_xpath).text == "Created On", "Transaction report document header English language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo4_language_xpath).text == "Updated On", "Transaction report document header English language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo5_language_xpath).text == "Owner", "Transaction report document header English language mis-matched"
        assert self.driver.find_element(By.XPATH,
                                        self.transaction_repo6_language_xpath).text == "Status", "Transaction report document header English language mis-matched"
        SideBar = self.driver.find_element(By.XPATH, self.side_bar_menu_xpath)
        SideBar.click()
        time.sleep(2)

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
