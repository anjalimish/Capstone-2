import unittest
#test
from selenium import webdriver
import os
from selenium.webdriver.common import keys
#driver = webdriver.firefox(excecutable_path= r'../../main/python/driver/geckodriver.exe')
driver = webdriver.Chrome(executable_path=r"/path/to/chromedriver")
driver.get('http://localhost:9090')
sbutton = driver.find_element_by_class_name("testbtn")
sbutton.click()
driver.find_element_by_class_name("testbtn1").send_keys(os.getcwd()+"\\Un.png")
driver.find_element_by_class_name("testbtn2").click()
import time
time.sleep(90)
z=driver.find_element_by_class_name("btn4").text
print(z)
class webTest(unittest.TestCase):
    def test_get(self):
        self.assertEquals(self.z,"info")
