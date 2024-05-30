from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

def getMoney():
    money = driver.find_element(By.ID, value='money')
    return int(money.text)

cookie = driver.find_element(By.ID, value='cookie')
cookie.click()



factory = driver.find_element(By.ID, value="buyFactory")
mine = driver.find_element(By.ID, value="buyMine")
shipment = driver.find_element(By.ID, value="buyShipment")
lab = driver.find_element(By.ID, value="buyAlchemy lab")
portal = driver.find_element(By.ID, value="buyTime machine")

def getCursor():
    cursor = driver.find_element(By.ID, value="buyCursor")
    cursor_cost = cursor.find_element(By.TAG_NAME, value='b')
    labels = cursor_cost.text.split(" ")
    cursor_cost = int(labels[len(labels)-1])
    return cursor_cost

def getGrandma():
    grandma = driver.find_element(By.ID, value="buyGrandma")
    grandma_cost = grandma.find_element(By.TAG_NAME, value='b')
    labels = grandma_cost.text.split(" ")
    grandma_cost = int(labels[len(labels)-1])
    return grandma_cost
    
def getFactory():
    factory = driver.find_element(By.ID, value="buyFactory")
    factory_cost = factory.find_element(By.TAG_NAME, value='b')
    labels = factory_cost.text.split(" ")
    factory_cost = int(labels[len(labels)-1])
    return factory_cost

def getMine():
    mine = driver.find_element(By.ID, value="buyMine")
    mine_cost = mine.find_element(By.TAG_NAME, value='b')
    labels = mine_cost.text.split(" ")
    mine_cost = int(labels[len(labels)-1].replace(',', ""))
    return mine_cost

def getShipment():
    shipment = driver.find_element(By.ID, value="buyShipment")
    shipment_cost = shipment.find_element(By.TAG_NAME, value='b')
    labels = shipment_cost.text.split(" ")
    shipment_cost = int(labels[len(labels)-1].replace(',', ""))
    return shipment_cost

def getLab():
    lab = driver.find_element(By.ID, value="buyAlchemy lab")
    lab_cost = lab.find_element(By.TAG_NAME, value='b')
    labels = lab_cost.text.split(" ")
    lab_cost = int(labels[len(labels)-1].replace(',', ""))
    return lab_cost

def getPortal():
    portal = driver.find_element(By.ID, value="buyTime machine")
    portal_cost = portal.find_element(By.TAG_NAME, value='b')
    labels = portal_cost.text.split(" ")
    portal_cost = int(labels[len(labels)-1].replace(',', ""))
    return portal_cost



duration = 5*60

start_time = time.time()

while time.time() - start_time < duration:
    cookie.click()
    time.sleep(1)
    end_time = time.time()
    print('time:', end_time - start_time)
    if (end_time - start_time) > 5:
        end_time = 0
        money = getMoney()
        cc = getCursor()
        gc = getGrandma()
        fc = getFactory()
        print(fc)
        mc = getMine()
        sc = getShipment()
        lc = getLab()
        pc = getPortal()
        
        if money >= cc:
            cursor = driver.find_element(By.ID, value="buyCursor")
            cursor.click()
            print("bought cursor")
        elif money >=gc:
            grandma = driver.find_element(By.ID, value="buyGrandma")
            grandma.click()
        elif money >=fc:
            factory = driver.find_element(By.ID, value="buyFactory")
            factory.click()
        elif money >=mc:
            mine = driver.find_element(By.ID, value="buyMine")
            mine.click()
        elif money >=sc:
            shipment = driver.find_element(By.ID, value="buyShipment")
            shipment.click()
        elif money >=lc:
            lab = driver.find_element(By.ID, value="buyAlchemy lab")
            lab.click()
        elif money >=pc:
            portal = driver.find_element(By.ID, value="buyTime machine")
            portal.click()
