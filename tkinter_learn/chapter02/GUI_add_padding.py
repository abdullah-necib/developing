import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.geometry("400x300+800+200")
defaultColor = win['background']

# redefine colors
colors = ["Blue", "Gold", "Red"]

# using Scrolled text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, heigh=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=6, columnspan=2,sticky=tk.W+tk.E,padx=4,pady=4)
# Labels
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)
ttk.Label(win, text="Choose a number").grid(column=1, row=0)


def click_me():
    action.configure(text="Hello " + name.get() + " " + number.get() + ' ' + str(chVarEn.get()))
    win.configure(background=defaultColor)
    # action.configure(state="disabled")


# action button
action = ttk.Button(win, text="Click Me", command=click_me)
action.grid(column=2, row=1,padx=10,pady =3)
# Text Entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
# ComboBox
number = tk.StringVar()
number_choosen = ttk.Combobox(win, width=12, textvariable=number)
number_choosen["values"] = (1, 2, 4, 42, 100)
number_choosen.grid(column=1, row=1)
number_choosen.current(3)
# Check Button
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.grid(column=1, row=4, sticky=tk.W)
check2.select()
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.grid(column=2, row=4, sticky=tk.W)
check3.deselect()
name_entered.focus()


# radiobutton callback
def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=colors[0])
    elif radSel == 2:
        win.configure(background=colors[1])
    elif radSel == 3:
        win.configure(background=colors[2])


# create 3 Radiobutton using 1 variable
radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)
#creating lable frame object
buttons_frame = ttk.LabelFrame(win,text="Lables in Frame")
buttons_frame.grid(column=0, row=7,sticky=tk.W+tk.E,padx=20,pady = 40)
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
win.mainloop()
