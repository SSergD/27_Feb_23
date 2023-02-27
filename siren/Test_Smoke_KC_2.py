import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # говорим WebDriver исчет каждый элемент в течение 5 секунд

browser.get('https://hb-zeta.stage.sirenltd.dev/')

browser.find_element(By.XPATH, "//div[@class='verticalsList--arrow']").click()  # переходим на WIS
browser.find_element(By.XPATH, "//div[@data-link='/kitchen-cabinets']").click()
browser.find_element(By.XPATH, "//button[@class='Button Btn BtnPrimary']").click()

zipcode = ['33773', '33773', '33773']
Zip = browser.find_element(By.XPATH, "//input[@placeholder='Enter ZIP Code']")  # Рандомный выбор ZIP
Zip.send_keys(random.choice(zipcode))
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Button Btn BtnPrimary']"))).click()
# 1 Choose your kitchen layout
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[src*='step1_1.svg']"))).click()
def buttonNext():
    butnex = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Btn BtnPrimary Button"]')))
    butnex.click()
buttonNext()
# 2 Approximate age of your kitchen
WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[src*='step2_2.svg']"))).click()
buttonNext()

name =  browser.find_element(By.XPATH, '//input[@name="fullName"]').send_keys('testS siren')
nowe = datetime.datetime.today().strftime("%d-%m-%H-%M-%S") + "_KC@sirenltd.com"
email = browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(nowe)
buttonNext()


nowt = "704308" + datetime.datetime.today().strftime("%M%S")
phone = browser.find_element(by="xpath", value='//input[@name="phoneNumber"]').send_keys(nowt)

browser.find_element(by="xpath", value="//span[@style and text() = 'Submit my request']").click()
time.sleep(2)

try:
    browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").click()
    print('Smoke_KC_confirmed')
except NoSuchElementException:
    print('Smoke_KC_confirmed (no phone confirmation)')

print(nowe)
print(nowt)