import wx

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, target):
        wx.FileDropTarget.__init__(self)
        self.target = target

    def OnDropFiles(self, x, y, filenames):
        for fname in filenames:
            self.target.AppendText(fname+'\n')

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        #sizer = wx.BoxSizer()
        #self.panel.SetSizer(sizer)
        self.text = wx.TextCtrl(self,style=wx.TE_MULTILINE,size=wx.Size(300,200))
        #self.text.SetSize()
        #sizer.Add(self.text)
        self.text.AppendText("Drag and Drop some FIles here..\n")
        dropTarget = MyFileDropTarget(self.text)
        self.text.SetDropTarget(dropTarget)



if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None,title ='copy past files')
    frm.Show()
    app.MainLoop()