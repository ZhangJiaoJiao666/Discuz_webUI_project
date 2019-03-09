from pageobject.forumHomePage import ForumHomePage
from testsuit.basecase import BaseTestCase
from framework.logger import Logger
import unittest
import time
logger=Logger(logger="DiscuzSearch").getLog()
class DiscuzSearch(BaseTestCase):
    def test_ds(self):
        homePage=ForumHomePage(self.driver)
        homePage.login("rebecca","123456")
        homePage.searchPost("haotest")
        self.driver.refresh()

        time.sleep(5)
        try:
            assert "haotest" in self.driver.title
            print("所找到内容与期望值相等")
        except Exception as e:
            print("未成功，找到内容与期望标题并不符合",e)
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(4)
        homePage.logout()








if __name__=="__main__":
    unittest.main(verbosity=2)
