import wx
import wx.lib.langlistctrl as langlist
import wx.adv as adv

class LanguageComboBox(adv.BitmapComboBox):
    def __init__(self, parent):
        adv.BitmapComboBox.__init__(self, parent)

        for x in dir(wx):
            if x.startswith('LANGUAGE_'):
                langID= getattr(wx,x)
                flag = self.GetFlag(langID)
                name = wx.Locale.GetLanguageName(langID)
                self.Append(name, flag)

    def GetFlag(self, langID):
        flag = langlist.GetLanguageFlag(langID)

        if flag.IsOk():
            if flag.Size != (16,11):
                img = wx.Bitmap.ConvertToImage(flag)
                img.Rescale(16,11)
                flag = img.ConvertToBitmap()
        return flag


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        pnl = wx.Panel(self)

        #here to add stuff to Frame
        cmb = LanguageComboBox(pnl)

        sizer.Add(cmb, 1, wx.LEFT | wx.FIXED_MINSIZE | wx.ALL,5)


        pnl.SetSizer(sizer)
        self.SetInitialSize((400, 250))


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title='NoteBook Test')
    frm.Show()
    app.MainLoop()
