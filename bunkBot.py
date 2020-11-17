from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import getpass

meetHome="https://meet.google.com"
emailId=str(input('Enter your email id:'))
password=getpass.getpass()

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

driver=webdriver.Chrome()
driver.implicitly_wait(30)

def getLink():
    driver.get('https://web.whatsapp.com/')
    driver.find_element_by_xpath('//span[contains(text(),"Jitesh New")]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div[1]/button[3]').click()
    classLink=driver.find_elements_by_class_name('_1vUBq')[0].get_attribute('title')
    return classLink

def gmailLogin():
    global driver
    print("\nStarting Login process!\n")
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(emailId)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

"""     print("[+] Opening Google chrome")
    driver.get(meetHome)
    time.sle
    signin=driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a')
    signin.click()
    emailField=driver.find_element_by_xpath('//*[@id="identifierId"]')
    emailField.clear()
    emailField.send_keys(emailId)
    emailButton=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    emailButton.click()
    time.sleep(5)
    passField=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passField.clear()
    passField.send_keys(password)
    loginButton=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
    loginButton.click()
    print("[+] Gmail login successful") """

def joinMeet():
    print(classLink)
    driver.get(classLink)
    time.sleep(1005)
    dismiss=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
    dismiss.click()
    print("[+] Microphone turned off")
    print("[+] Camera turned off")
    time.sleep(8)
    join=driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
    join.click()
    print("[+] Class joined")
    time.sleep(5)
    try:
        closeInfo=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div[3]/div')
        closeInfo.click()
    except:
        pass

while True:
    classLink = getLink()
    print(str(classLink)[:24])
    if str(classLink)[:24]=="https://meet.google.com/":
        gmailLogin()
        joinMeet()
    else:
        print("link not valid")
    
time.sleep(10)
