import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # говорим WebDriver исчет каждый элемент в течение 5 секунд

browser.get('https://hb-zeta.stage.sirenltd.dev/')

browser.find_element(By.XPATH, "//div[@class='verticalsList--arrow']").click()  # переходим на KR
browser.find_element(By.XPATH, "//div[@data-link='/kitchen-remodeling']").click()
browser.find_element(By.XPATH, "//button[@class='Button Btn BtnPrimary verticalsList--btn']").click()

zipcode = ['33773', '33773', '33773']
Zip = browser.find_element(By.XPATH, "//input[@placeholder='Enter ZIP Code']")  # Рандомный выбор ZIP
Zip.send_keys(random.choice(zipcode))
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Button Btn BtnPrimary']"))).click()

# 1 Which elements of the kitchen would you like to update?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Kitchen Cabinets')]"))).click()
def buttonNext():
    butnex = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Button--content']")))
    butnex.click()
    time.sleep(1)
buttonNext()
# 2 What would you like to do with your kitchen cabinets?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Replace all or most cabinets')]"))).click()
buttonNext()
# 3 What type of property is this?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Single family home')]"))).click()
buttonNext()
# 4 Is it a mobile, modular or manufactured home?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'No')]"))).click()
buttonNext()
# 5 Are you the homeowner or authorized to make property changes?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Yes')]"))).click()
buttonNext()
# 6 What is the approximate size of your kitchen in sqft?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not sure')]"))).click()
buttonNext()
# 7 Do you know what your approximate budget is?
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not sure')]"))).click()
buttonNext()

Email = []
Phone = []

name =  browser.find_element(By.XPATH, '//input[@name="fullName"]').send_keys('testS siren')
nowe = datetime.datetime.today().strftime("%d-%m-%H-%M-%S") + "_KC@sirenltd.com"
email = browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(nowe)
Email.append(nowe)
buttonNext()

nowt = "704308" + datetime.datetime.today().strftime("%M%S")
phone = browser.find_element(by="xpath", value='//input[@name="phoneNumber"]').send_keys(nowt)
Phone.append(nowt)

browser.find_element(by="xpath", value="//span[@style and text() = 'Submit my request']").click()

try:
    browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").click()
    print('Smoke_KC_confirmed')
except NoSuchElementException:
    print('Smoke_KC_confirmed (no phone confirmation)')

KC_dict = {'Email': Email, 'Phone': Phone}
df_headlines = pd.DataFrame(KC_dict)
df_headlines.to_csv('12345.csv')
browser.quit()

print(nowe)
print(nowt)