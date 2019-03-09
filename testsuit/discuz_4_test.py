from pageobject.forumHomePage import ForumHomePage
from testsuit.basecase import BaseTestCase
import unittest
class DiscuzFourSearch(BaseTestCase):
    def test_four(self):
        homePage=ForumHomePage(self.driver)
        homePage.login("rebecca","123456")
        homePage.defalt()
        homePage.choose()
        homePage.voteContent("第11投票哈哈哈","开心","伤心","还有")
        homePage.totle()
        homePage.refresh()
        homePage.logout()


if __name__=="__main__":
    unittest.main(verbosity=2)



