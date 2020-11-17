from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('https://web.whatsapp.com/')
driver.find_element_by_xpath('//span[contains(text(),"Jitesh New")]').click()
input_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]')
send = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
while True:
    input_box.send_keys(':devil' u'\ue007')
    input_box.send_keys(Keys.ENTER)
