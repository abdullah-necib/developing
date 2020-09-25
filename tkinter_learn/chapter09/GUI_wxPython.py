import wx
BACKGROUNDCOLOR = (240,240,240,255)

class MainFrame(wx.Frame):
    def __init__(self, *args, **Kwargs):
        wx.Frame.__init__(self, *args, **Kwargs)
        self.createWidgets()
        self.Show()
    
    def exitGUI(self,event):
        self.Destroy()
        
    def createWidgets(self):
        #self.createStatusBar()
        #self.createMenu()
        self.createNoteBook()
    
    def createNoteBook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)
        notebook.AddPage(widgets,'Widgets')
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        boxsizer = wx.BoxSizer()
        boxsizer.Add(notebook,1,wx.EXPAND)
        panel.SetSizerAndFit(boxsizer)
        
    
class Widgets(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.panel = wx.Panel(self)
        self.createWidgetFrame()
        self.createManageFilesFrame()
        #self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()
        
    def createWidgetFrame(self):
        staticBox = wx.StaticBox(self.panel,-1,'Widget Frame',size=(285,-1))
        self.statBoxSizerV =wx.StaticBoxSizer(staticBox,wx.VERTICAL)
    
    def createManageFilesFrame(self):
        staticBox = wx.StaticBox(self.panel,-1,'Manage Files',size=(285,-1))
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox,wx.VERTICAL)
    
        
    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV,1,wx.ALL)
        boxSizerV.Add(self.statBoxSizerMgrV,1,wx.ALL)
        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)
    
    def addWidgets(self):
        self.addCheckBoxes()
        self.addRadioButtons()
        self.addStaticBoxWithLabels()
    
    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel,label='brows to file'))
        boxSizerH.Add(wx.TextCtrl(self.panel,size=(174,-1), value='z:'))
        
        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH1.Add(wx.Button(self.panel,label='copy file to: '))
        boxSizerH1.Add(wx.TextCtrl(self.panel,size=(174,-1),value='z:/backup'))
        
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)
        
        self.statBoxSizerMgrV.Add(boxSizerV)
        
    


app = wx.App()
MainFrame(None, size= (350,450))
app.MainLoop()
