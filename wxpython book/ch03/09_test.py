import wx
import wx.lib.sized_controls as sized
import wx.xrc as xrc


class XrcTestApp(wx.App):
    def OnInit(self):
        frm = XrcTestFrame(None, title='Test Frame')
        frm.Show()
        return True


class XrcTestFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        pnl = XrcTestPanel(self)
        sizer = wx.BoxSizer()
        sizer.Add(pnl, 1, wx.EXPAND)
        self.SetSizer(sizer)


class XrcTestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.btn = wx.Button(self, label='Open Phone')
        self._doLayout()
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def _doLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.Add(self.btn)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnButton(self, event):
        PhoneDialog(self, "Phone Dialog").Show()


class PhoneDialog(wx.Dialog):
    def __init__(self, parent, title=''):
        wx.Dialog.__init__(self, parent, title=title)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # get resouuces
        resource = CustomXrcResource('xrchandler.xrc')
        panel = resource.LoadPanel(self, 'dialog_panel')
        self.display = panel.FindWindowByName('display')
        sizer.Add(panel, 1, wx.EXPAND)

        # additional buttons
        bsize = wx.BoxSizer(wx.HORIZONTAL)
        back = wx.Button(self, name='back')
        back.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK)
        bsize.Add(back, 1, wx.EXPAND)
        call = wx.Button(self, name='call')
        call.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD)

        bsize.Add(call, 1, wx.EXPAND)
        sizer.Add(bsize, 0, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):

        name = event.EventObject.Name

        if name.isdigit():
            print(name)
            self.display.AppendText(name)
        elif name == "back":
            txt = self.display.Value
            if len(txt):
                txt = txt[0:-1]
                self.display.Value = txt
        elif name == "call":
            print("Calling %s ..." % self.display.Value)


class CustomXrcResource(xrc.XmlResource):
    def __init__(self, filename):
        xrc.XmlResource.__init__(self, filename)
        self.InsertHandler(PhoneBtnPanelHandler())


class PhoneBtnPanelHandler(xrc.XmlResourceHandler):
    def CanHandle(self, dnode):
        return self.IsOfClass(node, "PhoneButtonPanel")

    def DoCreateResource(self):
        panel = PhoneButtonPanel(self.GetParentAsWindow())
        self.SetupWindow(panel)
        self.CreateChildren(panel)
        return panel


class PhoneButtonPanel(sized.SizedPanel):
    """Panel based widget to provide phone button input"""

    def __init__(self, parent):
        super(PhoneButtonPanel, self).__init__(parent)

        self.SetSizerType("grid", {"rows": 4, "cols": 3})
        lbls = ["1", "2", "3", "4", "5", "6",
                "7", "8", "9", "*", "0", "#"]
        for lbl in lbls:
            btn = wx.Button(self, label=lbl, name=lbl)


if __name__ == '__main__':
    app = XrcTestApp(False)
    app.MainLoop()
