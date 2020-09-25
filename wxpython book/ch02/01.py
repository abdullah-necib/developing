import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        button = wx.Button(self,wx.ID_OK)
        sizer.Add(button)
        button = wx.Button(self,label='Play')
        bitmapBit = wx.Bitmap('monkeyTime.png')
        button.SetBitmap(bitmapBit)
        sizer.Add(button)
        button = wx.Button(self,wx.ID_APPLY)
        button.SetAuthNeeded()
        sizer.Add(button)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON,self.OnButton)


    def OnButton(self, event):
        button = event.EventObject
        print('%s was pushed' % button.Label ,' button name is %s '% button.Name)
        if button.GetAuthNeeded():
            print('action require authorization to proceed')
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None,title='Start with Button')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()


