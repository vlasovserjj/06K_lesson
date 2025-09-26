from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(45)
browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay = browser.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys(45)

button_7 = browser.find_element(By.XPATH, '//span[text()="7"]').click()
button_plus = browser.find_element(By.XPATH, '//span[text()="+"]').click()
button_8 = browser.find_element(By.XPATH, '//span[text()="8"]').click()
button_result = browser.find_element(By.XPATH, '//span[text()="="]').click()
waiter = WebDriverWait(browser, 51)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))

result = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
print(result)

assert result == '15'
browser.quit