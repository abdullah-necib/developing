import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.button1 = wx.Button(self,label = 'btn 1')
        sizer.Add(self.button1)
        self.button2 = wx.Button(self, label='btn 2')
        sizer.Add(self.button2)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        btn = event.EventObject
        wx.MessageBox('Button %s on Panel' % btn.Label,'FROM PANEL')
        if btn is self.button1: event.Skip()

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = MyPanel(self)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        btn = event.EventObject
        wx.MessageBox('Button %s on Frame' % btn.Label, 'FROM FRAME')
        event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        #wx.App.__init__(self)
        self.frame = MyFrame(None, title='test event Propagation')
        self.frame.Show()
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        return True

    def OnButton(self, event):
        btn = event.EventObject
        wx.MessageBox('Button %s on App' % btn.Label,'From APP')
        event.Skip()

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()