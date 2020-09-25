import wx
import math

def GetNames(module, startwith=''):
    counter =0
    #print(dir(wx))
    #print(dir('test.py'))
    for x in dir(module):
        if x.startswith(startwith):
            print('{0:10} *** {1:40} --- {2}'.format(counter, x, getattr(module,x)))
            counter = counter +1
    print('MODULE: ' + module.__file__)
    print('VERSION: ' + module.__version__)

if __name__ == '__main__':
    """use it like GetNames(module, 'start with a text') """
    GetNames(wx,'')
    # get help about a class
    # print(help(wx.Dialog))
