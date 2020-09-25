import wx
import wx.lib
from wx.lib.sized_controls import SizedScrolledPanel


class MyPanel(SizedScrolledPanel):
    def __init__(self, parent):
        SizedScrolledPanel.__init__(self, parent)
        self.SetSizerType("form")
        label = wx.StaticText(self, label='field 1')
        text = wx.TextCtrl(self)
        text.SetSizerProp('expand', True)
        label2 = wx.StaticText(self, label='field 2')
        # label2.SetSizerProp('expand', True)
        choice = wx.Choice(self, choices=['1', '2', '3'])
        choice.SetSizerProp('expand', True)


if __name__ == '__main__':
    app = wx.App(False)
    frm = wx.Frame(None, title='test BoxSizer object')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()
