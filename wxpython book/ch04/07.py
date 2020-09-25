import xml.etree.ElementTree as ET
import wx

class XMLOutliner(wx.TreeCtrl):
    def __init__(self, parent, xmlText,*args,**kwargs):
        wx.TreeCtrl.__init__(self, parent,*args, **kwargs)
        rootElement = ET.fromstring(open(xmlText).read())
        root = rootElement.tag
        self._root = self.AddRoot(root)
        self.SetPyData(self._root, rootElement)
        self._populateTree(self._root, rootElement)
        self.Bind(wx.EVT_TREE_ITEM_GETTOOLTIP, self.OnToolTip)

    def _populateTree(self, parentNode, element):
        for child in element:
            node = self.AppendItem(parentNode, child.tag)
            self.SetPyData(node, element)
            self._populateTree(node, child)

    def _getDetails(self, element):
        xmlText = str(ET.tostring(element))
        items = xmlText.split('\n')
        return items[0]

    def OnToolTip(self, event):
        node = event.GetItem()
        data = self.GetPyData(node)
        tip = self._getDetails(data)
        event.SetToolTip(tip)


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        pnl = wx.Panel(self)
        sizer = wx.BoxSizer()
        tree = XMLOutliner(pnl,'xrcdlg.xrc')
        sizer.Add(tree,1, wx.EXPAND | wx.ALL, border=10)
        pnl.SetSizer(sizer)
        pnl.SetInitialSize()

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title='tree triying')
    frm.Show()
    app.MainLoop()