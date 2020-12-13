from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
driver.get("http://localhost:9090/")
print(driver.title)
print(driver.current_url)
search_form = driver.find_element_by_name('file')
search_form.send_keys('C:/Users/Dell/Documents/capstone2/static/test1.jpg')
search_form.submit()
search = driver.find_element_by_id('info')
search.submit()