# 导入xlrd模块
import xlrd
from framework.logger import Logger

logger = Logger("logger=Util").getLog()

class Util(object):

    @classmethod
    def read_excel(self, excelPath, sheetName = "Sheet1"):
        """将Execl表格中的数据读取出来:
           思路：先读行，再读列，以列表字典方式进行数据存储
           如：[{'username':'test1','password':'123456'},{'username':'test2','password':'123456'}]
        """
        workbook = xlrd.open_workbook(excelPath)
        sheet = workbook.sheet_by_name(sheetName)
        # 获取第一行作为key值
        keys = sheet.row_values(0)
        # 获取总行数
        rowNum = sheet.nrows
        # 获取总列数
        cloNum = sheet.ncols


        if rowNum <=1:
            logger.error("excel表中数据总行数小于1")
        else:
            r = []
            j=1
            for i in range(1, rowNum):
                sheet_data = {}
                values = sheet.row_values(j)
                for j in range(cloNum):
                    sheet_data[keys[j]] = values[j]
                r.append(sheet_data)
                j+=1
        return r

if __name__ == "__main__":

    print(Util.read_excel("E:/UI_forum_test/data/data.xlsx", "Sheet1"))

