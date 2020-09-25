import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Menu

win = tk.Tk()
win.title("Python GUI")
#win.geometry("600x500+800+200")
defaultColor = win['background']

def _quit():
    win.quit()
    win.destroy()
    exit()

#create menu bar
menu_bar = Menu(win)
win.configure(menu=menu_bar)

#create a file menu and add items to it
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit',command=_quit)
menu_bar.add_cascade(label='file',menu=file_menu)

#create help menu
help_menu = Menu(menu_bar,tearoff=0)
help_menu.add_command(label='About')
menu_bar.add_cascade(label='Help',menu=help_menu)
#create LabelFram mighty
mighty= ttk.LabelFrame(win, text='Mighty Python')
mighty.pack(expand=1, fill='both')


#mighty.grid(column=0, row=0, padx=8, pady=4)
#mighty.pack()

# Labels
a_label = ttk.Label(mighty, text="Enter a name")
a_label.grid(column=0, row=0,sticky=tk.W)
ttk.Label(mighty, text="Choose a number").grid(column=1, row=0,sticky=tk.W)

#action buttom callback()
def click_me():
    action.configure(text="Hello " + name.get() + " " + number.get() + ' ' + str(chVarEn.get()))
    win.configure(background=defaultColor)
    # action.configure(state="disabled")

# action button
action = ttk.Button(mighty, text="Click Me", command=click_me)
action.grid(column=2, row=0,padx=10,pady =3)

# Text Entry
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=20, textvariable=name)
name_entered.grid(column=0, row=1)
# ComboBox
number = tk.StringVar()
number_choosen = ttk.Combobox(mighty, width=20, textvariable=number)
number_choosen["values"] = (1, 2, 4, 42, 100)
number_choosen.grid(column=1, row=1)
number_choosen.current(3)

# Check Button
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text='Unchecked', variable=chVarUn)
check2.grid(column=1, row=2, sticky=tk.W)
check2.select()
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text='Enabled', variable=chVarEn)
check3.grid(column=2, row=2, sticky=tk.W)
check3.deselect()

# using Scrolled text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, heigh=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3,sticky=tk.W+tk.E,padx=4,pady=4)

# redefine colors
colors = ["Blue", "Gold", "Red"]

# radiobutton callback
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


# create 3 Radiobutton using 1 variable
radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=4, sticky=tk.W)


#creating lable frame object
buttons_frame = ttk.LabelFrame(mighty,text="Lables in Frame")
buttons_frame.grid(column=0, columnspan=3,row=5,sticky=tk.W+tk.E,padx=8,pady = 4)
ttk.Label(buttons_frame,text='label1.... tooo long label name').grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text='label2').grid(column=0,row=1,sticky=tk.W)
ttk.Label(buttons_frame,text='label3').grid(column=0,row=2,sticky=tk.W)
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)




#do not remove this line
def get_attr(widget):
    for k in widget.keys():
        print(k, "   ", widget[k])
get_attr(ttk.LabelFrame())

name_entered.focus()
win.mainloop()
