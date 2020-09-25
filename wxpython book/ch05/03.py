import urllib.request
import json
import wx
import wx.grid as gridlib
import inspect
import Tools.readCSV as read

def InsepectDetails(obj,filter = ''):
    cnt = 1
    filter = filter.lower()
    for k,v in inspect.getmembers(obj):
        if k.lower().find(filter) > -1 :
            print(cnt,':  ',k,' >>> ',v)
            cnt +=1

class MyDataSource(gridlib.PyGridTableBase):
    def __init__(self):
        gridlib.PyGridTableBase.__init__(self)
        self._RetreiveData()

    def _RetreiveData(self):
        # url = 'https://api.githup.com/repos/RobinD42/wxpython'
        # query = 'commits?path=%s&per_page=100'
        # changes = query % 'CHANGES.txt'
        # print(url+changes)
        # fp = urllib.request.urlopen(url + changes)
        # InsepectDetails(fp,'')
        # header = dict(fp.info())
        # if fp is not None:
        #     print(' ********** fp is not None ***********')
        #     self._data = json.load(fp)
        self._data = read.ReadCSV().GetCountriesData()

    def GetNumberRows(self):
        return len(self._data)

    def GetNumberCols(self):
        return 3

    def GetValue(self, row, col):
        data = self._data[row]['commit']
        keys = {0: ('author', 'date'),
                1: ('author', 'name'),
                2: ('message,')}
        value = ''
        temp = data
        for key in keys[col]:
            value = temp[key]
            temp = value
        return value

    def GetColLabelValue(self, col):
        cols = ["Date", "Name", "Comment"]
        return cols[col]

    def GetRowLabelValue(self, row):
        return str(row + 1)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title)
        sizer = wx.BoxSizer()
        self._grid = gridlib.Grid(self)
        self._data = MyDataSource()
        self._grid.SetTable(self._data)
        self._grid.EnableEditing(False)
        self._grid.AutoSizeColumns()
        sizer.Add(self._grid, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title='Test')
    frm.Show()
    app.MainLoop()
