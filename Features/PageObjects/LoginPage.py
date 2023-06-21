from selenium.webdriver.common.by import By
import time
from Features.PageObjects.BasePage import BasePage


# The page contains all the locators and the actions to perform on that web element. In this page file we have
# declared all the locators at the class level, and we are using them in the respective methods.
class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.userName_xpath = "//*[@id='username']"
        self.password_xpath = "//*[@id='password']"
        self.captcha_code_xpath = "//div[@id='captcha']"
        self.captcha_input_id = "inputType"
        self.captcha_verify_button_xpath = "//button[@id='succesBTN']"
        self.loginButton_xpath = "//*[text()='Login']"
        self.terms_conditions_xpath = "//*[text()='Terms & Conditions']"
        self.home_page_text_xpath = "//*[@id='main']/div[2]/div[2]/div[1]/div/h3"
        self.multi_login_xpath = "//*[@id='multilogin']/div[2]/button[1]"
        self.user_menu_xpath = "//*[@id='user_profile_id']"
        self.log_out_xpath = "//*[text()='Log Out']"
        self.signulu_logo_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div/div[1]/div[1]/img"
        self.header1_xpath = "//h1[contains(text(),'Please Login To Your Account')]"
        self.header2_xpath = "//*[text()='Login using User ID and Password']"
        self.rememberme_label_xpath = "//label[contains(text(),'Remember Me')]"
        self.forgot_link_xpath = "//a[contains(text(),'Forgot Password?')]"
        # self.paragrapg1_xpath = "//*[contains(text(),'Don't have an account?")]'
        self.paragrapg2_xpath = "/*[contains(text(),'Please click to view')]"
        self.header3_xpath = "//h3[contains(text(),'Signulu – way forward for digital signature servic')]"
        self.watch_demo_xpath = "//button[contains(text(),'Watch Demo')]"
        self.schedule_demo_xpath = "//button[contains(text(),'Schedule Demo')]"
        self.page_right_image_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div/div[2]/div[2]/img"


    def email_and_psw_inputs(self, Email, Password):

        EmailInput = self.driver.find_element(By.XPATH, self.userName_xpath)
        EmailInput.clear()
        EmailInput.send_keys(Email)
        time.sleep(1)
        PswInput = self.driver.find_element(By.XPATH, self.password_xpath)
        PswInput.click()
        PswInput.send_keys(Password)
        time.sleep(1)

    def landing_page_login_button_click(self):
        LoginButton = self.driver.find_element(By.XPATH, self.loginButton_xpath)
        LoginButton.click()
        time.sleep(7)

    def captcha_enter(self):
        CaptchaCode = self.driver.find_element(By.XPATH, self.captcha_code_xpath)
        CaptchaInput = self.driver.find_element(By.ID, self.captcha_input_id)
        CaptchaInput.send_keys(CaptchaCode.text)
        time.sleep(1)
        VerifyButton = self.driver.find_element(By.XPATH, self.captcha_verify_button_xpath)
        VerifyButton.click()
        time.sleep(2)

    def login_click(self):
        LoginButton = self.driver.find_element(By.XPATH, self.loginButton_xpath)
        LoginButton.click()
        time.sleep(3)

    def home_page_text(self):
        try:
            atttext = self.driver.find_element(By.XPATH, self.home_page_text_xpath).text
            time.sleep(4)
            assert atttext == "What would you like to do?", "Login failed?"
        except:
            self.driver.find_element(By.XPATH, self.multi_login_xpath).click()
            time.sleep(3)
            atttext = self.driver.find_element(By.XPATH, self.home_page_text_xpath).text
            assert atttext == "What would you like to do?", "Login failed?"

    def log_out(self):
        self.driver.find_element(By.XPATH, self.user_menu_xpath).click()
        self.driver.find_element(By.XPATH, self.log_out_xpath).click()
        time.sleep(3)

    def login_page_signulu_logo_validation(self):
        signuLuLogo = self.driver.find_element(By.XPATH, self.signulu_logo_xpath)
        assert signuLuLogo.is_displayed() == True, "Signulu Logo is not displayed on login page header section"

    def login_page_headers_validations(self):
        Header_1 = self.driver.find_element(By.XPATH, self.header1_xpath)
        assert Header_1.is_displayed() == True, "Please Login To Your Account Header is not displayed on the Login page"
        assert Header_1.text == "Please Login To Your Account", "Please Login To Your Account Header mis-matched on login page"
        Header_2 = self.driver.find_element(By.XPATH, self.header2_xpath)
        assert Header_2.is_displayed() == True, "Login using User ID and Password Header is not displayed on the Login page"
        assert Header_2.text == "Login using User ID and Password", "Login using User ID and Password Header mis-matched on login page"
        Header_3 = self.driver.find_element(By.XPATH, self.header3_xpath)
        assert Header_3.is_displayed() == True, "Signulu – way forward for digital signature services Header is not displayed on the Login page"
        assert Header_3.text == "Signulu – way forward for digital signature services", "Signulu – way forward for digital signature services Header mis-matched on login page"

    def login_page_paragraphs_validations(self):
        Paragraph_1 = self.driver.find_element(By.XPATH, self.paragrapg1_xpath)
        assert Paragraph_1.is_displayed() == True, "Don't have an account? Sign up now paragraph is not displayed on the Login page footer"
        assert Paragraph_1.text == "Don't have an account? Sign up now", "Don't have an account? Sign up now paragraph is mis-matched on login page"
        Paragraph_2 = self.driver.find_element(By.XPATH, self.paragrapg2_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Paragraph_2)
        time.sleep(3)
        # assert Paragraph_2.is_displayed() == True, "Login using User ID and Password Header is not displayed on the Login page"
        # assert Paragraph_2.text == "Login using User ID and Password", "Login using User ID and Password Header mis-matched on login page"
