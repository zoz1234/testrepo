from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TestClass:

    def setup_method(self):
        s = Service(executable_path=ChromeDriverManager().install())
        o = Options()
        o.add_experimental_option('detach', True)

        self.browser = webdriver.Chrome(service=s, options=o)

        self.browser.maximize_window()
        self.browser.get('URL')

    def teardown_method(self):
        self.browser.quit()

    # HELPER METHODS ---------------------------------------------------------------------------------------------------

    def get_element(self, locator: tuple, seconds=2) -> WebElement:
        """Call -> self.get_element((By.ID, 'elementID'), seconds=N)"""
        return WebDriverWait(self.browser, seconds).until(
            EC.presence_of_element_located(locator)
        )

    def get_elements(self, locator: tuple, seconds=2) -> list[WebElement]:
        """Call -> self.get_elements((By.TAG_NAME, 'input'), seconds=N)"""
        return WebDriverWait(self.browser, seconds).until(
            EC.presence_of_all_elements_located(locator)
        )

    # SHARED METHODS ---------------------------------------------------------------------------------------------------

    # TEST METHODS -----------------------------------------------------------------------------------------------------

    def test_function_name(self):
        pass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TestClass:

    def setup_method(self):
        s = Service(executable_path=ChromeDriverManager().install())
        o = Options()
        o.add_experimental_option('detach', True)

        self.browser = webdriver.Chrome(service=s, options=o)

        self.browser.maximize_window()
        self.browser.get('URL')

    def teardown_method(self):
        self.browser.quit()

    # HELPER METHODS ---------------------------------------------------------------------------------------------------

    def get_element(self, locator: tuple, seconds=2) -> WebElement:
        """Call -> self.get_element((By.ID, 'elementID'), seconds=N)"""
        return WebDriverWait(self.browser, seconds).until(
            EC.presence_of_element_located(locator)
        )

    def get_elements(self, locator: tuple, seconds=2) -> list[WebElement]:
        """Call -> self.get_elements((By.TAG_NAME, 'input'), seconds=N)"""
        return WebDriverWait(self.browser, seconds).until(
            EC.presence_of_all_elements_located(locator)
        )

    # SHARED METHODS ---------------------------------------------------------------------------------------------------

    # TEST METHODS -----------------------------------------------------------------------------------------------------

    def test_function_name(self):
        pass
