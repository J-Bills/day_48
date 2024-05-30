from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.wikipedia.org/wiki/Main_Page")
driver.get('http://secure-retreat-92358.herokuapp.com')
driver.implicitly_wait(5)
# driver.refresh()

# article_count_id = driver.find_element(By.ID, value='articlecount')
# article_num = article_count_id.find_element(By.CSS_SELECTOR, value='#articlecount a')

#Clicking on Links
# all_portals =driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

#Finding search input my name
fnsearch = driver.find_element(By.NAME, value='fName')

lnsearch = driver.find_element(By.NAME, value='lName')

emailsearch = driver.find_element(By.NAME, value='email')

submit = driver.find_element(By.TAG_NAME, value='button')
print(submit.get_attribute('type'))


#input text in search field
fnsearch.send_keys('FirstName')
lnsearch.send_keys('LastName')
emailsearch.send_keys('emailaddress@origin.com')
submit.click()
