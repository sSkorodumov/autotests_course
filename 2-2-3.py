from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.refresh()
    num1_el = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_el = browser.find_element(By.CSS_SELECTOR, "#num2")

    ans = int(num1_el.text) + int(num2_el.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(ans))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()