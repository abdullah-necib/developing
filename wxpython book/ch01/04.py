import wx
from time import sleep
from threading import Thread

class MyApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None,title='Test Binding Event')
        self.frame.Bind(wx.EVT_SHOW, self.OnFrameShow)
        self.frame.Bind(wx.EVT_CLOSE, self.OnFrameClose)
        self.frame.Show()
        return True

    def OnFrameShow(self,event):
        theFrame = event.EventObject
        wx.MessageBox('Frame %s Shown!' % theFrame.Title, 'mesage')
        t1 = Thread(target=self.startThread, args=(event,3,))
        t1.setDaemon(True)
        t1.start()


        event.Skip()

    def startThread(self,event,sec=10):
        sec =10
        for idx in range(sec):
            sleep(1)
            print('sleeping')


    def OnFrameClose(self,event):
        theFrame =event.EventObject
        print('Frame %s Closing!' %theFrame.Title)


        event.Skip()
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()