
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
driver.get('https://www.flipkart.com/')
search = driver.find_element(by=By.NAME, value="q")
search.send_keys("iphone",search.Ente)
search.send_keys(Keys.RETURN)
# driver.get("https://google.co.in/search?q=geeksforgeeks")
time.sleep(20)
driver.close()
