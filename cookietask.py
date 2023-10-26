from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
username_input = driver.find_element(By.ID, "user-name").send_keys("standard_user")
password_input = driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
