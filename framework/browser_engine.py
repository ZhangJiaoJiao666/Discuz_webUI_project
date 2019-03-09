import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BroserEngine").getLog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_driver_path = dir + "/tools/chromedriver.exe"
    IE_driver_path = dir + "/tools/IEDriverServer.exe"
    fireFoxdriver_path = dir + "/tools/geckodriver.exe"


    def open_browser(self):
        config=ConfigParser() #用来进行ini文件的读取
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini" #文件路径准确率高
        # config.read(file_path) #读取文件的路径
        config.read(file_path,encoding="utf-8")

        browser=config.get("browserType","browserName")  #ini文件中的
        logger.info("You had select %s browser" % browser)

        url=config.get("testServer",'URL')
        logger.info("the test server url is :%s" % url)


        if browser=="Firefox":
            driver = webdriver.Firefox(self.fireFoxdriver_path)
            logger.info("Starting firefox browser")
        elif browser=="Chrome":
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser")
        elif browser == "IE":
            driver = webdriver.Ie(self.IE_driver_path)
            logger.info("Starting IE browser")

        driver.get(url)
        logger.info("Open url:%s"%url)
        driver.maximize_window()
        logger.info("Maximize the current window. ")
        driver.implicitly_wait(10)
        logger.info("Wait for 10s to open .")
        return driver

    def quitBrowser(self):
        logger.info("Now,Close and quit the broswer.")
        self.driver.quit()


