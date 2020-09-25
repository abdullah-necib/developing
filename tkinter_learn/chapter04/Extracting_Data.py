#!/usr/bin/env python3
import tkinter as tk
from time import sleep
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
from tkinter import PhotoImage

GLOBAL_CONST = 42
win = tk.Tk()
win.title('Python GUI')
img = PhotoImage('mini.ico')
# win.iconbitmap('mini.ico')
win.tk.call('wm', 'iconphoto', win._w, img)


# ===========================================
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        if self.tip_window or not tip_text: return
        x, y, _cx, cy = self.widget.bbox("insert")  # get size of widget
        # print(self.widget.bbox('insert'))
        x = x + self.widget.winfo_rootx() + 10  # calculate display tooltip
        y = y + cy + self.widget.winfo_rooty() + 10
        # print('new result %d   %d'%(x,y))
        # print(self.widget.winfo_rootx().__doc__)
        self.tip_window = tw = tk.Toplevel(self.widget)  # create new tooltip windows
        tw.wm_overrideredirect(True)  # remove all windows manager (wm) decorations
        tw.wm_geometry('+%d+%d' % (x, y))
        # print('+%d+%d'%(x,y))
        # print(self.widget.geometry())   there is an error
        label = tk.Label(tw, text=tip_text, justify=tk.LEFT
                         , background='#ffffe0', relief=tk.SOLID, borderwidth=1
                         , font=('tohama', '10', 'normal'))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


# ===========================================
def create_Tooltip(widget, text):
    tooltip = ToolTip(widget)

    def enter(event):
        tooltip.show_tip(text)

    def leave(event):
        tooltip.hide_tip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# ===========================================

# display messagebox callback()
def msgBox():
    # msg.showinfo('Python message info box','a python gui created using tkinter\nyear is 2020')
    # msg.showerror('Error','this is error test')
    answer = msg.askyesnocancel('answer', 'do you want to print')
    print('{0} and result is  {1}'.format(type(answer), answer))


# create quit fun
def _quit():
    win.quit()
    win.destroy()
    exit()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
this call should be removed
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
win.after(60000, _quit)  # this call should be removed
"""----------------------------------------------------------------"""


# define a function for grid
def cr(widget, a, b, padx=4, pady=4, **kwr):
    widget.grid(column=a, row=b, padx=4, pady=4, **kwr)


# create menu
menu_bar = Menu(win)
win.configure(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label="Exit", command=_quit)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=msgBox)
menu_bar.add_cascade(menu=file_menu, label='File')
menu_bar.add_cascade(menu=help_menu, label='Help')

# create tab control
tabControl = ttk.Notebook(win)
# create the first tab
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
# add the tab to tab control
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='tab 2')
tabControl.add(tab3, text='tab 3')
tabControl.pack(expand=1, fill='both', padx=5, pady=5)

# create CANVAS -----------

tab3_fram = tk.Frame(tab3, bg='blue')
tab3_fram.pack(expand=1, fill='both')
for orange_color in range(10):
    if orange_color % 2 == 0:
        canvas = tk.Canvas(tab3_fram, width=200, height=10,
                           highlightthickness=0, bg='orange')

    else:
        canvas = tk.Canvas(tab3_fram, width=200, height=10,
                           highlightthickness=0, bg='blue')
    canvas.grid(row=orange_color, column=0)
# create LabelFrame
mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)
mighty2 = ttk.LabelFrame(tab2, text='the Snake')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# create Label
a_label = ttk.Label(mighty, text='Enter a name')
a_label.grid(column=0, row=0)
b_label = ttk.Label(mighty, text='choose a number')
b_label.grid(column=1, row=0)


# create button and button funtion
def click_me():
    action.configure(text='Welcome ' + entryVar.get())


action = ttk.Button(mighty, text='Click Me', command=click_me)
action.grid(column=2, row=0)

# create Entry
entryVar = tk.StringVar()
name_entry = ttk.Entry(mighty, width=20, textvariable=entryVar)
name_entry.grid(column=0, row=1, sticky='W')

# create combobox
number = tk.IntVar()
choose_number = ttk.Combobox(mighty, width=20, textvariable=number)
choose_number['values'] = (1, 2, 3, 14, 42, 100)
choose_number.grid(column=1, row=1)
choose_number.current(3)

