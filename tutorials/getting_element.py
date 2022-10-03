from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from credentials import username,passwords


driver = webdriver.Firefox()

driver.get('https://www.linkedin.com/')
time.sleep(2)
user_name = driver.find_element(By.ID,'session_key')
password = driver.find_element(By.ID,'session_password')
user_name.send_keys(username)

password.send_keys(passwords)
time.sleep(3)

button = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button')
button.click()
time.sleep(3)
drop_down = driver.find_element(By.ID,'ember18')
drop_down.click()
time.sleep(3)
search = driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
search.send_keys('konsultera solutions')
time.sleep(2)
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.ENTER)
time.sleep(4)
view_konsultera = driver.find_element(By.XPATH,"//a[@class='app-aware-link artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary']")
view_konsultera.click()
time.sleep(4)

website = driver.find_element(By.XPATH,"//a[@class='ember-view org-top-card-primary-actions__action']")
website.click()


