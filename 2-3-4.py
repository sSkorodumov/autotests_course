from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_value.text
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()