from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_signup_popup(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Sign_Up_Page.html")

    wait = WebDriverWait(driver, 10)  # wait up to 10 seconds for elements

    try:
        # Wait for and fill in the Name field
        name_field = wait.until(EC.visibility_of_element_located((By.ID, "name")))
        name_field.send_keys("Fredara Francan")

        # Wait for and fill in the Email field
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_field.send_keys("fredarasista@gmail.com")

        # Wait for and fill in the Password field
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("Freda1996@")

        # Wait for and click the Sign Up button
        signup_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='signupForm']//button[text()='Sign Up']")))
        signup_button.click()

        # Wait for the popup to appear
        popup = wait.until(EC.visibility_of_element_located((By.ID, "promo-popup")))
        popup_message = wait.until(EC.visibility_of_element_located((By.ID, "promo-popup-message"))).text

        # Assertions
        assert popup.is_displayed(), "Sign-Up popup did not display."
        assert "success" in popup_message.lower(), f"Unexpected message: {popup_message}"

        print("Sign-Up popup test passed on", driver.name)

    except TimeoutException as e:
        print("Test failed due to timeout:", e)
        assert False, "Test failed due to timeout"

    except AssertionError as e:
        print("Assertion failed:", e)
        raise


# Run the test safely
chrome_driver = webdriver.Chrome()
try:
    test_signup_popup(chrome_driver)
finally:
    chrome_driver.quit()