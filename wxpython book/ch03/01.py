import wx


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.label = wx.StaticText(self, label='Label:')
        choices = ['a', 'b', 'c']
        self.choice = wx.Choice(self, choices=choices)
        self.info = wx.StaticText(self)
        self._doLayout()
        self.Bind(wx.EVT_CHOICE, self.OnChoice, self.choice)

    def _doLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        row = wx.BoxSizer(wx.HORIZONTAL)
        row.Add(self.label)
        row.AddSpacer(10)
        row.Add(self.choice)
        sizer.Add(row, flag=wx.CENTER)
        sizer.AddSpacer(20)
        sizer.Add(self.info, flag=wx.CENTER)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)

    def OnChoice(self, event):
        lbl = "'%s' was selected" % event.String
        self.info.Label = lbl
        self.Layout()


if __name__ == '__main__':
    app = wx.App(False)
    frm = wx.Frame(None, title='test BoxSizer object')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()
