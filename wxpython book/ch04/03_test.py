import wx
import wx.propgrid as propgrid
import inspect
import ast
class InspectorGrid(propgrid.PropertyGrid):
    def __init__(self, parent):
        propgrid.PropertyGrid.__init__(self, parent)
        self.Bind(propgrid.EVT_PG_CHANGED, self.OnChange)
        self.valuesTypes = []

    def OnChange(self,event):
        prop = event.GetProperty()
        name = prop.GetName()
        val = prop.GetValue()
        print('we reach changing event')

        pass

    def SetObject(self, obj):
        self.Clear()
        self.Show() #this is added because we have to start the pg.PropertyGrid() object
        methods =[]
        self.Append(propgrid.PropertyCategory('Attributes'))
        if obj is not None:
            for name, val in inspect.getmembers(obj):
                if callable(name):
                    methods.append((name, val))
                else:
                    self.AddAttribute(name, val)
        self.Append(propgrid.PropertyCategory('Methods'))
        for m in methods:
            self.Append(self.AddMethod())
        # self.valuesTypes.sort()
        for i in self.valuesTypes:
            print(i)
        pass

    def GetProperty(self, name, val):
        pmap = {bool : propgrid.BoolProperty,
                int: propgrid.IntProperty,
                float: propgrid.FloatProperty,
                str : propgrid.StringProperty,
                wx.Colour: propgrid.ColourProperty,
                wx.Font : propgrid.FontProperty,
                wx.Size : SizeProperty
                }
        prop = pmap.get(type(val))
        if type(val) not in self.valuesTypes:
            self.valuesTypes.append(type(val))
        # print(prop)

    def AddAttribute(self, name, val):
        prop = self.GetProperty(name, val)



    def AddMethod(self, name, val):
        pass

class SizeProperty(propgrid.PyProperty):
    def __init__(self, value=''):
        super.__init__()
        self.value = value

    def StringToValue(self, text):



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        pnl = wx.Panel(self)
        sizer = wx.BoxSizer()
        obj = InspectorGrid(pnl)
        obj.SetObject(obj)
        sizer.Add(obj, wx.EXPAND | wx.ALL, 5)
        pnl.SetSizer(sizer)
        pnl.SetInitialSize()

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None, title='Test Grid')
    frm.Show()
    app.MainLoop()