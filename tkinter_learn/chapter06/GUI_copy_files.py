# ======================
# imports
# ======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep
import test_dir.ToolTip as tt
from threading import Thread
import test_dir.Queues as bq
from queue import Queue
from tkinter import filedialog as fd
from os import path

GLOBAL_CONST = 42
fDir = path.dirname(__file__)
netDir = fDir + 'Backup'

def __init__(self):
    self.createWidgets()
    self.defaultFileEntries()

def defaultFileEnteries(self):
    self.fileEntry.delete(0,tk.END)
    self.fileEntry.insert(0,fDir)
    if len(fDir) > self.entryLen:
        self.fileEntry.config(width = len(fDir) + 3)
        self.fileEntry.config(state='readonly')
    self.newEntry.delete(0, tk.END)
    self.newEntry.insert(0, netDir)
    if len(netDir) > self.entryLen:
        self.newEntry.config(width =len(netDir) +3)


# ===================================================================
class OOP():
    def __init__(self):  # Initializer method
        # Create instance
        self.win = tk.Tk()

        tt.create_ToolTip(self.win, 'Hello GUI')

        # Add a title
        self.win.title("Python GUI")
        self.create_widgets()
        #create a queue
        self.qui_queue = Queue()


    # Modified Button Click Function
    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' +
                                   self.number_chosen.get())
        #self.create_thread()
        #print(self)
        bq.write_to_scroll(self)
        #self.use_queues()

    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')

    # GUI Callback
    def checkCallback(self, *ignored_args):
        # only enable one checkbutton
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

        # Radiobutton Callback

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.mighty2.configure(text='Blue')
        elif radSel == 1:
            self.mighty2.configure(text='Gold')
        elif radSel == 2:
            self.mighty2.configure(text='Red')

        # update progressbar in callback loop

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i  # increment progressbar
            self.progress_bar.update()  # have to call update() in loop
        self.progress_bar["value"] = 0  # reset/clear progressbar

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

        #####################################################################################

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tabControl)  # Create a tab
        tabControl.add(tab1, text='Tab 1')  # Add the tab
        tab2 = ttk.Frame(tabControl)  # Add a second tab
        tabControl.add(tab2, text='Tab 2')  # Make second tab visible

        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        # Modify adding a Label using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')
        self.name_entered.delete(0, tk.END)
        self.name_entered.insert(0,'<default name>')

        # Adding a Button
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)

        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        # Adding a Spinbox widget
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin)  # using range
        self.spin.grid(column=0, row=2, sticky=tk.W)

        # Using a scrolled Text control
        scrol_w = 40
        scrol_h = 10
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

        for child in mighty.winfo_children():  # add spacing to align widgets within tabs
            child.grid_configure(padx=4, pady=2)

            # =====================================================================================
        # Tab Control 2 ----------------------------------------------------------------------
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4,sticky=(tk.W, tk.E))

        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)

        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=0, sticky=tk.W)

        # trace the state of the two checkbuttons
        chVarUn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())
        chVarEn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())

        # First, we change our Radiobutton global variables into a list
        colors = ["Blue", "Gold", "Red"]

        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()

        # Next we are selecting a non-existing index value for radVar
        self.radVar.set(99)

        # Now we are creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar,
                                    value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)  # row=6
            # And now adding tooltips
            tt.create_ToolTip(curRad, 'This is a Radiobutton control')

        # create manage file fream
        mngFileFrame = ttk.LabelFrame(tab2, text='Manage Files ')
        mngFileFrame.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

        # Button Callback()
        def getFileName():
            print('hello from getFileName')
            fDir = path.dirname(__file__)
            fName = fd.askopenfilename(parent= self.win, initialdir = fDir)
            file.set(fName)


        # Add widget to Manage file name
        lb =ttk.Button(mngFileFrame,text="Browse to file",command= getFileName)
        lb.grid(column=0, row=0,sticky=tk.W)
        file = tk.StringVar()
        self.entryLen = scrol_w
        self.fileEntry = ttk.Entry(mngFileFrame,width=self.entryLen,textvariable= file)
        self.fileEntry.grid(column=1, row=0,sticky ='WE')

        logDir = tk.StringVar()
        self.newEntry = tk.Entry(mngFileFrame, width=self.entryLen,textvariable= logDir)
        self.newEntry.grid(column=1,row=1, sticky = tk.W)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            file = src.split('/')[-1]
            dst = self.newEntry.get() + '' + file
            try:
                shutil.copy(src, dst)
                msg.showinfo('Copies files to network','Success File Copied')
            except FileNotFoundError as Err:
                msg.showerror('Copy File To Network','**** FAILED TO COPY\n\n'+ str(Err))
            except Exception as Err:
                msg.showerror('Copy File To Network', '**** FAILED TO COPY\n\n' + str(Err))

        cb = ttk.Button(mngFileFrame, text='Copy To File',command= copyFile)
        cb.grid(column=0, row=1, sticky='WE')

        for child in mngFileFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

        # Add a Progressbar to Tab 2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0,
                                                                                                 sticky='W')
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1,
                                                                                                    sticky='W')
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2,
                                                                                                 sticky='W')
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3,
                                                                                                        sticky='W')

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=2, pady=2)

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

            # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Display a Message Box
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')

            # Add another Menu to the Menu Bar and an item


        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)  # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Change the main windows icon
        # self.win.iconbitmap('pyc.ico')

        # It is not necessary to create a tk.StringVar()
        # strData = tk.StringVar()
        strData = self.spin.get()
        print("Spinbox value: " + strData)

        # call function
        self.usingGlobal()

        self.name_entered.focus()

        # Add Tooltips -----------------------------------------------------
        # Add a Tooltip to the Spinbox
        tt.create_ToolTip(self.spin, 'This is a Spinbox control')

        # Add Tooltips to more widgets
        tt.create_ToolTip(self.name_entered, 'This is an Entry control')
        tt.create_ToolTip(self.action, 'This is a Button control')
        tt.create_ToolTip(self.scrol, 'This is a ScrolledText control')

    def method_in_a_thread(self, num):
        #print('Hi how are you?')
        for idx in range(1, num):
            sleep(1)
            self.scrol.insert(tk.INSERT, str(idx) + '\n')
            # self.scrol.insert(tk.INSERT,'Muhammed Bisir gunaydin....')
            # self.scrol.insert(tk.INSERT,'{0} x {1} = {2}\n'.format(idx,idx,idx*idx))
            self.scrol.see('end')
        # self.scrol.insert(tk.INSERT, 'thread is finished {0}'.format(self.run_thread))

        self.scrol.insert(tk.INSERT, '{0} is Alive ? {1}\n'.format(self.run_thread, self.run_thread.is_alive()))
        self.scrol.see('end')

    def create_thread(self,num):
        """used in click_me when we press the button"""
        self.run_thread = Thread(target=self.method_in_a_thread, args=[num])
        self.run_thread.setDaemon(True)
        self.run_thread.start()
        #print('createThread():  ',self.run_thread.is_alive())
        #print( self.run_thread.isAlive())
        write_thread = Thread(target=self.use_queues)
        write_thread.start()


    def use_queues(self):
        """from old version
        qui_queue = Queue()
        print(qui_queue)
        for idx in range(10): qui_queue.put('Message from queue '+ str(idx) )
        """
        while True:
            print(self.qui_queue.get())



# ======================
# Start GUI
# ======================
oop = OOP()
# run_thread = Thread(target=oop.method_in_a_thread)
oop.win.mainloop()
