import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
class PythonHelpApi():
    #定义读取XML数据方法
    def readXmlData(self,xmlFileName,firstTagName,SecondTagName):
        #导入minidom模块
        from xml.dom import minidom
        #通过绝对路径定位xml文件，文件名不能写死（因为一个xml文件对应一个用例模块，有多个xml），只能用变量传参
        xmlFilePath="/Users/yenuo/PycharmProjects/GoodShears/GoodShearsPoolData/"+xmlFileName+".xml"
        #使用minidom中parse函数打开xml文件
        xmlFile=minidom.parse(xmlFilePath)
        #基于打开的xml文件，通过标签名定位一级标签，标签名不能写死，通过变量传参后面下脚本不要忘记，xml中标签名最好不要相同，如果相同下角标也许变量化
        OneNode=xmlFile.getElementsByTagName(firstTagName)[0]
        #基于一级标签定位二级标签，方法同一级方式，标签名变量化
        TwoNode=OneNode.getElementsByTagName(SecondTagName)[0]
        #基于二级标签获取节点文本值，最后返回给调用的地方
        return TwoNode.childNodes[0].nodeValue
    #定义读取Excel数据方法

    def readExcelData(self,sheetName,x,y):
        #导入xlrd模块
        import xlrd
        # 找到对应的Excel(相对路径或绝对路径)
        ExcelPath="/Users/yenuo/PycharmProjects/GoodShears/GoodShearsPoolData/PageElement.xlsx"
        # 打开找到的Excel文件
        ExcelName=xlrd.open_workbook(ExcelPath)
        # 找到sheet页
        sheetPage=ExcelName.sheet_by_name(sheetName)
        # 定位单元格,取单元格中的值
        # sheetPage.cell(x.y).value
        return sheetPage.cell_value(x,y)
    def CreatHTMLReport(self,reportName,revTitle,reDes,revTest):
        #导入HTMLTestRunner模块，使用HTMLTestRunner生成HTML格式的测试报告
        import HTMLTestRunner
        #通过绝对路径定位报告存储位置
        reportPath="/Users/yenuo/PycharmProjects/GoodShears/Testresult/HTMLTestReport/"+reportName+".html"
        #使用with open打开报告模版，以二进制形式写入具体内容（w代表写入，b代表二进制【因为报告的内容有不同的数据类型】）as存储，htmlstarm内存空间
        with open(reportPath,'wb') as htmlstarm:
            #使用HTMLTestRunner方法生成具体内容
            HTMLTestRunner.HTMLTestRunner(
                #stream文本流，文本流向内存空间进行存储
                stream=htmlstarm,
                #报告级别，通常使用1或者2，但一般使用2
                verbosity=2,
                #报告标题
                title=revTitle,
                #报告的描述信息
                description=reDes
            ).run(revTest)#运行具体用例才能生成报告
