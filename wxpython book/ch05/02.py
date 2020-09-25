# Chapter 5: Data Displays and Grids
# Recipe 2: Editing data lists
#
import re
import wx
import wx.lib.mixins.listctrl as listmix
# Module from recipe 1
import baselist
import inspect
RE_NAME = "[A-Z][a-z]*"
RE_EMAIL = ".+@email\.com"
RE_PHONE = "[0-9]{3}\-[0-9]{4}"


class PersonnelEditList(baselist.PersonnelList,
                        listmix.TextEditMixin, listmix.ListRowHighlighter):
    def __init__(self, parent):
        super(PersonnelEditList, self).__init__(parent)
        listmix.TextEditMixin.__init__(self)
        listmix.ListRowHighlighter.__init__(self)

        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnEdit)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.OnValidate)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDClick, self)

    def OnDClick(self, event):
        print(self.GetSelectedItemCount())


        # for k, v in inspect.getmembers(event):
        #     print(k,' >>> ',v)

    def OnEdit(self, event):
        item= event.Item
        # for k, v in inspect.getmembers(item):
        #     try:
        #         print(k,' >>> ',v,' ---- ',eval('item.'+k+'()') if k != 'Destroy' and  callable(v) else '')
        #     except Exception as err:
        #         print(err)
        # print(item.Column)
        # print(item.GetData())
        # if event.Item.Column == 0:
        #     # Don't allow edit of ID column values
        #     event.Veto()
        # else:
        #     event.Skip()

    def OnValidate(self, event):
        """Check input values and reject if bad data is present"""
        item = event.Item
        if item.Column != 0:
            validator = {1: RE_NAME,
                     2: RE_EMAIL,
                     3: RE_PHONE}.get(item.Column)
            ok = re.match(validator, item.Text)

            if not ok:
                event.Veto()
            else:
                print(item.Text)
                print(item.Column)
                event.Skip()
        else:
            event.Veto()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self._list = PersonnelEditList(self)

        # add some data
        self._list.AddEmployee("123", "Frank", "f@email.com", "555-1234")
        self._list.AddEmployee("124", "Jane", "j@email.com", "555-1434")
        self._list.AddEmployee("125", "Thor", "t@email.com", "555-1274")


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Editing lists of data")
        self.frame.Show();
        return True


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()