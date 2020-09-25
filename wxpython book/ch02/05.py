import wx
import sys
from urllib.request import urlopen
import re
from abc import ABCMeta, abstractclassmethod


class CompleterDataSource():
    __metaclass__ = ABCMeta
    #@abstractmethod
    def getSuggestions(self, phrase):
        """return list of string"""
        pass

class GoogleSuggestionSource(CompleterDataSource):
    def getSuggestions(self, phrase):
        url = 'http://google.com/complete/search?output=toolbar&q='
        if phrase:
            response = urlopen(url+phrase)
            encoding = response.info().get_param('charset', sys.getdefaultencoding())
            page = response.read().decode(encoding)

            suggestions = re.findall(r'data="([\w*\s*]+)"', page)
            for i in suggestions:
                i = i.replace('%20',' ')
            return suggestions

class DataSourceTextCtrl(wx.TextCtrl):
    def __init__(self,parent, datasource):
        wx.TextCtrl.__init__(self, parent)
        assert isinstance(datasource, CompleterDataSource)
        self._dataSource = datasource
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def OnKeyDown(self,event):
        self.AutoComplete([])
        event.Skip()

    def OnChar(self,event):
        char = chr(event.KeyCode)
        if not char.isalnum(): char =""

        query = self.Value + char
        query = query.replace(' ','%20')
        tips = self._dataSource.getSuggestions(query)
        if tips: self.AutoComplete(tips)
        event.Skip()

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.text = DataSourceTextCtrl(self,GoogleSuggestionSource())
        self.btn = wx.Button(self,label='test')
        vsizer.Add(self.text)
        vsizer.Add(self.btn)
        #vsizer.Add(self.text2)
        self.SetSizer(vsizer)

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Test other button types')
    pnl = MyPanel(frm)
    frm.Show()
    app.MainLoop()