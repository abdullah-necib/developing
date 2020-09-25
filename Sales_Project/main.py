import wx
import wx.lib.agw.aui as aui
import GUI.containers as containers



class MainFrame(wx.Frame):
    """this is the main frame for all application"""
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self,*args, **kwargs)
        self._mgr = aui.AuiManager(self)
        self.countriesTREE = containers.CountriesTree(self)
        self.mainPNL = wx.Panel(self)
        self.tasksPNL = wx.Panel(self)

        self.SetupMainPNL()

        self.Show()
        self.Maximize(True)

    def SetupMainPNL(self):
        info = aui.AuiPaneInfo().Left().Name('Countries')
        info.CloseButton(True).Caption("Countries List")
        info.HasBorder()
        # info.BestSize(400,10)
        info.MinSize(300,10)
        # info.Fixed()

        self._mgr.AddPane(self.countriesTREE, info)
        self._mgr.Update()



if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='Sales Program')
    app.MainLoop()
