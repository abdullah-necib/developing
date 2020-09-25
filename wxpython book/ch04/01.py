import wx

class MyNoteBook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        self.il = wx.ImageList(16,16)
        print(self.il.Add(wx.Bitmap('smile.png')))
        self.AssignImageList(self.il)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnChanging)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnChanged)

    def OnChanging(self, event):
        #print(event)
        result = wx.MessageBox('Allow Page Changes ?', 'Allow ?',wx.YES_NO)
        if result == wx.NO:
            event.Veto()

    def OnChanged(self, event):
        print('Page Chnaged ', event.Selection)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        sizer = wx.BoxSizer()
        self.nb = MyNoteBook(self)
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)
        page1 = wx.TextCtrl(self.nb, style=wx.TE_MULTILINE)
        self.nb.AddPage(page1,'Page 1')
        page2 = wx.TextCtrl(self.nb, style= wx.TE_MULTILINE)
        self.nb.AddPage(page2, 'Page 2', imageId=0)
        self.SetInitialSize((400,250))
        

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title ='NoteBook Test')
    frm.Show()
    app.MainLoop()
