from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(4, 3), facecolor='white')
axis = fig.add_subplot(211)
xValues = [1, 2, 3, 4]
yValues = [5, 7, 6, 8]
axis.plot(xValues, yValues)
axis.set_xlabel('horizontial label')
axis.set_ylabel('vertical label')
axis.grid(linestyle='-')

def _destroyWindows():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOWS',_destroyWindows)
canvas = FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
root.update()
root.deiconify()
root.mainloop()
