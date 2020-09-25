"""this program is modified to 
apply context menu based on the 
type of what mouse is hover
@author: Abdullah NECIB
"""
import wx

ID_BLUE = wx.NewId()
ID_RED = wx.NewId()
ID_BTN = wx.NewId()
ID_NOTHING = wx.NewId()

class ContextMgr():
    def __init__(self, parent):
        assert isinstance(parent, wx.Window)
        assert hasattr(parent, 'GetPopupMenu')
        self.window = parent
        self.window.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

    def OnContextMenu(self, event):
        """here you can add menu based on the caller"""
	#modifications
        if event.Id == ID_BTN:
            menu = self.window.GetPopupMenuBTN()
        else:
            menu = self.window.GetPopupMenu()
        if menu:
            self.window.PopupMenu(menu)
            menu.Destroy()




class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        content = ContextMgr(self)

        self.btn = wx.Button(self,id=ID_BTN, label='try Hover over me')
        sizer = wx.BoxSizer()
        sizer.Add(self.btn)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_MENU, self.OnMenu)



    def GetPopupMenu(self):
        menu = wx.Menu()
        menu.Append(ID_BLUE, 'Blue')
        menu.Append(ID_RED, 'Red')
        return menu
	#modifications
    def GetPopupMenuBTN(self):
        menu = wx.Menu()
        menu.Append(ID_BTN, 'NOTHING')
        return menu
    def OnMenu(self, event):

        evtID = event.Id
        if evtID == ID_BLUE:
            self.BackgroundColour = 'Blue'
            self.Refresh()
        elif evtID == ID_RED:
            self.BackgroundColour = 'Red'
            self.Refresh()
        elif evtID == ID_BTN:
            print('calling based on Button it works')
        else:
            event.Skip()
if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()
