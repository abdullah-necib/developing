import wx
import os
from threading import Thread


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, target):
        wx.FileDropTarget.__init__(self)
        self.target = target
        print(type(target))

    def OnDropFiles(self, x, y, filenames):
        self.target.Clear()
        self.contents =[]
        for fname in filenames:
            self.getAllDircContents(fname)

        for idx in self.contents:
            self.target.AppendText(idx +'\n')
        return True

    def getAllDircContents(self, mypath):
        isDirectory = os.path.isdir(mypath)
        self.contents.append(mypath)
        if isDirectory :
            for file in os.listdir(mypath):
                subDir = mypath +'/'+file.replace('\\','/')
                self.getAllDircContents(subDir)


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)

        self.text = wx.TextCtrl(self.panel, size=wx.Size(400,200),style=wx.TE_MULTILINE)
        self.text.AppendText('please drop files here\n')
        dropFiles = MyFileDropTarget(self.text)
        self.text.SetDropTarget(dropFiles)



if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None,title='text only')
    frm.Show()
    app.MainLoop()