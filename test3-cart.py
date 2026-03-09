from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Define the test function for cart with items
def test_cart_with_items(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Cart_Page.html")
    time.sleep(18)

    # Check that at least one item is present
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart-item")
    assert len(cart_items) > 0, "No items found in the cart."
    print(f"Found {len(cart_items)} item(s) in the cart.")

    # Verify each item has name, quantity, and price
    for index, item in enumerate(cart_items, start=1):
        name = item.find_element(By.CSS_SELECTOR, ".item-name").text
        quantity = item.find_element(By.CSS_SELECTOR, ".item-quantity").get_attribute("value")
        price = item.find_element(By.CSS_SELECTOR, ".item-price").text
        print(f"Item {index}: Name={name}, Quantity={quantity}, Price={price}")
        assert name != "", "Item name is missing."
        assert quantity != "", "Item quantity is missing."
        assert price != "", "Item price is missing."

    # Verify the totals
    total = driver.find_element(By.ID, "total").text
    vat = driver.find_element(By.ID, "vat").text
    final_total = driver.find_element(By.ID, "final-total").text
    print(f"Total: {total}, VAT: {vat}, Final Total: {final_total}")
    assert total != "", "Total amount is missing."
    assert vat != "", "VAT amount is missing."
    assert final_total != "", "Final total amount is missing."

    # Click Checkout
    checkout_button = driver.find_element(By.XPATH, "//a[text()='Check Out']")
    checkout_button.click()
    time.sleep(2)

    # Confirm checkout page opened (simple URL check)
    assert "checkout" in driver.current_url.lower(), "Checkout page did not open."
    print("Cart checkout test passed on", driver.name)


# Run the test
chrome_driver = webdriver.Chrome()
test_cart_with_items(chrome_driver)
chrome_driver.quit()