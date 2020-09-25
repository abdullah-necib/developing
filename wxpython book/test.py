import wx
import wx.propgrid as pg
import inspect
import wx.lib.agw.flatnotebook as fnb

app = wx.App()
frm = wx.Frame(None, title='test')
frm.Show()
prop = pg.PropertyGrid(frm)
counter =0
obj = fnb.EVT_FLATNOTEBOOK_PAGE_CLOSING

for name, val in inspect.getmembers(obj):
    if name.lower().startswith(''):
        print(counter,' ',name, '-->', val)
        counter +=1
#print(inspect.getfullargspec(obj.StringToValue))
#print(help(wx.propgrid.PyProperty))
#for idx in  inspect.classify_class_attrs(pg.PyProperty):
    #print(idx)
    
import ast


#print(inspect.getfullargspec(fnb.FlatNotebook.__init__))
#print(help(ast.literal_eval))
#inspect.getmembers(fnb.EVT_FLATNOTEBOOK_PAGE_CLOSING)