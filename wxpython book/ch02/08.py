import wx

ID_BLUE = wx.NewId()
ID_RED = wx.NewId()


class ContextMenuMgr(object):
    def __init__(self, parent):
        assert isinstance(parent, wx.Window)
        assert hasattr(parent, 'GetPopupMenu') #parent must implement PopUp
        self.window = parent
        self.window.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

    def OnContextMenu(self, event):
        menu = self.window.GetPopupMenu()
        if menu:
            self.window.PopupMenu(menu)
            menu.Destroy()
            #print(menu)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._menuMgr =ContextMenuMgr(self)
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def GetPopupMenu(self):
        menu= wx.Menu()
        menu.Append(ID_BLUE,"BLUE")
        menu.Append(ID_RED, "RED")
        return menu

    def OnMenu(self, event):
        evtID = event.Id
        if evtID == ID_BLUE:
            self.BackgroundColour = wx.BLUE
            self.Refresh()
        elif evtID == ID_RED:
            self.BackgroundColour = wx.RED
            self.Refresh()
        else: event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()