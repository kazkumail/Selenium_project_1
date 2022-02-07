from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("/Users/kumail/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

input_first_name = driver.find_element(By.NAME, 'fName')
input_first_name.send_keys("FIRST NAME")

input_last_name = driver.find_element(By.NAME, 'lName')
input_last_name.send_keys("LAST NAME")

email_address = driver.find_element(By.NAME, 'email')
email_address.send_keys("FIRSTNAMELASTNAME@gmail.com")

sign_up_button = driver.find_element(By.TAG_NAME, 'button')
sign_up_button.click()