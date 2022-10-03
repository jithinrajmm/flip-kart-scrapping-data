from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
 
# create webdriver object
driver = webdriver.Firefox()
 
 
# get geeksforgeeks.org
driver.get("https://www.flipkart.com/")
 
# get element
element = driver.find_element(By.NAME,value='q')
element.send_keys("Hey, Tecadmin")
element.send_keys(Keys.RETURN)

 
# send keys
element.send_keys("Arrays")
time.sleep(20)
driver.close()