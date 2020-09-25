import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()
strData.set('Hello Stranger')
varData = strData.get()
print(varData)
intData = tk.IntVar()
print(intData)
print(intData.get())