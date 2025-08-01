import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage
from utils.logger_config import setup_logger

logger = setup_logger(__name__)

class ParkingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.car_plate_input = (By.ID, "car_plate")
        self.slot_input = (By.ID, "slot")
        self.start_button = (By.ID, "submit")
        self.row_xpath_template = "//tr[td[text()='{}']]"
        self.finish_button_xpath_template = "//tr[td[text()='{}']]//button[contains(@class, 'btn')]"
        self.logout_link = (By.LINK_TEXT, "Logout")
        self.history_button = (By.LINK_TEXT, "History")


    def park_vehicle(self, plate, slot):
        logger.info(f"Parking vehicle {plate} in slot {slot}")

        self.fill_input(self.car_plate_input, plate)
        self.fill_input(self.slot_input, slot)
        self.click(self.start_button)

        logger.info("Clicked 'Start Parking'")

    def enter_plate_num(self, plate):
        logger.info(f"Entering plate number {plate}")
        plate_input = self.driver.find_element(*self.car_plate_input)
        plate_input.clear()
        plate_input.send_keys(plate)

    def click_start_parking(self):
        logger.info("Click 'Start Parking'")
        self.click(self.start_button)


    def get_plate_field_value(self):
        logger.info(f"Getting plate field value")
        return self.driver.execute_script("return arguments[0].value;", self.driver.find_element(*self.car_plate_input))

    def verify_parking_started(self, plate):
        logger.info(f"Verifying parking started for {plate}")

        success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        assert plate in success_msg.text, f"Expected plate {plate} in success message, got: {success_msg.text}"

        logger.info("Success message verified.")
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2 and plate in cells[0].text:
                logger.info(f"Found plate {plate} in active parking table.")
                return True

        raise AssertionError(f"Plate {plate} not found in active parking table.")

    def get_parking_alert_text(self, timeout=10):
        logger.info("Get alert text")
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert"))
        )
        alert_text = self.driver.find_element(By.CLASS_NAME, "alert").text.strip()

        return alert_text


    def finish_parking(self, plate_number):
        logger.info(f"Attempting to finish parking for plate: {plate_number}")
        row_locator = (By.XPATH, self.row_xpath_template.format(plate_number))
        finish_button_locator = (By.XPATH, self.finish_button_xpath_template.format(plate_number))
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(row_locator)
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(finish_button_locator)
            ).click()
            logger.info(f"Successfully clicked 'Finish' for vehicle {plate_number}")
        except Exception as e:
            logger.error(f"Failed to finish parking for plate {plate_number}: {e}")
            raise

    def logout(self):
            logger.info("Logging out")
            self.driver.find_element(*self.logout_link).click()

    def generate_random_plate(self):
        logger.info("Generating random plate number")
        return ''.join([str(random.randint(0, 9)) for _ in range(8)])

    def go_to_history_page(self):
        logger.info("Go to history page")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.history_button)
        ).click()

    def get_validation_error_text(self):
        logger.info("Get validation error text")
        locator = (By.ID, "plate-error")
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).text.strip()

    def get_required_field_validation_message(self):
        logger.info("Checking HTML5 required field validation message")
        input_element = self.driver.find_element(*self.car_plate_input)
        is_valid = self.driver.execute_script("return arguments[0].checkValidity();", input_element)
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", input_element)
        logger.info(f"Validation result: {'Valid' if is_valid else 'Invalid'} - Message: '{validation_message}'")
        return not is_valid, validation_message

