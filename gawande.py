from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
link = 'https://jobs.rockwellautomation.com/'

driver.get(link)

time.sleep(4)
driver.maximize_window()
driver.find_element(
    By.XPATH, '//*[@id="cws_jobsearch_keywords"]').send_keys('temporary_data')

driver.find_element(
    By.XPATH, '//*[@id="select2-cws_jobsearch_primary_category-container"]').click()

driver.find_element(
    By.XPATH, '/html/body/span/span/span[1]/input').send_keys('information', Keys.ENTER)


