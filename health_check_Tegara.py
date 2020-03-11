#from bs4 import BeautifulSoup as bs
#from requests import Session
#use session object 
#Requests session is used when you intend keeping the context of a request, so the cookies and all information of that request session can be stored.
#The post method is used to send a post request with the parameters and log us in.


# with Session() as s:
#     site = s.get('https://app.tegara.jp/login')
#     #print(site.content)
#     bs_content = bs(site.content,"html.parser")
#     login_data = {"loginId":"b.mushtaq@z-planet.co.jp","loginPassword":"9ScxJ6jCEpmV33v"}
#     s.post("https://app.tegara.jp/login",login_data)
#     home_page = s.get("https://app.tegara.jp/user/weather/")
   
#     soup = bs(home_page.content,"html.parser")
#     print(soup)
#     form_element = soup.find('input-weather')
#     print('This is the static html data :- ',form_element)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium .common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = False
options.add_argument("--window-size=500,500")

driver = webdriver.Chrome(options=options,executable_path="C:\\Users\\b.mushtaq\\Documents\\chromedriver.exe")

def login():
    driver.get("https://app.tegara.jp/login")
    #print(driver.page_source)
    driver.find_element_by_name("loginId").send_keys("b.mushtaq@z-planet.co.jp")
    driver.find_element_by_name("loginPassword").send_keys("9ScxJ6jCEpmV33v")
    driver.find_element_by_id("login_btn").click()
    ##driver.save_screenshot('CREEP.png')
    try:
        button = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"panel-btn")))
        print('successfully loigged in')
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        #print(html)
                         
        
        print("///////")
        home()

    except NoSuchElementException:
        print('Incorrect login/password')
        
    finally:
        time.sleep(3)
        driver.quit()
def home():
    select_date = driver.find_element_by_class_name("calender").click()
login()
home()

