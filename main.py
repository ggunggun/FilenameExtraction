# __author__ = 'gengt'

from ExcelReader import ExcelReader
from ExcelWriter import ExcelWriter
from FileNameExtraction import FileNameExtraction
import MyGUI

def demo():
    f1 = 'sample/test.xlsx'
    f2 = 'sample/test1.xlsx'
    excelR = ExcelReader(f1)
    print excelR.asList()
    tables = excelR.asList()
    table = tables.values()[0]
    table.append([3, 'a', 'b', 'c'])
    excelW = ExcelWriter(f2)
    excelW.buildWorkBook(tables)
    excelW.save()
    excelR1 = ExcelReader(f2)
    print excelR1.asList()

def excelPrint(fileName):
    excel = ExcelReader(fileName)
    print excel.asList()

def  extract(dir, exl):
    fileNameExtraction = FileNameExtraction(dir)
    extractResult = fileNameExtraction.extract()
    excelW = ExcelWriter(exl)
    excelW.buildWorkBook({'sheet': extractResult.values()})
    excelW.save()
    #excelPrint(exl)

if __name__ == '__main__':
    #extract('sample/direction', 'sample/test2.xlsx')
    #MyGUI.foo()
    MyGUI.main(extract, None)
