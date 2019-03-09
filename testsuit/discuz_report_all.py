import unittestimport sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("E:\\UI_forum_testt")
# sys.path.append("E:/UI_forum_test")
import os.path
import HTMLTestRunner




from testsuit.forum_serch_test import Forum_Search
from testsuit.forum_admin_test import ForumAdminTest
from testsuit.discuz_3_test import DiscuzSearch
from testsuit.discuz_4_test import DiscuzFourSearch

new_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(new_path,"report")
if not os.path.exists(report_path):
    os.makedirs(report_path)

suit=unittest.TestSuite()
suit.addTest(unittest.makeSuite(Forum_Search))
suit.addTest(unittest.makeSuite(ForumAdminTest))
suit.addTest(unittest.makeSuite(DiscuzSearch))
suit.addTest(unittest.makeSuite(DiscuzFourSearch))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="论坛测试情况描述")
    runner.run(suit)