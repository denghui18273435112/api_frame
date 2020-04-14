from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig

class Data:
    def __init__(self,testcase_file,sheet_name):
        """
        :param testcase_file:  表格名称
        :param sheet_name:   sheet名称
        :return: 使用excel工具类，获取结果list
        """
        self.reader = ExcelReader(testcase_file,sheet_name)

    def get_run_data(self):
        """
        #2、列是否运行内容，y
        根据是否运行列==y，获取执行测试用例
         #3、保存要执行结果，放到新的列表。
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                run_list.append(line)
        print("运行用例",run_list)
        return run_list

    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        # run_list=list()
        # for line in self.reader.data():
        # run_list.append(line)
        """
        run_list = [ line for line in self.reader.data()]
        return run_list

    def get_case_pre(self,pre):
        """
        #获取全部测试用例
        #list判断，执行，获取
        根据前置条件：从全部测试用例取到对应测试用例
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None