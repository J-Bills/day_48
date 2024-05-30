from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.wikipedia.org/wiki/Main_Page")

article_count_id = driver.find_element(By.ID, value='articlecount')
article_num = article_count_id.find_element(By.LINK_TEXT, value='6,829,029')


print(article_num.text)

driver.quit()