# create textbox
scrol = scrolledtext.ScrolledText(mighty, heigh=5, width=60, wrap=tk.WORD)
scrol.grid(column=0, row=3, columnspan=3)

# create check box //MIGHTY 2
chDisVar = tk.IntVar()
chEnVar = tk.IntVar()
chSeVar = tk.IntVar()
chk1 = tk.Checkbutton(mighty2, text='Disabled', state=tk.DISABLED, variable=chDisVar)
chk2 = tk.Checkbutton(mighty2, text='Enabled', variable=chEnVar)
chk3 = tk.Checkbutton(mighty2, text='Selected', variable=chSeVar)
cr(chk1, 0, 0)
cr(chk2, 1, 0)
cr(chk3, 2, 0)
chk1.select()
chk2.select()
chk3.deselect()


# create RadioButton  //MIGHTY 2
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
        mighty2.configure(text=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
        mighty2.configure(text=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])
        mighty2.configure(text=colors[2])
    elif radSel == 3:  # win.configure(background=default)
        win.configure(background=colors[3][1])
        mighty2.configure(text=colors[3][0])


colors = ['blue', 'gold', 'red', ['default', win['background']]]
radVar = tk.IntVar()

for i in colors:
    cr(ttk.Radiobutton(mighty2, text=i[0] if type(i) == list else i, value=colors.index(i),
                       variable=radVar, command=radCall), colors.index(i), 1)
radVar.set(3)


# create spin box
def spinCall():
    value = spin.get()
    scrol.insert(tk.INSERT, value + '\n')


spin = tk.Spinbox(mighty, from_=0, to=10, width=10, bd=3, command=spinCall)
cr(spin, 2, 1)
create_Tooltip(spin, 'this is a spin tool')

# Create another frame and create labels inside // mighty2
label_frame = ttk.LabelFrame(mighty2, text='Labels in Frame')
cr(label_frame, 0, 2)
for i in range(3):
    ttk.Label(label_frame, text='label ' + str(i + 1)).grid(column=0, row=i, sticky=tk.W, padx=4, pady=4)

# add sticky to all mighty and mighty2 children
"""PERSONAL"""
for child in mighty.winfo_children():
    child.grid_configure(padx=8, pady=4, sticky=tk.W)
for child in mighty2.winfo_children():
    child.grid_configure(padx=8, pady=4, sticky=tk.W)


def get_attr(widget):
    """this is a test for the tag"""
    for k in widget.keys():
        print(k, "   ", widget[k])


get_attr(tk.LabelFrame())
print(__file__)

# create ttk.Progressbar
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=256,
                               mode='determinate')
cr(progress_bar, 0, 2, padx=4, pady=4, sticky=(tk.W, tk.E))


# create functions
def progress_run():
    progress_bar['maximum'] = 100
    for i in range(100):
        sleep(0.05)
        progress_bar['value'] = i
        progress_bar.update()
    progress_bar['value'] = 0


def progress_start():
    progress_bar.start()


def progress_stop():
    progress_bar.stop()


def progress_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)


# create LabelFrame for progressBar //MIGHTY2
progress_frame = ttk.LabelFrame(mighty2, text='Progress Bar functions')
cr(progress_frame, 1, 2)
cr(ttk.Button(progress_frame, text='Run', width=20, command=progress_run), 0, 0)
cr(ttk.Button(progress_frame, text='Start', width=20, command=progress_start), 0, 1)
cr(ttk.Button(progress_frame, text='Stop', width=20, command=progress_stop), 0, 2)
cr(ttk.Button(progress_frame, text='Stop after Sec', width=20, command=progress_stop_after), 0, 3)

"""
tk.Spinbox(mighty, relief=tk.RAISED).grid()
tk.Spinbox(mighty,relief=tk.SUNKEN).grid()
tk.Spinbox(mighty,relief=tk.FLAT ).grid()
tk.Spinbox(mighty,relief=tk.GROOVE ).grid()
tk.Spinbox(mighty,relief=tk.RIDGE ).grid()
"""
strData = spin.get()
print("Spinbox value is: "+strData)
def usingGolbal():
    global GLOBAL_CONST
    print('FUNTION USING global keyword: ' + str(GLOBAL_CONST))
    GLOBAL_CONST = 777
    print('assign value to GLOBAL_CONST : '+ str(GLOBAL_CONST))
usingGolbal()
print('outside function GLOVAL_CONST IS: ' +str(GLOBAL_CONST))

win.mainloop()