import wx
import wx.grid as grid
import Tools.readCSV as read

class MyTableBase(grid.GridTableBase):
    def __init__(self):
        grid.GridTableBase.__init__(self)
        self._data = read.ReadCSV().GetCountriesData()
        self.columnName = [x for x in self._data[0].keys() if x != 'cities']
        print(self._data[0])

    def GetNumberCols(self):
        colCnt = len(self._data[0].keys())
        print('we have columns: ',colCnt)
        return colCnt-1

    def GetNumberRows(self):
        print('length of data is ',len(self._data))
        return len(self._data)

    def GetValue(self, row, col):
        # print('from getValue')

        # print(self.columnName)
        return str(self._data[row][self.columnName[col]])

    def GetColLabelValue(self, col):
        return self.columnName[col].upper()

    def CanMeasureColUsingSameAttr(self, col):
        return True


    def SetRowAttr(self, attr, row):
        pass




class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title)
        sizer = wx.BoxSizer()
        # pnlSizer = wx.BoxSizer()
        # pnl = wx.Panel(self)
        # pnlSizer.Add(wx.TextCtrl(pnl))
        # pnl.SetSizer(pnlSizer)
        # sizer.Add(pnl)
        self._grid = grid.Grid(self)

        self._data = MyTableBase()
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