import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_novelship_factorial(fresh_browser: webdriver.Remote):
    fresh_browser.get("http://qainterview.pythonanywhere.com/")
    # assert fresh_browser.title == "Factorial"  # Comment this as it will fail the test
    header_title: WebElement = fresh_browser.find_element(By.CSS_SELECTOR,
                                                          "body > div.container.toppy > div:nth-child(1) > div > h1")
    header_title = header_title.get_attribute("textContent")
    assert header_title == "The greatest factorial calculator!"
    # logging.info(f"header_title::::: {header_title}")
    text_box: WebElement = fresh_browser.find_element(By.ID, "number")
    text_box.is_enabled()
    assert text_box.get_attribute("placeholder") == "Enter an integer"
    # Insert value into text box
    text_box.clear()
    text_box.send_keys(5)
    # Click the Button
    calc_btn: WebElement = fresh_browser.find_element(By.ID, "getFactorial")
    calc_btn.click()
    # locator is used to identify the element, and wait until it is present
    locator = (By.ID, "resultDiv")
    wait = WebDriverWait(fresh_browser, 3)
    wait.until(ec.text_to_be_present_in_element(locator, "The factorial of 5 is: 120"))
    # result of the text presented
    result: WebElement = fresh_browser.find_element(By.ID, "resultDiv")
    result = result.get_attribute("textContent")
    # Assertion of the result
    assert result == "The factorial of 5 is: 120"
