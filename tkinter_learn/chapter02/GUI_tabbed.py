import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python GUI')
default = win['background']

# create quit fun
def _quit():
    win.quit()
    win.destroy()
    exit()

def cr(widget,a,b):
    widget.grid(column=a, row=b)


# create menu
menu_bar = Menu(win)
win.configure(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label="Exit", command=_quit)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')
menu_bar.add_cascade(menu=file_menu, label='File')
menu_bar.add_cascade(menu=help_menu, label='Help')

# create tab control
tabControl = ttk.Notebook(win)
# create the first tab
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
# add the tab to tab control
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='tab2')
tabControl.pack(expand=1, fill='both',padx=5,pady=5)

# create LabelFrame
mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)
mighty2 = ttk.LabelFrame(tab2,text='the Snake')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# create Label
a_label = ttk.Label(mighty, text='Enter a name')
a_label.grid(column=0, row=0)
b_label = ttk.Label(mighty, text='choose a number')
b_label.grid(column=1, row=0)

#create button and button funtion
def click_me():
    action.configure(text='Welcome '+entryVar.get())

action = ttk.Button(mighty, text='Click Me', command=click_me)
action.grid(column=2,row=0)

#create Entry
entryVar = tk.StringVar()
name_entry = ttk.Entry(mighty, width = 20, textvariable=entryVar)
name_entry.grid(column=0, row=1,sticky='W')

#create combobox
number =tk.IntVar()
choose_number = ttk.Combobox(mighty,width=20,textvariable=number)
choose_number['values'] = (1,2,3,14,42,100)
choose_number.grid(column=1,row=1)
choose_number.current(3)

#create textbox
text_entry =scrolledtext.ScrolledText(mighty,heigh = 5, width=60, wrap=tk.WORD)
text_entry.grid(column=0,columnspan=3)

#create check box //MIGHTY 2
chDisVar =tk.IntVar()
chEnVar=tk.IntVar()
chSeVar = tk.IntVar()
chk1 = tk.Checkbutton(mighty2,text='Disabled', state=tk.DISABLED,variable=chDisVar)
chk2 = tk.Checkbutton(mighty2,text='Enabled', variable=chEnVar)
chk3 = tk.Checkbutton(mighty2,text='Selected',variable=chSeVar)
cr(chk1,0,0)
cr(chk2,1,0)
cr(chk3,2,0)
chk1.select()
chk2.select()
chk3.deselect()

#create RadioButton  //MIGHTY 2
def radCall():
    radSel = radVar.get()
    if radSel==0 :
        win.configure(background=colors[0])
        mighty2.configure(text=colors[0])
    elif radSel==1:
        win.configure(background=colors[1])
        mighty2.configure(text=colors[1])
    elif radSel==2:
        win.configure(background=colors[2])
        mighty2.configure(text=colors[2])
    elif radSel ==3: #win.configure(background=default)
        win.configure(background=colors[3][1])
        mighty2.configure(text=colors[3][0])

colors = ['blue','gold','red',['default', win['background']]]
radVar = tk.IntVar()

for i in colors:
    cr(ttk.Radiobutton(mighty2,text=i[0] if type(i)==list else i, value=colors.index(i),\
                       variable=radVar,command=radCall),colors.index(i),1)
radVar.set(3)

#Create another frame and create labels inside
label_frame = ttk.LabelFrame(mighty2,text='Labels in Frame')
cr(label_frame,0,2)
for i in range(3):
    ttk.Label(label_frame,text='label '+str(i+1)).grid(column=i,row=0,sticky=tk.W,padx=4,pady=4)



for child in mighty.winfo_children():
    child.grid_configure(padx=8, pady=4,sticky=tk.W)
for child in mighty2.winfo_children():
    child.grid_configure(padx=8, pady=4,sticky=tk.W)
win.mainloop()
