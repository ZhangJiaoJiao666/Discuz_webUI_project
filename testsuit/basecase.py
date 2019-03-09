import unittest
from framework.browser_engine import BrowserEngine


class BaseTestCase(unittest.TestCase):
    browser = BrowserEngine()
    def setUp(self):
        self.driver=self.browser.open_browser()


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)

