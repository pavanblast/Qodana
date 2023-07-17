import json
import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from Features.PageObjects.HomePage import HomePage
from Features.PageObjects.InPersonSign import InPersonSign
from Features.PageObjects.RegistrationPageOnMobile import RegistrationPageOnMobile
from PageObjects.BasePage import BasePage
from PageObjects.LoginPage import LoginPage
from PageObjects.WebsitePages import WebsitePages
from PageObjects.ReportsPage import ReportsPage
from PageObjects.LiteuserValidDocumentsUploadVerification import LiteuserValidDocumentsUploadVerification

data = json.load(open("Resources/config.json"))


# This environment page is used as hooks page. Here we can notice that we have used before, after hooks along side
# with some step hooks. 

def before_scenario(context, scenario):
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    # }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    time.sleep(5)
    basepage = BasePage(context.driver)
    context.loginpage = LoginPage(basepage)
    context.websitepages = WebsitePages(basepage)
    context.liteuserpages = LiteuserValidDocumentsUploadVerification(basepage)
    context.homepage = HomePage(basepage)
    context.inpersonsign = InPersonSign(basepage)
    context.registrationpageonmobile = RegistrationPageOnMobile(basepage)
    context.reportspage = ReportsPage(basepage)
    context.stepid = 1
    context.driver.get(data['ApplicationURL'])
    # context.driver.get(data['LiteUserURL'])
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    time.sleep(3)


def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    pass
    #context.driver.close()
