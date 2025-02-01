import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

BASE_URL = "http://127.0.0.1:5502/Code/Frontend"

@pytest.fixture
def driver():
    # Setup Selenium WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sign_in_and_sell_product(driver):
    print("Test for sign-in and sell product started")

    # Define WebDriverWait with a 10-second timeout
    wait = WebDriverWait(driver, 10)

    # Step 1: Sign In
    print("Starting sign-in process")
    driver.get(f"{BASE_URL}/SignIn.html")

    # Find and fill out the email field
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("user2@iitdh.ac.in")

    # Find and fill out the password field
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("user2")  # Use a test password

    # Submit the form by clicking the Sign in button
    driver.find_element(By.CLASS_NAME, "signin-btn").click()

    # Wait for alert and verify message for successful login
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print("Alert message received:", alert_text)
        assert "Login successful" in alert_text
        alert.accept()
    except Exception as e:
        print("Error during login:", e)
        assert False, "Login alert not found or unexpected alert message."

    # Check for redirection to index page after login
    wait.until(EC.url_to_be(f"{BASE_URL}/index.html"))
    assert driver.current_url == f"{BASE_URL}/index.html"
    print("Sign-in process completed successfully")

    # Step 2: Navigate to Sell Page
    print("Navigating to the Sell page")
    driver.get(f"{BASE_URL}/Sell.html")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))

    # Step 3: Fill and Submit the Sell Form
    print("Filling out the sell product form")

    driver.find_element(By.ID, "title").send_keys("Test23 Product")
    driver.find_element(By.ID, "selling_price").send_keys("150")
    driver.find_element(By.ID, "new_item_price").send_keys("200")
    driver.find_element(By.ID, "description").send_keys("This is a test description.")
    driver.find_element(By.ID, "grade").send_keys("4")

    # Select a category
    category_dropdown = driver.find_element(By.ID, "categoryID")
    category_dropdown.click()
    driver.find_element(By.XPATH, "//select[@id='categoryID']/option[@value='1']").click()

    # Fill in image links
    driver.find_element(By.ID, "imageLinks").send_keys("https://example.com/image1.jpg\nhttps://example.com/image2.jpg")

    # Submit the form
    driver.find_element(By.CLASS_NAME, "sell-btn").click()

    # Wait for alert and verify message for successful listing
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print("Alert message received:", alert_text)
        assert "Product listed successfully" in alert_text
        alert.accept()

    except Exception as e:
        print("Error during product listing:", e)
        assert False, "Sell alert not found or unexpected alert message."

    print("Test for sign-in and sell product completed successfully")
