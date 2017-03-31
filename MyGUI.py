#-*- coding:utf-8 -*-
#  __author__ = 'gengt'
#import os
import wx

def foo():
    print wx.version()

def main(extractMethod, log):
    #app = MyApp(extractMethod, log)
    #app.MainLoop()
    app = wx.App(True, 'error.log')
    #app.RedirectStdio('error.log')
    frame = wx.Frame(parent=None, title='Filename Extraction')
    mpnl = MainPanel(frame, extractMethod, log)
    frame.Show()
    app.MainLoop()


#class MyFrame(wx.Frame):
#    def __init__(self, parent, title, extractMethod, log):
#        wx.MyFrame.__init__(self, parent=parent, title=title)
#        self.extractMethod = extractMethod
#        self.log = log
#
#
#class MyApp(wx.App):
#    def __init__(self, extractMethod, log):
#        wx.App.__init__(self)
#        self.extractMethod = extractMethod
#        self.log = log
#
#    def OnInit(self):
#        frame = wx.Frame(parent = None, title = 'Filename Extraction')
#        mpnl = MainPanel(frame, self.extractMethod, self.log)
#        frame.Show()
#        return True



class MainPanel(wx.Panel):
    def __init__(self, parent, extractMethod, log):
        wx.Panel.__init__(self, parent, -1)
        self.extractMethod = extractMethod
        self.log = log

        folderLabel = wx.StaticText(self, -1, "Scan Folder: ")
        folderInput = wx.TextCtrl(self, -1, "", size=(220, -1))
        self.folderInput = folderInput
        #self.Bind(wx.EVT_TEXT, self.EvtText, t1)
        folderButton = wx.Button(self, -1, "...", size=(30, -1))
        self.Bind(wx.EVT_BUTTON, self.exploreFolder, folderButton)

        excelLabel = wx.StaticText(self, -1, "Output File: ")
        excelInput = wx.TextCtrl(self, -1, "", size=(220, -1))
        self.excelInput = excelInput
        excelButton = wx.Button(self, -1, "...", size=(30, -1))
        self.Bind(wx.EVT_BUTTON, self.exploreFile, excelButton)

        extractButton = wx.Button(self, -1, "Extract")
        self.Bind(wx.EVT_BUTTON, self.extract, extractButton)

        space = 6
        #bsizer = wx.BoxSizer(wx.VERTICAL)
        #bsizer.Add(b1, 0, wx.GROW | wx.ALL, space)

        sizer = wx.FlexGridSizer(cols=3, hgap=space, vgap=space)
        sizer.AddMany([folderLabel, folderInput, folderButton,
                       excelLabel, excelInput, excelButton,
                       (0,0), extractButton, (0, 0)])
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(sizer, 0, wx.ALL, 25)
        self.SetSizer(border)
        self.SetAutoLayout(True)

    def exploreFolder(self, evt):
        # In this case we include a "New directory" button.
        dlg = wx.DirDialog(self, "Choose a directory ...",
                           style=wx.DD_DEFAULT_STYLE
                           # | wx.DD_DIR_MUST_EXIST
                           # | wx.DD_CHANGE_DIR
                           )

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it.
        if dlg.ShowModal() == wx.ID_OK:
            ##self.log.WriteText('You selected: %s\n' % dlg.GetPath())
            path = dlg.GetPath()
            print "set explore folder:", path
            self.folderInput.WriteText(path)

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()

    def exploreFile(self, evt):
        wildcard = "Excel Workbook (*.xlsx)|*.xlsx|" \
                   "Excel 97-2003 Workbook (*.xls)|*.xls|" \
                   "All files (*.*)|*.*"
        ##self.log.WriteText("CWD: %s\n" % os.getcwd())

        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'save' dialog.
        #
        # Unlike the 'open dialog' example found elsewhere, this example does NOT
        # force the current working directory to change if the user chooses a different
        # directory than the one initially set.
        dlg = wx.FileDialog(self, message="Save file as ...", defaultFile="", wildcard=wildcard, style=wx.SAVE)

        # This sets the default filter that the user will initially see. Otherwise,
        # the first filter in the list will be used by default.
        #dlg.SetFilterIndex(2)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print "set xsl file", path
            self.excelInput.WriteText(path)
            ##self.log.WriteText('You selected "%s"' % path)

            # Normally, at this point you would save your data using the file and path
            # data that the user provided to you, but since we didn't actually start
            # with any data to work with, that would be difficult.
            #
            # The code to do so would be similar to this, assuming 'data' contains
            # the data you want to save:
            #
            # fp = file(path, 'w') # Create file anew
            # fp.write(data)
            # fp.close()
            #
            # You might want to add some error checking :-)
            #

        # Note that the current working dir didn't change. This is good since
        # that's the way we set it up.
        ##self.log.WriteText("CWD: %s\n" % os.getcwd())

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def extract(self, evt):
        print "extract: folder: %s; xsl: %s" % (self.folderInput.GetValue(), self.excelInput.GetValue())
        #wx.Log.LogTextAtLevel(wx.LOG_Error, "bala")
        #wx.Log.LogText("balabala")
        #wx.LOG_Debug("balabalabala")
        if self.folderInput.GetValue() and self.excelInput.GetValue():
            try:
                self.extractMethod(self.folderInput.GetValue(), self.excelInput.GetValue())
            except Exception, e:
                print e
                dlg = wx.MessageDialog(self,
                                       'Sad. Some error happens. Please refer to error.log',
                                       'Result',
                                       wx.OK | wx.ICON_ERROR
                                       # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                       )
                dlg.ShowModal()
                dlg.Destroy()
            dlg = wx.MessageDialog(self, 'Congratulations. The filenames have been extracted to %s' % self.excelInput.GetValue(),
                                   'Result',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self,
                                   'You must specify the extract folder and the export file.',
                                   'Result',
                                   wx.OK | wx.ICON_WARNING
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()

