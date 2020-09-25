import wx
import wx.lib.sized_controls as sized


class ProxyConfigDlg(sized.SizedDialog):
    def __init__(self, parent, title):
        sized.SizedDialog.__init__(self, parent, title=title)
        pane = self.GetContentsPane()
        pane.SetSizerType("grid", {"rows": 3, "cols": 2})

        proxyLbl = wx.StaticText(pane, label="Proxy URL: ")
        url = wx.TextCtrl(pane)
        url.SetSizerProps(expand=True)

        nameLbl = wx.StaticText(pane, label='User Name: ')
        name = wx.TextCtrl(pane)
        name.SetSizerProps(expand=True)

        passLbl = wx.StaticText(pane, label="Password: ")
        name = wx.TextCtrl(pane)
        name.SetSizerProps(expand=True)

        bsz = self.CreateButtonSizer(wx.CANCEL | wx.OK)
        self.SetButtonSizer(bsz)
        self.SetInitialSize((300, 175))
        self.Fit()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        btn = wx.Button(self, label='Click Me')
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        dlg = ProxyConfigDlg(self, title='this is a new Dialog for Proxy')
        # print('we reach this')
        dlg.ShowModal()

        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='test Dialog')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()
