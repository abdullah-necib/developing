import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        self.button = wx.Button(self, label='Push Me')

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None,title='this is test')
    frm.Show()
    app.MainLoop()