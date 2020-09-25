import wx
import wx.adv as adv

class DatePicker(adv.DatePickerCtrl):
    def __init__(self, parent, dt, style=adv.DP_DEFAULT):
        adv.DatePickerCtrl.__init__(self, parent=parent, dt=dt, style=style)
        self.SetInitialSize((200,-1))


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        now = wx.DateTime.Now()
        self._dp = DatePicker(parent= self, dt = now, style=adv.DP_DROPDOWN)
        sizer.Add(self._dp,0, wx.ALL,20)
        self.SetSizer(sizer)
        self.gdpc = adv.GenericDatePickerCtrl(self,dt=now)
        sizer.Add(self.gdpc)
        self.t = adv.TimePickerCtrl(self,dt=now)
        sizer.Add(self.t)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.pnl = MyPanel(self)
        self.Bind(adv.EVT_DATE_CHANGED, self.OnDateChange)
    def OnDateChange(self, event):
        date = event.GetDate()
        print(type(date))
        self.Title = date.Format('%d.%m.%Y')


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None,title='this is a new frame')
    frm.Show()
    app.MainLoop()