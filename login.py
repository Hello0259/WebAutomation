from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys("Oliver@yahoo.com")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys("12345")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()
time.sleep(2)
print("Login Successful")


