import wx


class WrappingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # sbox = wx.StaticBox(self,label = 'static box label')
        sizer = wx.WrapSizer(wx.HORIZONTAL)

        for x in range(15):
            btn = wx.Button(self, label='Button "%d"' % x)
            sizer.Add(btn, 0, wx.ALL, 5)
        self.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App(False)
    frm = wx.Frame(None, title='test BoxSizer object')
    pnl = WrappingPanel(frm)
    frm.Show()
    app.MainLoop()
