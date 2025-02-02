
from selenium.webdriver.common.by import By
import time


class TableSearchPage:
    URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search']")
    TABLE_ROWS = (By.CSS_SELECTOR, "#example tbody tr")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, text):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(text)
        time.sleep(2)  # Wait for table to update

    def get_visible_rows_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len([row for row in rows if row.is_displayed()])









