import builtins
import wx
import wx.stc as stc
import inspect
import wx.html2
#import bs4.BeautifulSoup as bs
import bs4
cnt=0
with open('/home/abdullah/Documents/inspectFile.log','w') as f:
    for name, value in inspect.getmembers(bs4.element.Tag):
        if name.lower().find('') != -1:
            strval =  str(cnt)+'\t'+name+ '\t'+str(value)+'\n'
            print(strval)
            f.write(strval)
            cnt += 1

print('done')


    
