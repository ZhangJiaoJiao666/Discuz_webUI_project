import unittest
import time
from testsuit.basecase import BaseTestCase
from pageobject.forumHomePage import ForumHomePage

class ForumAdminTest(BaseTestCase):
    def test_forumAdmin(self):
        homePage=ForumHomePage(self.driver)
        homePage.login("admin","zjj")
        homePage.defalt()
        homePage.deleteForum()
        homePage.managePart("zjj")
        homePage.addNewPart("123")
        homePage.logout()
        time.sleep(6)
        homePage.login("rebecca","123456")
        homePage.userNewSend()
        homePage.send_forum("我是用户","我在新板块下发帖")
        homePage.reply_forum("我也是用户，我在新板块下回复")
        homePage.logout()



if __name__ == "__main__":
    unittest.main(verbosity=2)



