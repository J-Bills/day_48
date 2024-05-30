from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"{price_dollar.text}.{price_cent.text}")

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(doc_link)
# submit_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug.text)

#Challenge:

event_menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events  = event_menu.find_elements(By.TAG_NAME, value='li')

event_dict ={
    
}

for index, e in enumerate(events):
    result = e.text.split('\n')
    event  = {'time' :result[0], 'name':result[1]}
    event_dict[str(index)] = event

print(event_dict)
#driver.quit()