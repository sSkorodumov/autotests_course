from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.CSS_SELECTOR, "#book").click()


    x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_value.text
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()