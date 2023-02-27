import select
import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.get('https://hb-zeta.stage.sirenltd.dev/')
time.sleep(2)

dropdown = Select(browser.find_element(By.TAG_NAME, 'display: block;'))
select.select_by_value('1')
#browser.find_element(by='xpath', value="//div[@class='verticalsList--body w-100']").click()
WIS = browser.find_element(by='xpath', value='//div[@data-link="/walk-in-showers"]').click()
time.sleep(1)

button = browser.find_element(by="xpath", value="//button[@class='Button Btn BtnPrimary']").click()
time.sleep(2)

#After HomePage

zipcode = ['00001', '00001', '00001']
Zip = browser.find_element(by="xpath", value="//input[@placeholder='Enter ZIP Code']")
Zip.send_keys(random.choice(zipcode))

button = browser.find_element(by="xpath", value="//button[@class='Button Btn BtnPrimary']").click()

time.sleep(4)

wizard11 = browser.find_element(by="xpath", value="//*[contains(text(), 'Ease')]")
wizard12 = browser.find_element(by="xpath", value="//*[contains(text(), 'Safer')]")

def notsure():
    browser.find_element(by="xpath", value="//*[contains(text(), 'Not sure')]")

wizard10 = [notsure(), wizard12, wizard11]
wizClick1 = random.choice(wizard10)
wizClick1.click()

def buttonNext():
    time.sleep(1)
    browser.find_element(by="xpath", value="//span[@style and text() = 'Next']").click()
    time.sleep(2.5)
buttonNext()

wizard21 = browser.find_element(by="xpath", value="//*[contains(text(), 'Tub ')]")
wizard22 = browser.find_element(by="xpath", value="//*[contains(text(), 'Shower ')]")
wizard20 = [notsure(), wizard22, wizard21]
wizClick2 = random.choice(wizard20)
wizClick2.click()


buttonNext()

wizard31 = browser.find_element(by="xpath", value="//*[contains(text(), 'Against 1')]")
wizard32 = browser.find_element(by="xpath", value="//*[contains(text(), 'Against 2')]")
wizard30 = [notsure(), wizard32, wizard31]
wizClick3 = random.choice(wizard30)
wizClick3.click()

buttonNext()

def AnswerNo():
    browser.find_element(by="xpath", value="//div[@class and text() = 'No']").click()
AnswerNo()

def Continue():
        browser.find_element(by="xpath", value="// div[contains(text(), 'continue?')]")
        time.sleep(0.3)

Continue()

def AnswerYes():
    browser.find_element(by="xpath", value="//div[@class and text() = 'Yes']").click()

AnswerYes(), buttonNext()

AnswerYes(), Continue()

AnswerNo(), buttonNext()

AnswerNo(), Continue()

AnswerYes(), buttonNext()

AnswerYes(), Continue()

AnswerNo(), buttonNext()
time.sleep(1)

seni = browser.find_element(by="xpath", value="//div[contains (text(), 'Senior 65+')]").text
sen = 'Senior 65+'


if  seni == sen:
    wizardSeni1 = browser.find_element(by="xpath", value="//div[contains(text(), 'Senior 65')]")
    wizardSeni2 = browser.find_element(by="xpath", value="//div[contains(text(), 'Military')]")
    wizardSeni3 = browser.find_element(by="xpath", value="//div[contains(text(), 'None')]")
    wizardSeni0 = [wizardSeni1, wizardSeni2, wizardSeni3]
    wizClick4 = random.choice(wizardSeni0).click()

    buttonNext()
else:
    pass

def NameEmail():
    name = browser.find_element(by="xpath", value='//input[@name="fullName"]').send_keys('testS siren')
    nowe = datetime.datetime.today().strftime("%d-%m-%H-%M-%S") + "@sirenltd.com"
    email = browser.find_element(by="xpath", value='//input[@name="email"]').send_keys(nowe)
    buttonNext()
NameEmail()

def Telephone():
    nowt = "704308" + datetime.datetime.today().strftime("%M%S")
    phone = browser.find_element(by="xpath", value='//input[@name="phoneNumber"]').send_keys(nowt)
Telephone()

browser.find_element(by="xpath", value="//span[@style and text() = 'Submit my request']").click()
time.sleep(2)
xyz = browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").text
y = 'Phone number is correct'

if xyz == y:
    browser.find_element(by="xpath", value="//span[@style and text() = 'Phone number is correct']").click()
    time.sleep(2)
    browser.find_element(by="xpath", value="//h4[contains(text(), 'Thank you')]")
else:
    print('No')
