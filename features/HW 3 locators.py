from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

driver.find_element(By.CSS_SELECTOR, '.a-link-nav-icon')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.ID, 'continue')
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")











