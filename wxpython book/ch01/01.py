import wx

class MyFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.SetIcon(wx.Icon('appIcon.png'))
        self.Panel = wx.Panel(self)
        
        
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None ,title='Main Frame from Abdullah')
        self.frame.Show()
        return True
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()