#-*- coding:utf-8 -*-
#  __author__ = 'gengt'

import os


class FileNameExtraction(object):

    def __init__(self, folder):
        self.folder = folder

    def extract(self):
        return self.__extract(self.folder)

    def __extract(self, folder, resultDict={}):
        if os.path.exists(folder) and os.path.isdir(folder):
            #for dir, dirs, files in os.walk(folder):
            #    for file in files:
            #        print file.decode('gbk').encode('utf-8')
            files = os.listdir(folder)
            for file in files:
                #print file.decode('gb2312')
                #print unicode(file, 'gbk')
                if os.path.isdir(file):
                    self.__extract(file, resultDict)
                else:
                    #unicodeFile = unicode(file , "utf-8")
                    #unicodeFile = unicode(file, 'gbk')
                    if type(file) is unicode:
                        unicodeFile = file
                    else:
                        unicodeFile = unicode(file, 'gbk')
                    baseName = os.path.basename(unicodeFile)
                    name, ext = os.path.splitext(unicodeFile)
                    resultDict[baseName] = [baseName]
                    resultDict[baseName].extend(name.split(u'-'))
                    #print  resultDict[baseName]

        return resultDict
