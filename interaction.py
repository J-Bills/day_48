from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.wikipedia.org/wiki/Main_Page")
driver.implicitly_wait(5)
# driver.refresh()

# article_count_id = driver.find_element(By.ID, value='articlecount')
# article_num = article_count_id.find_element(By.CSS_SELECTOR, value='#articlecount a')

#Clicking on Links
# all_portals =driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

#Finding search input my name
search = driver.find_element(By.NAME, value='search')
print(search.get_attribute('name'))

#input text in search field
search.send_keys('Python', Keys.ENTER)


