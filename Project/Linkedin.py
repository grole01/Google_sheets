from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#path=(r"C:\pythonProject1\chromedriver")
driver=webdriver.Chrome()#(path)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
#driver.page_source

username=driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("adujmic1@gmail.com")
password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("18092004")
sign_in=driver.find_element_by_xpath('//*[@id="app__container"]/main/div[3]/form/div[3]/button').click()

driver=webdriver.Chrome()#(path)
driver.get("https://www.google.com/")
sleep(2)
driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()
sleep(5)