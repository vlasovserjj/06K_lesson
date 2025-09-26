from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
browser.get("https://www.saucedemo.com/")
user = browser.find_element(By.CSS_SELECTOR, "#user-name")
user.send_keys("standard_user")

password = browser.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")

login_but = browser.find_element(By.CSS_SELECTOR, "#login-button").click()

backpack = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

shirt = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

onesie = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

shopping = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

checkout = browser.find_element(By.CSS_SELECTOR, "#checkout").click()

first_name = browser.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Сергей")

last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Власов")

index = browser.find_element(By.CSS_SELECTOR, "#postal-code")
index.send_keys("410007")

contin = browser.find_element(By.CSS_SELECTOR, "#continue").click()

sum = browser.find_element(By.CLASS_NAME, "summary_total_label")
total_price = sum.text
assert total_price == "Total: $58.29"
browser.quit()

assert total_price == "Total: $58.29"
print(total_price)
