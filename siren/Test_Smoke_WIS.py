import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # говорим WebDriver исчет каждый элемент в течение 5 секунд

browser.get('https://hb-zeta.stage.sirenltd.dev/')

browser.find_element(By.XPATH, "//div[@class='verticalsList--arrow']").click()  # переходим на WIS
browser.find_element(By.XPATH, "//div[@data-link='/walk-in-showers']").click()
browser.find_element(By.XPATH, "//button[@class='Button Btn BtnPrimary verticalsList--btn']").click()

zipcode = ['00001', '00001', '00001']
Zip = browser.find_element(By.XPATH, "//input[@placeholder='Enter ZIP Code']")  # Рандомный выбор ZIP
Zip.send_keys(random.choice(zipcode))
browser.find_element(By.XPATH, "//button[@class='Button Btn BtnPrimary']").click()

WebDriverWait(browser, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/walk-in-showers/form/step1_1.svg"]'))).click()    # wizard 1
def buttonNext():
    butnex = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="Btn BtnPrimary Button"]')))
    butnex.click()
buttonNext()

WebDriverWait(browser, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/walk-in-showers/form/step2_2.svg"]'))).click()    # wizard 2
buttonNext()

WebDriverWait(browser, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/walk-in-showers/form/step3_3.svg"]'))).click()    # wizard 3
buttonNext()

def AnswerYes():
    WebDriverWait(browser, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/shared1/yes-icon.svg"]'))).click()
AnswerYes()
buttonNext()
time.sleep(1)

def AnswerNo():
    WebDriverWait(browser, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/shared1/no-icon.svg"]'))).click()
AnswerNo()
buttonNext()
time.sleep(1)

AnswerYes(), buttonNext()
time.sleep(1)
AnswerNo(), buttonNext()

#seni = browser.find_element(By.XPATH, "//div[contains (text(), 'Senior 65+')]").text
#sen = 'Senior 65+'

#if  seni == sen:
#    WebDriverWait(browser, 3).until(
#    EC.element_to_be_clickable((By.XPATH, '//img[@src="/static/walk-in-showers/form/discount1.svg"]'))).click()

#    buttonNext()
#pass

name = browser.find_element(by="xpath", value='//input[@name="fullName"]').send_keys('testS siren')
nowe = datetime.datetime.today().strftime("%d-%m-%H-%M-%S") + "@sirenltd.com"
email = browser.find_element(by="xpath", value='//input[@name="email"]').send_keys(nowe)
buttonNext()

nowt = "704308" + datetime.datetime.today().strftime("%M%S")
phone = browser.find_element(by="xpath", value='//input[@name="phoneNumber"]').send_keys(nowt)

browser.find_element(by="xpath", value="//span[@style and text() = 'Submit my request']").click()
time.sleep(2)
xyz = browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").text
y = 'Phone number is correct'

#if xyz == y:
#    browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").click()
#    time.sleep(2)
#else:
#    print('No')

browser.find_element(by="xpath", value="//h4[contains(text(), 'Thank you')]")