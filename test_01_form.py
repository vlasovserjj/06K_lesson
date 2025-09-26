from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pytest
edge_driver_path = r"C:\Program Files\EdgeNew\msedgedriver.exe"

driver = webdriver.Edge(service=EdgeService(edge_driver_path))
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


fn = '[name="first-name"]'
ln = '[name="last-name"]'
em = '[name="e-mail"]'
ad = '[name="address"]'
ph = '[name="phone"]'
st = '[name="city"]'
cn = '[name="country"]'
jp = '[name="job-position"]'
cm = '[name="company"]'
search = driver.find_element

first_name = search(By.CSS_SELECTOR, fn)
first_name.send_keys("Иван")

last_name = search(By.CSS_SELECTOR, ln)
last_name.send_keys("Петров")

adress = search(By.CSS_SELECTOR, ad)
adress.send_keys("Ленина, 55-3")

email = search(By.CSS_SELECTOR, em)
email.send_keys("test@skypro.com")

phone_number = search(By.CSS_SELECTOR, ph)
phone_number.send_keys("+7985899998787")

sity = search(By.CSS_SELECTOR, st)
sity.send_keys("Москва")

country = search(By.CSS_SELECTOR, cn)
country.send_keys("Россия")

job_position = search(By.CSS_SELECTOR, jp)
job_position.send_keys("QA")

company = search(By.CSS_SELECTOR, cm)
company.send_keys("SkyPro")

company = search(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

zip_code = search(By.CSS_SELECTOR, '#zip-code')
color_red = zip_code.value_of_css_property('background-color')
red_exp_color = 'rgba(248, 215, 218, 1)'
assert color_red == red_exp_color

green_exp_color = 'rgba(209, 231, 221, 1)'

fnn = "#first-name"
lnn = "#last-name"
emn = "#e-mail"
adn = "#address"
phn = "#phone"
stn = "#city"
cnn = "#country"
jpn = "#job-position"
cmn = "#company"



fields = [fnn, lnn, adn, emn, phn, stn, cnn, jpn, cmn] 
for field in fields:
    element = driver.find_element(By.CSS_SELECTOR, field)
    green = element.value_of_css_property('background-color')
    green_exp_color = 'rgba(209, 231, 221, 1)'
    assert green == 'rgba(209, 231, 221, 1)'

driver.quit()