# __author__ = 'gengt'

from openpyxl.reader.excel import load_workbook


class ExcelReader(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.workBook = load_workbook(fileName)
        self.workSheets = {}
        #print self.workBook.get_named_ranges()
        #print self.workBook.get_sheet_names()
        for name in self.workBook.get_sheet_names():
            self.workSheets[name] = self.workBook.get_sheet_by_name(name)
        #print self.workSheets

    def printAll(self):
        for name, ws in self.workSheets.items():
            print name
            for row in ws.values:
                print row

    def asList(self):
        tables = {}
        for name, ws in self.workSheets.items():
            table = []
            for row in ws.values:
                table.append(list(row))
            tables[name] = table
        return tables

    def asWorkBook(self):
        return self.workBook
