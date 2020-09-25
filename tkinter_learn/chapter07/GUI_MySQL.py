import tkinter as tk
from tkinter import ttk as ttk
from tkinter.scrolledtext import ScrolledText
from GUI_MySQL_class import MySQL


class OOP(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI Application')
        self.create_widgets()
        self.mySql = MySQL()

    def create_widgets(self):
        # Menu
        menu_main = tk.Menu(self.win)
        self.win.configure(menu=menu_main)

        menu_file = tk.Menu(menu_main, tearoff=0)
        menu_file.add_command(label='New')
        menu_file.add_command(label='Exit', command=self._quit)
        menu_main.add_cascade(label='File', menu=menu_file)

        # Tabs
        tabcontrol = ttk.Notebook(self.win)
        tabcontrol.grid(column=0, row=0, sticky=(tk.W, tk.E))

        tab_mysql = ttk.Frame(tabcontrol)
        tab_mysql.pack(expand=1, fill='both')
        tabcontrol.add(tab_mysql, text='MySQL')

        tab_widget = ttk.Frame(tabcontrol)
        tab_widget.pack(expand=1, fill='both')
        tabcontrol.add(tab_widget, text='Widgets')

        # LabelFrames tab_mysql
        frame_mysql = ttk.LabelFrame(tab_mysql, text='Python Database')
        frame_mysql.grid(column=0, row=0, sticky=(tk.W, tk.E), padx=8, pady=4)

        frame_bookQuotation = ttk.LabelFrame(tab_mysql, text='Book Quotation')
        frame_bookQuotation.grid(column=0, row=1, sticky=(tk.W, tk.E), padx=8, pady=4)

        # Labels tab_mysql
        label_bookTitle = tk.Label(frame_mysql, text='Book Title')
        label_bookTitle.grid(column=0, row=0, sticky=tk.W)
        label_page = ttk.Label(frame_mysql, text='Page')
        label_page.grid(column=1, row=0, sticky=tk.W)

        # Entries tab_mysql
        self.entry_insert = ttk.Entry(frame_mysql, width=30)
        self.entry_insert.grid(column=0, row=1, sticky=tk.W)
        self.entry_pageInsert = tk.Entry(frame_mysql, width=5)
        self.entry_pageInsert.grid(column=1, row=1, sticky=tk.W)

        self.entry_get = ttk.Entry(frame_mysql, width=30)
        self.entry_get.grid(column=0, row=2, sticky=tk.W)
        self.entry_pageGet = tk.Entry(frame_mysql, width=5)
        self.entry_pageGet.grid(column=1, row=2, sticky=tk.W)

        self.entry_mod = ttk.Entry(frame_mysql, width=30)
        self.entry_mod.grid(column=0, row=3, sticky=tk.W)
        self.entry_pageMod = tk.Entry(frame_mysql, width=5)
        self.entry_pageMod.grid(column=1, row=3, sticky=tk.W)

        # Buttons tab_mysql
        self.button_insert = ttk.Button(frame_mysql, text='Insert Quote', width=15, command= self.insertQuote)
        self.button_insert.grid(column=2, row=1, sticky=tk.W)

        self.button_get = ttk.Button(frame_mysql, text='Get Quote', width=15,command = self.getQuote)
        self.button_get.grid(column=2, row=2, sticky=tk.W)

        self.button_mod = ttk.Button(frame_mysql, text='Mody Quote', width=15)
        self.button_mod.grid(column=2, row=3, sticky=tk.W)

        # Scrolltext tab_mysql
        self.scroltext_bookQuotation = ScrolledText(frame_bookQuotation, heigh=15, \
                                                    width=self.entry_insert['width'] + self.entry_pageInsert['width'] \
                                                          + self.button_insert['width'] + 4, wrap=tk.WORD)
        self.scroltext_bookQuotation.grid(column=0, row=0, sticky=(tk.W, tk.E))

        for child in frame_mysql.winfo_children():
            child.grid_configure(padx=8, pady=3)
        for child in frame_bookQuotation.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def insertQuote(self):
        title= self.entry_insert.get()
        page = self.entry_pageInsert.get()
        quote = self.scroltext_bookQuotation.get(1.0,tk.END)
        self.mySql.insertBooks(title,page,quote)

    def getQuote(self):
        all_books = self.mySql.showBooks()
        print(all_books)
        self.scroltext_bookQuotation.insert(tk.INSERT,str(all_books) +'\n')


    def _quit(self):
        """used in menu_file command Exit"""
        self.win.quit()
        self.win.destroy()


if __name__ == '__main__':
    root = OOP()
    root.win.mainloop()
