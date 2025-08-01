from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from utils.logger_config import setup_logger

logger = setup_logger(__name__)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[contains(@type, 'submit')]")
        self.logout_button = (By.LINK_TEXT, "Logout")

    def login(self, username, password):
        logger.info(f"Attempting login with user: {username}")
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def verify_login_successful(self, timeout=10):
        logger.info("Verifying login success")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.logout_button)
            )

            assert "Parking" in self.driver.title, "Title does not contain 'parking'"

            return True
        except Exception as e:
            logger.error("Login failed")
            return False