from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"{price_dollar.text}.{price_cent.text}")

search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.get_attribute('placeholder'))

#driver.close()
driver.quit()