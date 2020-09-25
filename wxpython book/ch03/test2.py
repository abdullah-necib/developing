import wx


class StaticWrapText(wx.PyControl):
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.NO_BORDER,
                 validator=wx.DefaultValidator, name='StaticWrapText'):
        wx.PyControl.__init__(self, parent, id, pos, size, style, validator, name)
        self.statictext = wx.StaticText(self, wx.ID_ANY, label, style=style)
        self.wraplabel = label
        # self.wrap()

    def wrap(self):
        self.Freeze()
        self.statictext.SetLabel(self.wraplabel)
        self.statictext.Wrap(self.GetSize().width)
        self.Thaw()

    def DoGetBestSize(self):
        self.wrap()
        # print self.statictext.GetSize()
        self.SetSize(self.statictext.GetSize())
        return self.GetSize()


class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        text = "I'm subclasses the statictext because I want it to act exactly like a static text, but correctly wordwrap as needed. I've found several examples of it on the web, but none that worked how I wanted. The wordwrap makes it look much nicer when the user may decide to re-size the window, so I would definitely like to have it be wordwrapped. I know about the wx.lib.wordwrap, but chose to use the built in Wrap function of the statictext control instead. It basically does the same thing from what I understand."
        # txt = wx.StaticText(panel, label=text)
        txt = StaticWrapText(panel, label=text)
        wxbutton = wx.Button(panel, label='Button', size=wx.Size(120, 50))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txt, 0, wx.EXPAND, 5)
        sizer.Add(wxbutton, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)


# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
