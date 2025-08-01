from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage


class HistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.history_table_rows = (By.CSS_SELECTOR, ".table tr")

    def is_vehicle_in_history(self, plate):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.history_table_rows)
        )
        rows = self.driver.find_elements(*self.history_table_rows)
        for row in rows:
            if plate in row.text:
                return True
        return False