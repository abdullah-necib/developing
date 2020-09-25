import wx

class EasyMenu(wx.Menu):
    _map = {wx.ID_CUT: wx.ART_CUT,
            wx.ID_COPY: wx.ART_COPY,
            wx.ID_PASTE: wx.ART_PASTE,
            wx.ID_OPEN: wx.ART_FILE_OPEN,
            wx.ID_SAVE: wx.ART_FILE_SAVE,
            wx.ID_EXIT: wx.ART_QUIT
            }

    def AddEasyItem(self, id, label=''):
        item = wx.MenuItem(self, id, label)
        art = EasyMenu._map.get(id,None) # None is the value to be returned if key does not exist
        if art is not None:
            bmp = wx.ArtProvider.GetBitmap(art, wx.ART_MENU)
            if bmp.IsOk():
                item.SetBitmap(bmp)
            return self.AppendItem(item)

class Editor(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        menuBar = wx.MenuBar()
        self.DoSetupMenu(menuBar)
        self.SetMenuBar(menuBar)
        self.text =wx.TextCtrl(self, style=wx.TE_MULTILINE)

    def RegisterMenuAction(self, menu, id, handler, lablel=''):
        item = menu.AddEasyItem(id, lablel)
        self.Bind(wx.EVT_MENU,handler, item)
        
    def DoSetupMenu(self, menuBar):
        fileMenu = EasyMenu()
        self.RegisterMenuAction(fileMenu,wx.ID_OPEN, self.OnFile)
        self.RegisterMenuAction(fileMenu, wx.ID_SAVE, self.OnFile)
        self.RegisterMenuAction(fileMenu, wx.ID_EXIT, self.OnFile)
        menuBar.Append(fileMenu,'File')
        editMenu = EasyMenu()
        self.RegisterMenuAction(editMenu,wx.ID_CUT, self.OnEdit)
        self.RegisterMenuAction(editMenu, wx.ID_COPY, self.OnEdit)
        self.RegisterMenuAction(editMenu, wx.ID_CUT, self.OnEdit)
        menuBar.Append(editMenu, 'Edit')

    def OnFile(self, event):
        if event.Id== wx.ID_OPEN:
            print(event.EventObject)
            raise NotImplementedError("Open Not Implemented")
        elif event.Id== wx.ID_SAVE:
            raise NotImplementedError("Save Not Implemented")
        elif event.Id== wx.ID_EXIT:
            self.Close()
        else:
            event.Skip()
    def OnEdit(self, event):
        action = {wx.ID_CUT: self.txt.Cut,
                  wx.ID_COPY: self.txt.Copy,
                  wx.ID_PASTE: self.txt.Past}
        if action.has_key(event.id):
            action.get(event.id)()
        else: event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frm = Editor(None,title='this is a new frame')
    frm.Show()
    app.MainLoop()