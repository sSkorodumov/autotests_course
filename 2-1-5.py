from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute("valuex")
    x = float(x_value)
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()