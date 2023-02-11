from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


# Create xPATH
#driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
#driver.find_element(By.ID, 'ap_email')
#driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
#driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#driver.find_element(By.XPATH, "//a[contains(@href, 'forgotpassword')]")
#driver.find_element(By.XPATH, "//a[contains(@href, 'customer/account-issues')]")
#driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
#driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")

#testcase SIGN IN
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//span[@class='nav-line-2' and text()= '& Orders']").click()

expected_result1 = 'Sign in'
actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Sign in')]").text
print('Sign in')

assert expected_result1 == actual_result1, f'Expected {expected_result1} but got actual {actual_result1}'
print('Test case passed')


#testcase EMAIL FIELD
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//span[@class='nav-line-2' and text()= '& Orders']").click()
print('Email')

expected_result2 = driver.find_element(By.ID, 'ap_email')
actual_result2 = driver.find_element(By.XPATH, "//input[@type='email']")


assert expected_result2 == actual_result2, f'Expected {expected_result2} but got actual {actual_result2}'
print('Test case passed')




























driver.quit()

















