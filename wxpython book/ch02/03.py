import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.allCB = wx.CheckBox(self, label='All Selected',style=wx.CHK_3STATE)
        vsizer.Add(self.allCB)
        self.option1 = wx.CheckBox(self, label='Option 1')
        vsizer.Add(self.option1, flag=wx.LEFT, border=10)
        self.option2 = wx.CheckBox(self, label='Option 2')
        vsizer.Add(self.option2, flag=wx.LEFT, border = 10)
        self.SetSizer(vsizer)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)

    def OnCheckBox(self, event):
        check = event.EventObject
        if check is self.allCB:
            self.option1.Value = check.Value
            self.option2.Value = check.Value
        else:
            values = [self.option1.Value, self.option2.Value]
            if all(values):
                self.allCB.Set3StateValue(wx.CHK_CHECKED)
            elif any(values):
                self.allCB.Set3StateValue(wx.CHK_UNDETERMINED)
            else:
                self.allCB.Set3StateValue(wx.CHK_UNCHECKED)


if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()