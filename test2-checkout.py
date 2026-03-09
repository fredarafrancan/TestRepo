from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Define the test function
def test_checkout_form(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/checkout.html")
    time.sleep(1)

    # Fill billing details
    driver.find_element(By.NAME, "firstname").send_keys("Fredara")
    driver.find_element(By.NAME, "email").send_keys("fredarasista@gmail.com")
    driver.find_element(By.NAME, "city").send_keys("Vienna")
    driver.find_element(By.NAME, "state").send_keys("Vienna")
    driver.find_element(By.NAME, "zip").send_keys("1210")

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    # Simple verification (depends on page behavior)
    assert "checkout" in driver.current_url.lower(), "Checkout did not proceed correctly."
    print("Checkout form test passed on", driver.name)


# Run the test
chrome_driver = webdriver.Chrome()
test_checkout_form(chrome_driver)
chrome_driver.quit()