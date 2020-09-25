import wx
import wx.lib.mixins.listctrl as litmix
import wx.lib.sized_controls as sized
import wx.lib.agw.aui as aui

class AuiFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self._mgr = aui.AuiManager(self)
        self._phone = PhoneDialogPanel(self)
        self._contacts = ContactList(self)
        self._Calling = wx.ListBox(self)

        self.SetupMgr()
        self.SetInitialSize((750,350))

    def SetupMgr(self):
        info = aui.AuiPaneInfo().center().Name("Contact")
        lbl = 'Contact List'
        info = info.CloseButton(False).Caption(lbl)
        self._mgr.AddPane(self._contacts, info)

        self._phone.SetInitialSize()
        size = self._phone.BestSize
        info = aui.AuiPaneInfo().Right().Name("Phone")
        info = info.ButtomDockable(False).TopDockable(False)
        info = info.Layer(0).Caption('Phone')
        info = info.Fixed()
        self._mgr.AddPane(self._phone, info)

        info = aui.AuiPaneInfo().Right().Layer(0).Position(1)
        info = info.Name['Log'].Caption('Call Log')
        info = info.BestSize(size).MinSize(size)
        self._mgr.AddPane(self._Calling, info)

        self._mgr.Update()

if __name__ == '__main__':
    app = wx.App()
    frm = AuiFrame(None, title='test aui manager')
    frm.Show()
    app.MainLoop()