import wx
import wx.lib.platebtn as platbtn
import wx.adv

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.Add(sizer)

        #add toggle Button
        toggle = wx.ToggleButton(self, label='Toggle Me')
        toggle.SetValue(True)
        sizer.Add(toggle)
        toggle = wx.ToggleButton(self,label='Me too')
        sizer.Add(toggle)

        #add plate button
        plate = platbtn.PlateButton(self, label='Plate Button')
        sizer.Add(plate)
        plate = platbtn.PlateButton(self, label= 'withMenu',style=platbtn.PB_STYLE_DROPARROW)
        menu = wx.Menu('Action Menu')
        menu.Append(wx.ID_OPEN, 'Open it')
        menu.Append(wx.ID_CLOSE, 'close it')
        plate.SetMenu(menu)
        sizer.Add(plate)

        note="""long message that inform 
        the user abou what this message
        does !...."""
        lbl = 'CommandLink'
        cmdlnk = wx.adv.CommandLinkButton(self, mainLabel = lbl, note=note)
        vsizer.Add(cmdlnk)
        self.SetSizer(vsizer)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnToggle(self,event):
        btn = event.EventObject
        print('%s toggle button was pushed' % btn.Label)
        print('Toggle State: %s '% btn.Value)

    def OnButton(self, event):
        btn = event.EventObject
        print('%s  button was pushed' % btn.Label)
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()


