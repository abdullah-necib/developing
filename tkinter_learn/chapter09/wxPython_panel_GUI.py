import wx

class GUI(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        parent.CreateStatusBar()
        menu = wx.Menu()
        menu.Append(wx.ID_ABORT,'About','Wx python GUI')
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT,'Exit','Exit the GUI')
        menuBar = wx.MenuBar()
        menuBar.Append(menu, 'File')
        parent.SetMenuBar(menuBar)        
        button = wx.Button(self,label='Print',pos=(0,60))
        self.Bind(wx.EVT_BUTTON,self.printButton,button)
        self.textBox = wx.TextCtrl(self,size=(280,50),style=wx.TE_MULTILINE)
    def printButton(self,event):
        self.textBox.AppendText('Print Button has been clicked\n')

app = wx.App()
frame = wx.Frame(None)
GUI(frame)
frame.Show()
app.MainLoop()
                           