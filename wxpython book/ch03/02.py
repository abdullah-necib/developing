import wx


class RatingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._chLabel = wx.StaticText(self, label='Rating: ')
        choices = ['Excelent', 'Good', 'Average', 'Poor']
        self._choice = wx.Choice(self, choices=choices)
        self._cmtLabel = wx.StaticText(self, label='Comment: ')
        self._comment = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self._submit = wx.Button(self, label='Submit')
        self._doLayout()

    def _doLayout(self):
        main = wx.BoxSizer(wx.VERTICAL)

        topRow = wx.BoxSizer(wx.HORIZONTAL)

        topRow.Add(self._chLabel, 1, wx.EXPAND | wx.ALIGN_LEFT, 10)
        topRow.Add(self._choice, 3, wx.EXPAND, 20)  # | wx.ALIGN_CENTER_VERTICAL
        main.Add(topRow, 0, wx.EXPAND | wx.ALL, 5)

        commentRow = wx.BoxSizer(wx.HORIZONTAL)
        commentRow.Add(self._cmtLabel, flag=wx.RIGHT, border=30)
        commentRow.Add(self._comment, 1, wx.EXPAND)
        main.Add(commentRow, 1, wx.EXPAND | wx.ALL, 5)
        main.Add(self._submit, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        self.SetSizer(main)


if __name__ == '__main__':
    app = wx.App(False)
    frm = wx.Frame(None, title='test BoxSizer object')
    pnl = RatingPanel(frm)
    frm.Show()
    app.MainLoop()
