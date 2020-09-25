import wx


class GroupBox(wx.StaticBox):
    def __init__(self, parent, orient, label=''):
        wx.StaticBox.__init__(self, parent, label=label)
        self._sizer = wx.StaticBoxSizer(self, orient)

    def AddItem(self, item, proportion=0, flag=wx.ALL, border=5):
        self._sizer.Add(item, proportion, flag, border)

    @property
    def Sizer(self):
        return self._sizer


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sbox = GroupBox(self, wx.HORIZONTAL, label='Group of Buttons')
        for x in range(1, 4):
            btn = wx.Button(self, label="Button '%d'" % x)
            sbox.AddItem(btn)
        sizer.Add(sbox.Sizer, 0, wx.ALL, 20)

        groupBox = wx.StaticBox(self, label='Group Of Labels')
        staticBoxSizer = wx.StaticBoxSizer(groupBox, wx.HORIZONTAL)
        for x in range(1, 4):
            lbl = wx.StaticText(self, label="Label '%d'" % x)
            staticBoxSizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(staticBoxSizer, 0, wx.ALL, 20)
        self.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App(False)
    frm = wx.Frame(None, title='test BoxSizer object')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()
