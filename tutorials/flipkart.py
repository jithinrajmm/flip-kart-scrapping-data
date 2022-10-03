from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# action chaining 
from selenium.webdriver import ActionChains
# for chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# time
import time
# requests
import requests
# beatiful soap
from bs4 import BeautifulSoup
# csv
import csv
# path specificaiton
import os

search_name = 'black berry phones'

driver = webdriver.Firefox()

driver.maximize_window()
time.sleep(2)

 
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.flipkart.com/')

# login_close = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
# if login_close:
#     login_close.click()

search = driver.find_element(By.NAME,value='q')
# print(search)

search.send_keys(search_name)

search.send_keys(Keys.ARROW_DOWN)

search.send_keys(Keys.ENTER)
time.sleep(10)
next_button= driver.find_element(By.XPATH,"//span[text()='Next']")

next_button.click()



# csv_heading = ['product_name','price']



# def grab_data():

#     current_url = driver.current_url
#     response = requests.get(current_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     headings = soup.find_all("div",{"class":"_4rR01T"})
#     prices = soup.find_all("div",{"class":"_30jeq3"})
#     data = []

#     for loop in range(len(headings)):
#         temp_dict = {}
#         temp_dict['product_name'] = headings[loop].string
#         price = prices[loop].string.replace('₹','')
#         price = price.replace(',','')
#         temp_dict['price'] = int(price)
#         data.append(temp_dict)

#     file_path = f'{search_name}.csv'
#     # i have written this code for checking the file is existing or not
#     # but when we are hitting the next button it's is also checking the all dom elements and grabing the duplicated values

#     if os.path.isfile(file_path):
#         with open(f'{search_name}.csv', 'a', encoding='UTF8', newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=csv_heading)
#             writer.writerows(data)
#     else:
#         with open(f'{search_name}.csv', 'w', encoding='UTF8', newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=csv_heading)
#             writer.writeheader()
#             writer.writerows(data)



# grab_data()
# # next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
# time.sleep(5)
# next_button= driver.find_element(By.XPATH,'//nav[@class="yFHi8N"]//a[@class="_1LKTO3"]')

# if next_button:
#     print(next_button,'inside function')
#     time.sleep(3)
#     next_button.click()
    
#     grab_data()
