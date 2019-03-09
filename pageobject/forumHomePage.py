from pageobject.base import BasePage
import time
from selenium.webdriver.common.by import By
from framework.logger import Logger
import logging
logger=Logger(logger="ForumHomePage").getLog()
class ForumHomePage(BasePage):
    userName_input_loc=(By.NAME,"username")
    pwd_input_loc=(By.NAME,"password")
    login_btn_loc=(By.CSS_SELECTOR,'.fastlg_l em')
    #默认板块
    default_partbtn_loc=(By.CSS_SELECTOR,".bm_c h2 a")
    #发帖板块
    title_input_loc=(By.CSS_SELECTOR,".bm_c .px")
    content_input_loc=(By.CSS_SELECTOR,".tedt .pt")
    send_btn_loc=(By.CSS_SELECTOR,".bm_c button")

    #回复帖子板块
    replay_input_loc=(By.CSS_SELECTOR,".plc textarea")
    reply_btn_loc=(By.CSS_SELECTOR,".plc button")

    #退出功能
    logout_btn_loc=(By.PARTIAL_LINK_TEXT,"退出")

    #删除帖子
    forum_selected_loc=(By.XPATH,"//th/a[2]")
    delete_title_loc=(By.LINK_TEXT,"删除主题")
    sure_delete_loc=(By.XPATH,"//p/button/span")

    #模块管理
    manage_part_loc=(By.PARTIAL_LINK_TEXT,"管理中心")
    # admin_pwd_input_loc=(By.CSS_SELECTOR,".loginform input")
    admin_pwd_input_loc = (By.XPATH, "//p[@class ='loginform']/input[@name='admin_password']")
    admin_login_submit_btn_loc=(By.CSS_SELECTOR,".loginnofloat input")

    #进入论坛
    admin_forum_btn_loc=(By.XPATH,"//ul/li[7]/em/a")

    #创建板块
    add_new_partbtn_loc=(By.CSS_SELECTOR,".lastboard a")
    new_part_name_loc = (By.NAME, "newforum[39][]")
    # new_part_name_loc=(By.CSS_SELECTOR,".board input")
    add_submit_loc=(By.CSS_SELECTOR,".fixsel input")

    #用户在新模块下发帖
    new_part_user_send=(By.XPATH,"//tbody/tr[2]/td[2]/h2/a")

   #实战3
    search_post_loc=(By.CSS_SELECTOR,".scbar_txt_td input")
    search_btn_loc=(By.CSS_SELECTOR,".scbar_btn_td button")

    search_title_text_loc=(By.CSS_SELECTOR,".pbw h3 a")

    #实战4
    choose_sendforum_loc=(By.XPATH,"//a[@id='newspecial']/img")
    hold_vote_btn_loc=(By.PARTIAL_LINK_TEXT,"发起投票")

    vote_title_input_loc=(By.CSS_SELECTOR,".pbt .z span input")
    vote_title_input_loc1 = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")
    vote_title_input_loc2= (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    vote_title_input_loc3= (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")

    send_vote_btn_loc=(By.CSS_SELECTOR,".mtm button span")
    # back_firstPage_loc=(By.CSS_SELECTOR,".bm .nvhm")

    # 统计
    total_votes_name_loc = (By.XPATH, "//th[@class='common']/a[2]")
    # 进行投票
    vote_button_loc = (By.CSS_SELECTOR, ".pslt input")
    vote_submitbtn_loc = (By.CSS_SELECTOR, ".pn span")
    # 各个选项的名称及比例
    option_name_loc = (By.XPATH, "//div[@class='pcht']/table/tbody/tr/td/label")
    option_ratio_loc1= (By.XPATH,"//div[@class='pcht']/table/tbody/tr[2]/td[2]")
    option_ratio_loc2 = (By.XPATH, "//div[@class='pcht']/table/tbody/tr[4]/td[2]")
    option_ratio_loc3 = (By.XPATH, "//div[@class='pcht']/table/tbody/tr[6]/td[2]")
    # 主题的名称
    theme_name_loc = (By.CSS_SELECTOR, ".ts span")

    # alltheme_btn_loc=(By.XPATH,"//div[@class='tf']/a[1]")
    # choose_vote_loc=(By.XPATH,"//div[@id='filter_special_menu']/ul/li[2]/a")


    def login(self,user,pwd):
        self.open_url("http://127.0.0.1/forum.php?")
        self.sendkeys(user,*self.userName_input_loc)
        self.sendkeys(pwd,*self.pwd_input_loc)
        self.click(*self.login_btn_loc)
        time.sleep(5)

    def defalt(self):
        self.click(*self.default_partbtn_loc)
        time.sleep(5)

    def send_forum(self,title,content):
        try:
            if  len(title)+len(content)>=10:
                self.sendkeys(title,*self.title_input_loc)
                self.sendkeys(content,*self.content_input_loc)
                time.sleep(3)
                self.click(*self.send_btn_loc)
                logger.info("发表帖子成功")
                time.sleep(15)
            else:
                logger.error("发帖长度必须在4-1000字节之间，请重新输入！")
                time.sleep(15)
        finally:
            pass

    def reply_forum(self,reply_content):
        self.sendkeys(reply_content,*self.replay_input_loc)
        self.click(*self.reply_btn_loc)
        time.sleep(5)
        self.window_handle(0)

    def logout(self):
        self.click(*self.logout_btn_loc)
        time.sleep(15)


    def deleteForum(self):
        self.click(*self.forum_selected_loc)
        time.sleep(2)
        self.click(*self.delete_title_loc)
        time.sleep(3)
        self.click(*self.sure_delete_loc)
        time.sleep(4)


    def managePart(self,pwd):
        self.click(*self.manage_part_loc)
        time.sleep(3)
        self.window_handle(1)
        self.sendkeys(pwd,*self.admin_pwd_input_loc)
        time.sleep(4)
        self.click(*self.admin_login_submit_btn_loc)
        time.sleep(5)

    def addNewPart(self,content):
        self.click(*self.admin_forum_btn_loc)
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.click(*self.add_new_partbtn_loc)
        self.clear(*self.new_part_name_loc)
        time.sleep(3)
        self.sendkeys(content,*self.new_part_name_loc)
        self.click(*self.add_submit_loc)
        time.sleep(4)
        self.close()
        self.window_handle(0)
        self.refresh()
        time.sleep(15)

    def userNewSend(self):
        self.click(*self.new_part_user_send)
        time.sleep(2)


    def searchPost(self,content):
        self.sendkeys(content,*self.search_post_loc)
        self.click(*self.search_btn_loc)
        self.window_handle(1)
        # self.refresh()
        time.sleep(4)
        self.click(*self.search_title_text_loc)
        self.window_handle(2)
        self.refresh()

    def choose(self):
        self.click(*self.choose_sendforum_loc)
        time.sleep(4)
        self.click(*self.hold_vote_btn_loc)
        time.sleep(5)

    def voteContent(self,title,text1,text2,text3):
        self.sendkeys(title,*self.vote_title_input_loc)
        self.sendkeys(text1,*self.vote_title_input_loc1)
        self.sendkeys(text2, *self.vote_title_input_loc2)
        self.sendkeys(text3, *self.vote_title_input_loc3)
        time.sleep(5)
        # self.driver.switch_to.frame(0)
        print("发送成功")
        self.click(*self.send_vote_btn_loc)
        time.sleep(7)

    def totle(self):
        vote_name_list=[]
        self.click(*self.vote_button_loc)
        time.sleep(3)
        self.click(*self.vote_submitbtn_loc)
        time.sleep(3)

        options=self.find_elements(*self.option_name_loc)
        for option in options:
            name=self.text(option)
            vote_name_list.append(name)
            continue

        ratio1=self.getText(*self.option_ratio_loc1)
        print("第一个选项：",vote_name_list[0],"比例为：",ratio1)
        ratio2=self.getText(*self.option_ratio_loc2)
        print("第二个选项：", vote_name_list[1], "比例为：", ratio2)
        ratio3=self.getText(*self.option_ratio_loc3)
        print("第三个选项：", vote_name_list[2], "比例为：",ratio3)
        theme=self.getText(*self.theme_name_loc)
        print("投票主题是：",theme)
        self.getText(*self.theme_name_loc)
        time.sleep(5)
        self.window_handle(0)
        self.refresh()




























