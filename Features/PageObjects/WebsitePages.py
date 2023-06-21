from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

from Features.PageObjects.BasePage import BasePage


class WebsitePages(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.about_link_text = "About"
        self.industries_menu_xpath = "//header/nav[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]"
        self.manufacturing_link_text = "Manufacturing"
        self.banking_services_link_text = "Banking and Financial Services"
        self.professional_services_link_text = "Professional Services"
        self.real_estate_link_text = "Real Estate"
        self.healthcare_link_text = "Healthcare"
        self.law_link_text = "Law"
        self.it_link_text = "IT"
        self.pricing_link_text = "Pricing"
        self.blog_link_text = "Blog"
        self.contact_link_text = "Contact"
        self.login_link_text = "Login"
        self.start_trial_link_text = "Start Trial"
        self.start_free_trail_button1_xpath = "(//button[contains(text(),'Start Free Trial ')])[1]"
        self.start_free_trail_button2_xpath = "(//button[contains(text(),'Start Free Trial ')])[2]"
        self.start_free_trail_button3_xpath = "(//button[contains(text(),'Start Free Trial ')])[3]"
        self.start_free_trail_button4_xpath = "(//button[contains(text(),'Start Free Trial ')])[4]"
        self.start_free_trail_button5_xpath = "(//button[contains(text(),'Start Free Trial ')])[5]"
        self.footer_start_free_trail_button_xpath = "//a[contains(text(),'Start Free Trial')]"
        self.know_more_button1_xpath = "(//button[contains(text(),'Know More ')])[1]"
        self.know_more_button2_xpath = "(//button[contains(text(),'Know More ')])[2]"
        self.know_more_button3_xpath = "(//button[contains(text(),'Know More ')])[3]"
        self.know_more_button4_xpath = "(//button[contains(text(),'Know More ')])[4]"
        self.know_more_button5_xpath = "(//button[contains(text(),'Know More ')])[5]"
        self.video_1_xpath = "//body/div[1]/div[1]/p[1]/video[1]"
        self.video_2_xpath = "//body/section[1]/div/div[2]/div[2]/video"
        self.video_3_xpath = "//body/section[1]/div/div[3]/div[2]/video"
        self.video_4_xpath = "//body/section[1]/div/div[4]/div[2]/video"
        self.facebook_xpath = "//body/footer/div/div/div[4]/ul/li[1]/a"
        self.twitter_xpath = "//body/footer/div/div/div[4]/ul/li[2]/a"
        self.linkedin_xpath = "//body/footer/div/div/div[4]/ul/li[3]/a"
        self.youtube_xpath = "//body/footer/div/div/div[4]/ul/li[4]/a"
        self.instagram_xpath = "//body/footer/div/div/div[4]/ul/li[5]/a"
        self.carousal_id = "recipeCarousel"
        self.image_1_xpath = "//header/nav[1]/div[1]/a[1]/img[1]"
        self.image_2_xpath = "//body/section[2]/div[1]/div[2]/div[1]/div[1]/img[1]"
        self.image_3_xpath = "//body/section[2]/div[1]/div[2]/div[1]/div[2]/img[1]"
        self.image_4_xpath = "//body/section[2]/div[1]/div[2]/div[1]/div[3]/img[1]"
        self.image_5_xpath = "//body/section[2]/div[1]/div[2]/div[1]/div[4]/img[1]"
        self.image_6_xpath = "//body/section[2]/div[1]/div[2]/div[1]/div[5]/img[1]"
        self.image_7_xpath = "//body/footer[1]/div[1]/div[1]/div[1]/img[1]"
        self.about_img_1_xpath = "//body/section[1]/div/div/div[2]/img"
        self.about_img_2_xpath = "//body/section[3]/div/div/div[1]/div/div[1]/img"
        self.about_img_3_xpath = "//body/section[3]/div/div/div[2]/div/div[1]/img"
        self.about_img_4_xpath = "//body/section[3]/div/div/div[3]/div/div[1]/img"
        self.about_linked_in_1_xpath = "//body/section[3]/div/div/div[1]/div/div[2]/a"
        self.about_linked_in_2_xpath = "//body/section[3]/div/div/div[2]/div/div[2]/a"
        self.about_linked_in_3_xpath = "//body/section[3]/div/div/div[3]/div/div[2]/a"
        self.landing_page_text_xpath = "//li[contains(text(),'Legally Binding')]"
        self.about_page_header_xpath = "//*[contains(text(),'Millennium Infotech, Inc. is the company behind ')]"
        self.manufacturing_page_header_xpath = "//*[contains(text(),'MANUFACTURING')]"
        self.finance_page_header_xpath = "//*[contains(text(),'LEVERAGING ')]"
        self.professional_page_header_xpath = "//*[contains(text(),'Staffing ')]"
        self.real_estate_page_header_xpath = "//*[contains(text(),'REAL ESTATE')]"
        self.healthcare_estate_page_header_xpath = "//body/section[1]/div/div/div[1]/h3"
        self.healthcare_estate_page_header_xpath = "//body/section[1]/div/div/div[1]/h3"

    def landing_page_nav_bar_elements_redirection(self):
        About = self.driver.find_element(By.LINK_TEXT, self.about_link_text)
        self.driver.execute_script("arguments[0].click();", About)
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, self.about_page_header_xpath).is_displayed, "In About page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in About page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH, self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Manufacturing = self.driver.find_element(By.LINK_TEXT, self.manufacturing_link_text)
        self.driver.execute_script("arguments[0].click();", Manufacturing)
        time.sleep(2)
        #assert self.driver.title == "Signulu - Enhance Manufacturing Operations with E-signature Software", "Page title mismatched in Manufacturing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/manufacturing", "Page URL is mismatched in Manufacturing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        BankingAndFinance = self.driver.find_element(By.LINK_TEXT, self.banking_services_link_text)
        self.driver.execute_script("arguments[0].click();", BankingAndFinance)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Banking And Finance page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/finance", "Page URL is mismatched in Banking And Finance page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        ProfessionalServices = self.driver.find_element(By.LINK_TEXT, self.professional_services_link_text)
        self.driver.execute_script("arguments[0].click();", ProfessionalServices)
        time.sleep(2)
        #assert self.driver.title == "signulu", "Page title mismatched in Professional Services page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/professionalservices", "Page URL is mismatched in Professional Services page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        RealEstate = self.driver.find_element(By.LINK_TEXT, self.real_estate_link_text)
        self.driver.execute_script("arguments[0].click();", RealEstate)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Real Estate page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/realestate", "Page URL is mismatched in Real Estate page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Healthcare = self.driver.find_element(By.LINK_TEXT, self.healthcare_link_text)
        self.driver.execute_script("arguments[0].click();", Healthcare)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Healthcare page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/healthcare", "Page URL is mismatched in Healthcare page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH, self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Law = self.driver.find_element(By.LINK_TEXT, self.law_link_text)
        self.driver.execute_script("arguments[0].click();", Law)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Law page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/law", "Page URL is mismatched in Law page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        IT = self.driver.find_element(By.LINK_TEXT, self.it_link_text)
        self.driver.execute_script("arguments[0].click();", IT)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Law page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/it", "Page URL is mismatched in Landing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        self.driver.find_element(By.XPATH, self.image_1_xpath).click()
        Pricing = self.driver.find_element(By.LINK_TEXT, self.pricing_link_text)
        self.driver.execute_script("arguments[0].click();", Pricing)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Pricing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/pricing", "Page URL is mismatched in Pricing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        Blog = self.driver.find_element(By.LINK_TEXT, self.blog_link_text)
        self.driver.execute_script("arguments[0].click();", Blog)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Blog page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/bloglist", "Page URL is mismatched in Blog page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        Contact = self.driver.find_element(By.LINK_TEXT, self.contact_link_text)
        self.driver.execute_script("arguments[0].click();", Contact)
        time.sleep(6)
        #assert self.driver.title == "signulu", "Page title mismatched in Contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "Page URL is mismatched in Contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        Login = self.driver.find_element(By.LINK_TEXT, self.login_link_text)
        self.driver.execute_script("arguments[0].click();", Login)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Login page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/login", "Page URL is mismatched in Login page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH,self.landing_page_text_xpath).is_displayed(), "In Landing page header not displayed"
        assert self.driver.current_url == "https://qa.signulu.com/", "Page URL is mismatched in Landing page"

        StartTrial = self.driver.find_element(By.LINK_TEXT, self.start_trial_link_text)
        self.driver.execute_script("arguments[0].click();", StartTrial)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in StartTrial page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "Page URL is mismatched in StartTrial page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartTrial : Page URL is mismatched in Landing page"





    def landing_page_start_trail_buttons(self):
        StartFreeTrailBtn1 = self.driver.find_element(By.XPATH, self.start_free_trail_button1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn1)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn1)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn1 : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartFreeTrailBtn1 : Page URL is mismatched in Landing page"

        StartFreeTrailBtn2 = self.driver.find_element(By.XPATH, self.start_free_trail_button2_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn2)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn2)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn2 : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartFreeTrailBtn2 : Page URL is mismatched in Landing page"

        StartFreeTrailBtn3 = self.driver.find_element(By.XPATH, self.start_free_trail_button3_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn3)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn3)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn3 : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartFreeTrailBtn3 : Page URL is mismatched in Landing page"

        StartFreeTrailBtn4 = self.driver.find_element(By.XPATH, self.start_free_trail_button4_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn4)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn4)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn4 : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartFreeTrailBtn4 : Page URL is mismatched in Landing page"
        self.driver.refresh()
        time.sleep(2)
        try:

            StartFreeTrailBtn5 = self.driver.find_element(By.XPATH, self.start_free_trail_button5_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn5)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn5)
            time.sleep(2)
            assert self.driver.title == "Signulu", "Page title mismatched in register page"
            assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn5 : Page URL is mismatched in register page"
            self.driver.back()
            time.sleep(4)
            assert self.driver.title == "signulu", "Page title mismatched in Landing page"
            assert self.driver.current_url == "https://qa.signulu.com/index.php", "StartFreeTrailBtn5 : Page URL is mismatched in Landing page"

        except NoSuchElementException:
            print("============> exception handled for Start free trial button <================")

        FooterStartFreeTrailBtn = self.driver.find_element(By.XPATH, self.footer_start_free_trail_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", FooterStartFreeTrailBtn)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", FooterStartFreeTrailBtn)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "FooterStartFreeTrailBtn : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "FooterStartFreeTrailBtn : Page URL is mismatched in Landing page"
        time.sleep(2)

    def landing_page_know_more_buttons(self):
        KnowMoreBtn1 = self.driver.find_element(By.XPATH, self.know_more_button1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn1)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", KnowMoreBtn1)
        time.sleep(2)
        assert self.driver.title == "signulu", "Page title mismatched in contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn1 : Page URL is mismatched in contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "KnowMoreBtn1 : Page URL is mismatched in Landing page"

        KnowMoreBtn2 = self.driver.find_element(By.XPATH, self.know_more_button2_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn2)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", KnowMoreBtn2)
        time.sleep(2)
        assert self.driver.title == "signulu", "Page title mismatched in contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn2 : Page URL is mismatched in contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "KnowMoreBtn2 : Page URL is mismatched in Landing page"

        KnowMoreBtn3 = self.driver.find_element(By.XPATH, self.know_more_button3_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn3)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", KnowMoreBtn3)
        time.sleep(2)
        assert self.driver.title == "signulu", "Page title mismatched in contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn3 : Page URL is mismatched in contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "KnowMoreBtn3 : Page URL is mismatched in Landing page"

        KnowMoreBtn4 = self.driver.find_element(By.XPATH, self.know_more_button4_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn4)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", KnowMoreBtn4)
        time.sleep(2)
        assert self.driver.title == "signulu", "Page title mismatched in contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn4 : Page URL is mismatched in contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "KnowMoreBtn4 : Page URL is mismatched in Landing page"

        try:
            KnowMoreBtn5 = self.driver.find_element(By.XPATH, self.know_more_button5_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn5)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", KnowMoreBtn5)
            time.sleep(2)
            assert self.driver.title == "signulu", "Page title mismatched in contact page"
            assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn5 : Page URL is mismatched in contact page"
            self.driver.back()
            time.sleep(4)
            assert self.driver.title == "signulu", "Page title mismatched in Landing page"
            assert self.driver.current_url == "https://qa.signulu.com/index.php", "KnowMoreBtn5 : Page URL is mismatched in Landing page"
        except NoSuchElementException:
            print("============> exception handled for Know more button <================")
        time.sleep(2)

    def videos_validation(self):
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.video_1_xpath))
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.video_1_xpath))
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.video_1_xpath))
        self.driver.refresh()
        time.sleep(1)
        # Video 1 status checking
        Video1 = self.driver.find_element(By.XPATH, self.video_1_xpath)
        # Zoom out by reducing the zoom level
        time.sleep(2)
        self.driver.execute_script("document.body.style.zoom='33%'")
        is_video1_playing = self.driver.execute_script("return arguments[0].paused;", Video1)
        assert is_video1_playing == False, "======>The video_1 should be played, but it is not playing"
        # Pause the video
        self.driver.execute_script("arguments[0].pause();", Video1)
        is_video1_playing = self.driver.execute_script("return arguments[0].paused;", Video1)
        assert is_video1_playing == True, "The video_1 should not play, but it is playing"
        # Wait for 3 seconds
        time.sleep(3)
        # Enable autoplay using JavaScript
        self.driver.execute_script("arguments[0].play();", Video1)
        is_video1_playing = self.driver.execute_script("return arguments[0].paused;", Video1)
        assert is_video1_playing == False, "---->The video_1 should be played, but it is not playing"
        time.sleep(1)

        # Video 2 status checking
        Video2 = self.driver.find_element(By.XPATH, self.video_2_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Video2)
        is_video2_playing = self.driver.execute_script("return arguments[0].paused;", Video2)
        assert is_video2_playing == False, "The video_2 should be played, but it is not playing"
        # Pause the video
        self.driver.execute_script("arguments[0].pause();", Video2)
        is_video2_playing = self.driver.execute_script("return arguments[0].paused;", Video2)
        assert is_video2_playing == True, "The video_2 should not play, but it is playing"
        # Wait for 3 seconds
        time.sleep(3)
        # Enable autoplay using JavaScript
        self.driver.execute_script("arguments[0].play();", Video2)
        is_video2_playing = self.driver.execute_script("return arguments[0].paused;", Video2)
        assert is_video2_playing == False, "The video_2 should be played, but it is not playing"
        time.sleep(1)

        # Video 3 status checking
        Video3 = self.driver.find_element(By.XPATH, self.video_3_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Video3)
        is_video3_playing = self.driver.execute_script("return arguments[0].paused;", Video3)
        assert is_video3_playing == False, "The video_3 should be played, but it is not playing"
        # Pause the video
        self.driver.execute_script("arguments[0].pause();", Video3)
        is_video3_playing = self.driver.execute_script("return arguments[0].paused;", Video3)
        assert is_video3_playing == True, "The video_3 should not play, but it is playing"
        # Wait for 3 seconds
        time.sleep(3)
        # Enable autoplay using JavaScript
        self.driver.execute_script("arguments[0].play();", Video3)
        is_video3_playing = self.driver.execute_script("return arguments[0].paused;", Video3)
        assert is_video3_playing == False, "The video_3 should be played, but it is not playing"
        time.sleep(1)

        # Video 4 status checking
        Video4 = self.driver.find_element(By.XPATH, self.video_4_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Video4)
        is_video4_playing = self.driver.execute_script("return arguments[0].paused;", Video4)
        assert is_video4_playing == False, "The video_4 should be played, but it is not playing"
        # Pause the video
        self.driver.execute_script("arguments[0].pause();", Video4)
        is_video4_playing = self.driver.execute_script("return arguments[0].paused;", Video4)
        assert is_video4_playing == True, "The video_4 should not play, but it is playing"
        # Wait for 3 seconds
        time.sleep(3)
        # Enable autoplay using JavaScript
        self.driver.execute_script("arguments[0].play();", Video4)
        is_video4_playing = self.driver.execute_script("return arguments[0].paused;", Video4)
        assert is_video4_playing == False, "The video_4 should be played, but it is not playing"
        time.sleep(1)
        self.driver.execute_script("document.body.style.zoom = '100%'")
        self.driver.refresh()
        time.sleep(1)

    def social_media_icons(self):
        Facebook = self.driver.find_element(By.XPATH, self.facebook_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Facebook)
        time.sleep(2)
        assert self.driver.current_url == "https://www.facebook.com/signulu/", "Page URL is mismatched in Facebook page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "Page URL is mismatched in Landing page"

        Twitter = self.driver.find_element(By.XPATH, self.twitter_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Twitter)
        time.sleep(2)
        assert self.driver.current_url == "https://twitter.com/signulu", "Page URL is mismatched in twitter page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "Page URL is mismatched in Landing page"

        LinkedIn = self.driver.find_element(By.XPATH, self.linkedin_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", LinkedIn)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", LinkedIn)
        time.sleep(2)
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "Page URL is mismatched in Landing page"

        Youtube = self.driver.find_element(By.XPATH, self.youtube_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Youtube)
        time.sleep(2)
        assert self.driver.current_url == "https://www.youtube.com/channel/UCpYSuQ3xctOH7thHTHMmqQA?view_as=subscriber", "Page URL is mismatched in youtube page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "Page URL is mismatched in Landing page"

        Instagram = self.driver.find_element(By.XPATH, self.instagram_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Instagram)
        time.sleep(2)
        assert self.driver.current_url == "https://www.instagram.com/signulu/", "Page URL is mismatched in Instagram page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "Page URL is mismatched in Landing page"

    def carousels_validation(self):
        # Find the carousel element on the page
        Carousel = self.driver.find_element(By.ID, self.carousal_id)
        assert Carousel.is_displayed() == True, "The carousel is not visible on landing page"

    def landing_page_images_validation(self):
        Image_1 = self.driver.find_element(By.XPATH, self.image_1_xpath)
        assert Image_1.is_displayed() == True, "Image_1 is not visible on landing page"
        FooterStartFreeTrailBtn = self.driver.find_element(By.XPATH, self.footer_start_free_trail_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", FooterStartFreeTrailBtn)
        time.sleep(2)
        Image_2 = self.driver.find_element(By.XPATH, self.image_2_xpath)
        time.sleep(1)
        assert Image_2.is_displayed() == True, "Image_2 is not visible on landing page"
        Image_3 = self.driver.find_element(By.XPATH, self.image_3_xpath)
        assert Image_3.is_displayed() == True, "Image_3 is not visible on landing page"
        Image_4 = self.driver.find_element(By.XPATH, self.image_4_xpath)
        assert Image_4.is_displayed() == True, "Image_4 is not visible on landing page"
        Image_5 = self.driver.find_element(By.XPATH, self.image_5_xpath)
        assert Image_5.is_displayed() == True, "Image_5 is not visible on landing page"
        Image_6 = self.driver.find_element(By.XPATH, self.image_6_xpath)
        assert Image_6.is_displayed() == True, "Image_6 is not visible on landing page"
        Image_7 = self.driver.find_element(By.XPATH, self.image_7_xpath)
        assert Image_7.is_displayed() == True, "Image_7 is not visible on landing page"


    def about_page_nav_bar_elements_redirection(self):
        About = self.driver.find_element(By.LINK_TEXT, self.about_link_text)
        self.driver.execute_script("arguments[0].click();", About)
        time.sleep(2)

        SignuluLogo = self.driver.find_element(By.XPATH, self.image_1_xpath)
        self.driver.execute_script("arguments[0].click();", SignuluLogo)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php", "SignuluLogo : Page URL is mismatched in Landing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Manufacturing = self.driver.find_element(By.LINK_TEXT, self.manufacturing_link_text)
        self.driver.execute_script("arguments[0].click();", Manufacturing)
        time.sleep(2)
        #assert self.driver.title == "Signulu - Enhance Manufacturing Operations with E-signature Software", "Page title mismatched in Manufacturing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/manufacturing", "Page URL is mismatched in Manufacturing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "Manufacturing: Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        BankingAndFinance = self.driver.find_element(By.LINK_TEXT, self.banking_services_link_text)
        self.driver.execute_script("arguments[0].click();", BankingAndFinance)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Banking And Finance page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/finance", "Page URL is mismatched in Banking And Finance page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "BankingAndFinance : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        ProfessionalServices = self.driver.find_element(By.LINK_TEXT, self.professional_services_link_text)
        self.driver.execute_script("arguments[0].click();", ProfessionalServices)
        time.sleep(2)
        #assert self.driver.title == "signulu", "Page title mismatched in Professional Services page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/professionalservices", "Page URL is mismatched in Professional Services page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "ProfessionalServices : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        RealEstate = self.driver.find_element(By.LINK_TEXT, self.real_estate_link_text)
        self.driver.execute_script("arguments[0].click();", RealEstate)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Real Estate page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/realestate", "Page URL is mismatched in Real Estate page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "RealEstate : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Healthcare = self.driver.find_element(By.LINK_TEXT, self.healthcare_link_text)
        self.driver.execute_script("arguments[0].click();", Healthcare)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Healthcare page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/healthcare", "Page URL is mismatched in Healthcare page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "Healthcare : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        Law = self.driver.find_element(By.LINK_TEXT, self.law_link_text)
        self.driver.execute_script("arguments[0].click();", Law)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Law page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/law", "Page URL is mismatched in Law page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "Law : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.industries_menu_xpath).click()
        IT = self.driver.find_element(By.LINK_TEXT, self.it_link_text)
        self.driver.execute_script("arguments[0].click();", IT)
        time.sleep(2)
        #assert self.driver.title == "Signulu", "Page title mismatched in Law page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/it", "Page URL is mismatched in Landing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about#", "IT : Page URL is mismatched in About page"

        self.driver.find_element(By.XPATH, self.image_1_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.about_link_text).click()
        Pricing = self.driver.find_element(By.LINK_TEXT, self.pricing_link_text)
        self.driver.execute_script("arguments[0].click();", Pricing)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Pricing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/pricing", "Page URL is mismatched in Pricing page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Pricing : Page URL is mismatched in About page"

        Blog = self.driver.find_element(By.LINK_TEXT, self.blog_link_text)
        self.driver.execute_script("arguments[0].click();", Blog)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Blog page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/bloglist", "Page URL is mismatched in Blog page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Blog : Page URL is mismatched in About page"

        Contact = self.driver.find_element(By.LINK_TEXT, self.contact_link_text)
        self.driver.execute_script("arguments[0].click();", Contact)
        time.sleep(6)
        #assert self.driver.title == "signulu", "Page title mismatched in Contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "Page URL is mismatched in Contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Contact : Page URL is mismatched in About page"

        Login = self.driver.find_element(By.LINK_TEXT, self.login_link_text)
        self.driver.execute_script("arguments[0].click();", Login)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in Login page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/login", "Page URL is mismatched in Login page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Login : Page URL is mismatched in About page"

        StartTrial = self.driver.find_element(By.LINK_TEXT, self.start_trial_link_text)
        self.driver.execute_script("arguments[0].click();", StartTrial)
        time.sleep(6)
        #assert self.driver.title == "Signulu", "Page title mismatched in StartTrial page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "Page URL is mismatched in StartTrial page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "StartTrial : Page URL is mismatched in About page"


    def about_page_start_trail_buttons(self):
        StartFreeTrailBtn1 = self.driver.find_element(By.XPATH, self.start_free_trail_button1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", StartFreeTrailBtn1)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", StartFreeTrailBtn1)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "StartFreeTrailBtn1 : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "StartFreeTrailBtn1 : Page URL is mismatched in About page"

        FooterStartFreeTrailBtn = self.driver.find_element(By.XPATH, self.footer_start_free_trail_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", FooterStartFreeTrailBtn)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", FooterStartFreeTrailBtn)
        time.sleep(2)
        assert self.driver.title == "Signulu", "Page title mismatched in register page"
        assert self.driver.current_url == "https://appqa.signulu.com/account/register", "FooterStartFreeTrailBtn : Page URL is mismatched in register page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "FooterStartFreeTrailBtn : Page URL is mismatched in About page"
        time.sleep(2)

    def about_page_know_more_buttons(self):
        KnowMoreBtn1 = self.driver.find_element(By.XPATH, self.know_more_button1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", KnowMoreBtn1)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", KnowMoreBtn1)
        time.sleep(2)
        assert self.driver.title == "signulu", "Page title mismatched in contact page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/contact", "KnowMoreBtn1 : Page URL is mismatched in contact page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "KnowMoreBtn1 : Page URL is mismatched in About page"

    def about_page_images_validation(self):
        Image_1 = self.driver.find_element(By.XPATH, self.image_1_xpath)
        assert Image_1.is_displayed() == True, "Image_1 is not visible on About page"
        About_page_image_1 = self.driver.find_element(By.XPATH, self.about_img_1_xpath)
        assert About_page_image_1.is_displayed() == True, "About_page_image_1 is not visible on About page"
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.footer_start_free_trail_button_xpath))
        time.sleep(1)
        About_page_image_2 = self.driver.find_element(By.XPATH, self.about_img_2_xpath)
        assert About_page_image_2.is_displayed() == True, "About_page_image_2 is not visible on About page"
        About_page_image_3 = self.driver.find_element(By.XPATH, self.about_img_3_xpath)
        assert About_page_image_3.is_displayed() == True, "About_page_image_3 is not visible on About page"
        About_page_image_4 = self.driver.find_element(By.XPATH, self.about_img_4_xpath)
        assert About_page_image_4.is_displayed() == True, "About_page_image_4 is not visible on About page"

        FooterStartFreeTrailBtn = self.driver.find_element(By.XPATH, self.footer_start_free_trail_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", FooterStartFreeTrailBtn)
        time.sleep(2)

        AboutFooterImage = self.driver.find_element(By.XPATH, self.image_7_xpath)
        assert AboutFooterImage.is_displayed() == True, "AboutFooterImage is not visible on About page"

    def about_page_social_media_icons(self):
        About = self.driver.find_element(By.LINK_TEXT, self.about_link_text)
        self.driver.execute_script("arguments[0].click();", About)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, self.about_linked_in_1_xpath))
        LinkedIn_1 = self.driver.find_element(By.XPATH, self.about_linked_in_1_xpath)
        self.driver.execute_script("arguments[0].click();", LinkedIn_1)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        LinkedIn_2 = self.driver.find_element(By.XPATH, self.about_linked_in_2_xpath)
        LinkedIn_2.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        LinkedIn_3 = self.driver.find_element(By.XPATH, self.about_linked_in_3_xpath)
        LinkedIn_3.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        Facebook = self.driver.find_element(By.XPATH, self.facebook_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Facebook)
        time.sleep(2)
        assert self.driver.current_url == "https://www.facebook.com/signulu/", "Page URL is mismatched in Facebook page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in Landing page"

        Twitter = self.driver.find_element(By.XPATH, self.twitter_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Twitter)
        time.sleep(2)
        assert self.driver.current_url == "https://twitter.com/signulu", "Page URL is mismatched in twitter page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in Landing page"

        LinkedIn = self.driver.find_element(By.XPATH, self.linkedin_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", LinkedIn)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", LinkedIn)
        time.sleep(2)
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in Landing page"

        Youtube = self.driver.find_element(By.XPATH, self.youtube_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Youtube)
        time.sleep(2)
        assert self.driver.current_url == "https://www.youtube.com/channel/UCpYSuQ3xctOH7thHTHMmqQA?view_as=subscriber", "Page URL is mismatched in youtube page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in Landing page"

        Instagram = self.driver.find_element(By.XPATH, self.instagram_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", Instagram)
        time.sleep(2)
        assert self.driver.current_url == "https://www.instagram.com/signulu/", "Page URL is mismatched in Instagram page"
        self.driver.back()
        time.sleep(4)
        assert self.driver.title == "signulu", "Page title mismatched in Landing page"
        assert self.driver.current_url == "https://qa.signulu.com/index.php/about", "Page URL is mismatched in Landing page"


