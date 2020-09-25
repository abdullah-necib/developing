from abc import ABCMeta, abstractmethod
import wx
from urllib.request import urlopen
import re

class CompleteSuggestions():
    __metaclass__ = ABCMeta
    #@absrtactmethod
    def getSuggestions(self, phrase):
        pass

class GoogleSuggestions(CompleteSuggestions):
    def getSuggestions(self, phrase):
        url ='http://google.com/complete/search?output=toolbar&q='
        response = urlopen(url+phrase)
        html_response = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        decoded_html = html_response.decode(encoding)
        result = re.findall(r'data="([\w*\s*]+)"',decoded_html)
        for text in result:
            text = text.replace('%20',' ')
        return result

class DataSourceTextCtrl(wx.TextCtrl):
    def __init__(self, parent, datasource):
        wx.TextCtrl.__init__(self, parent)
        assert isinstance(datasource, CompleteSuggestions)
        self._dataSource = datasource
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def OnKeyDown(self, event):
        self.AutoComplete([])
        event.Skip()

    def OnChar(self, event):
        char = chr(event.KeyCode)
        if not char.isalnum() : char = ""
        query = self.Value + char
        query = query.replace(' ','%20')
        tips = self._dataSource.getSuggestions(query)
        print(tips)
        if tips : self.AutoComplete(tips)
        event.Skip()

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = DataSourceTextCtrl(self, GoogleSuggestions())
        sizer.Add(self.text, border=10)
        self.btn = wx.Button(self,label='only for test' )
        sizer.Add(self.btn, border=10)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()