import wx

class ImagePaenl(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        theBitmap = wx.Bitmap("usingBitmaps.png")
        self.bitmap = wx.StaticBitmap(self, bitmap=theBitmap)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.SetIcon(wx.Icon('appIcon.png'))
        self.Panel =ImagePaenl(self)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='Main Frame from Abdullah')
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()