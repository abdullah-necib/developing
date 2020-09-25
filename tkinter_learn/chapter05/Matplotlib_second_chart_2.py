from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12, 8), facecolor='white')
xValues = [1, 2, 3, 4]
yValues = [5, 7, 6, 8]
axis1 = fig.add_subplot(221)
axis2 = fig.add_subplot(222, sharex=axis1, sharey=axis1)
axis3 = fig.add_subplot(223, sharex=axis1, sharey=axis1)
axis4 = fig.add_subplot(224, sharex=axis1, sharey=axis1)
axis1.plot(xValues, yValues)
axis1.set_xlabel('horizontal label')
axis1.set_ylabel('vertical label')
axis1.grid(linestyle='-')
axis2.plot(xValues, yValues)
axis2.set_xlabel('horizontal label')
axis2.set_ylabel('vertical label')
axis2.grid(linestyle='-')
axis3.plot(xValues, yValues)
axis3.set_xlabel('horizontal label')
axis3.set_ylabel('vertical label')
axis3.grid(linestyle='-')
axis4.plot(xValues, yValues)
axis4.set_xlabel('horizontal label')
axis4.set_ylabel('vertical label')
axis4.grid(linestyle='-')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW',_destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
print(type(axis1))
root.deiconify()
root.mainloop()
