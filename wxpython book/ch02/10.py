import wx

ArtMap = {wx.ID_CUT: wx.ART_CUT,
          wx.ID_COPY: wx.ART_COPY,
          wx.ID_PASTE: wx.ART_PASTE,
          wx.ID_OPEN: wx.ART_FILE_OPEN,
          wx.ID_SAVE: wx.ART_FILE_SAVE,
          wx.ID_EXIT: wx.ART_QUIT,
          }


class EasyMenuItem(wx.Menu):
    def AddItem(self, id, label=''):
        """this function is used only for adding ART bmp"""
        item = wx.MenuItem(self, id, label)
        art = ArtMap.get(id, None)
        if art is not None:
            bmp = wx.ArtProvider.GetBitmap(art,wx.ART_MENU)
            if bmp.IsOk():
                item.SetBitmap(bmp)
        return self.Append(item)

class EasyToolBar(wx.ToolBar):
    def AddItem(self, id):
        art = ArtMap.get(id, None)
        if art is not None:
            bmp = wx.ArtProvider.GetBitmap(art,wx.ART_TOOLBAR)
            if bmp.IsOk():
                self.AddSimpleTool(id, bmp)

class Editor(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.AddMenu()
        self.AddToolBar()

        self.txt = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_RICH2)


    def AddMenu(self):
        mainMenu = wx.MenuBar()
        fileMenu = EasyMenuItem()
        self.RegisterMenuItem(fileMenu, wx.ID_OPEN)
        self.RegisterMenuItem(fileMenu, wx.ID_SAVE)
        self.RegisterMenuItem(fileMenu, wx.ID_EXIT)
        editMenu = EasyMenuItem()
        self.RegisterMenuItem(editMenu, wx.ID_CUT)
        self.RegisterMenuItem(editMenu, wx.ID_COPY)
        self.RegisterMenuItem(editMenu, wx.ID_PASTE)
        mainMenu.Append(fileMenu, 'File')
        mainMenu.Append(editMenu, 'Edit')
        self.SetMenuBar(mainMenu)

    def RegisterMenuItem(self, menu, id):
        item = menu.AddItem(id)
        self.Bind(wx.EVT_MENU, self.OnMenu, item)

    def OnMenu(self, event):
        evtID = event.Id
        if evtID == wx.ID_OPEN:
            raise NotImplemented('Open is Not Ready')
        elif evtID == wx.ID_SAVE:
            raise NotImplemented('Save is Not Ready')
        elif evtID == wx.ID_EXIT:
            self.Close()
        elif evtID == wx.ID_CUT:
            raise NotImplemented('Cut is Not Ready')
        elif evtID == wx.ID_COPY:
            raise NotImplemented('Copy is Not Ready')
        elif evtID == wx.ID_PASTE:
            raise NotImplemented('Paste is Not Ready')
        else:
            event.Skip()

    def AddToolBar(self):
        mainToolBar = EasyToolBar(self)
        for key in ArtMap.keys():
            mainToolBar.AddItem(key)
        mainToolBar.Realize()
        self.SetToolBar(mainToolBar)

class EditorUpdateWithUI(Editor):
    def __init__(self, *args, **kwargs):
        Editor.__init__(self, *args, **kwargs)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI)

    def OnUpdateUI(self, event):
        evtID = event.Id
        if evtID in (wx.ID_COPY,wx.ID_CUT):
            event.Enable(self.txt.CanCopy())
        elif evtID == wx.ID_PASTE:
            event.Enable(self.txt.CanPaste())
        else:
            event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        frm = EditorUpdateWithUI(None, title='Test Menu and ToolBar')
        frm.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
