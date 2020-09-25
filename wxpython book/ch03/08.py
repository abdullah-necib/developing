import wx
import wx.xrc as xrc


class ResourceDialog(object):
    def __init__(self, parent):
        object.__init__(self)
        resouce = xrc.XmlResource("xrcdlg.xrc")
        self.dlg = resouce.LoadDialog(parent, "xrctestdlg")
        checkId = resouce.GetXRCID("check_box")
        self.dlg.Bind(wx.EVT_CHECKBOX, self.OnCheck, id=checkId)

    def OnCheck(self, event):
        print("Checked %s " % event.IsChecked())

    def ShowModal(self):
        result = self.dlg.ShowModal()
        if result == wx.ID_OK:
            print("Ok Clicked")
        else:
            print("Cancel Clicked")


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        pnl = wx.Panel(self)
        btn = wx.Button(pnl, label="Click here")
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Show()

    def OnButton(self, event):
        test = ResourceDialog(self)
        test.ShowModal()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title='this is test only')
    app.MainLoop()
