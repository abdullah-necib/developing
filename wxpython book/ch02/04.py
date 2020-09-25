import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.text = MemoryTextCtrl(self)
        #self.text2 = MemoryTextCtrl(self, style=wx.TE_MULTILINE, size=wx.Size(200, 200))
        self.btn = wx.Button(self,label='test')
        vsizer.Add(self.text)
        vsizer.Add(self.btn)
        #vsizer.Add(self.text2)
        self.SetSizer(vsizer)

class MemoryTextCtrl(wx.TextCtrl):
    def __init__(self, parent,*args,**kwargs):
        wx.TextCtrl.__init__(self, parent,*args,**kwargs)
        self._memories = set()
        self.Bind(wx.EVT_KILL_FOCUS, lambda event: self.Memorize())
        self.Bind(wx.EVT_SET_FOCUS, self.OnUpdateComplete)

    def OnUpdateComplete(self, event):
        print(self._memories)
        check = self.AutoComplete(list(self._memories))
        print(check)

        event.Skip()

    def Memorize(self):
        if self.Value:
            self._memories.add(self.Value)

    #def Forget(self):
     #   self._memories.clear()


if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()