import os
import sys
import pickle
from env import *
from time import gmtime, strftime,sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options




login_url = 'https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F'
chrome_options = Options()
WAIT_TIMEOUT = 5
path = os.path.dirname(os.path.abspath(__file__))
chrome_options.page_load_strategy = 'eager'
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)

def saveCookie(self, cookieName):
     with open(self.path + '/' + cookieName, 'wb') as filehandler:
        pickle.dump(self.driver.get_cookies(), filehandler)
     print("save user {}".format(cookieName))

def loadCookie(self, cookieName):
        with open(self.path + '/' + cookieName, 'rb') as cookiesfile:
            for cookie in pickle.load(cookiesfile):
                driver.add_cookie(cookie)

def loginByCookie(cookieName):
        try:
            self.loadCookie(cookieName)
            self.driver.refresh()
            print("login {}".format(cookieName))
        except Exception as e:
            print("{} cookie not found".format(cookieName))

def checkPopModal():
        try:
            sleep(3)
            pop = driver.find_element_by_css_selector("POP_MODAL")
            pop.click()
        except :
            print("no modal found")
         

def checkLogin():
        try:
        
            WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located(("css", "AVATAR"))
            )
            print("Login Success")
            return True
        except Exception as e:
            print("Login Failed")
            return False

def purchase(phone, password, item_url,cookieName):
    driver.get(login_url)
    checkPopModal()

    loginByCookie(cookieName)
    if not checkLogin():
        WebDriverWait(driver,WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.NAME, 'loginKey')))
        driver.find_element_by_name('loginKey').send_keys(phone)
        driver.find_element_by_name('password').send_keys(password + Keys.RETURN)
        otp = str (send_OTP())
        driver.find_element_by_css_selector('input[autocomplete="one-time-code"]').send_keys(otp + Keys.RETURN)
        WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.NAME, 'navbar__username')))

    self.saveCookie(cookieName)
    driver.get(item_url)
    #use this if variant more than 1
    # variant_XPATH = "//button[contains(., 'Red')]"
    buy_XPATH = "//button[contains(., 'beli sekarang')]"
    checkout_XPATH == "//button[contains(., 'checkout')]"
    buat_XPATH == "//button[contains(., 'Buat Pesanan')]"

    driver.find_element_by_xpath(buy_XPATH).click()

    wait.until(presence_of_element_located((By.XPATH, checkout_XPATH)))
    driver.find_element_by_xpath(checkout_XPATH).click()

    wait.until(presence_of_element_located((By.XPATH, buat_XPATH)))
    # use this for auto checkout
    # driver.find_element_by_xpath(buat_XPATH).click()

def send_OTP():
    text = str(input ("Enter OTP: "))
    return text
#fill user and pass 
phone = '' 
password = '' 
#item url flashsale
item_url = 'https://shopee.co.id/Apple-iPhone-11-Pro-512GB-Midnight-Green-i.255563049.6435648695'

purchase(phone, password, item_url, cookie_name)
