from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#--------------------------------------------------------------
fig = Figure(figsize=(12, 5), facecolor='white')
#--------------------------------------------------------------
axis = fig.add_subplot(111)

xValues  = [1,2,3,4]

yValues0 = [6,7.5,8,7.5]
yValues1 = [5.5,6.5,50,6]
yValues2 = [6.5,7,8,7]
yAll = [yValues0,yValues1,yValues2]
minY = min([y for alpha in yAll for y in alpha])
yUpperLimit = 20
maxY = max([y for yValues in yAll for y in yValues if y < yUpperLimit])

t0, = axis.plot(xValues, yValues0, color='red')
t1, = axis.plot(xValues, yValues1, color='blue')
t2, = axis.plot(xValues, yValues2, color='gold')

axis.set_xlabel('horizontal')
axis.set_ylabel('vertical')

#dynamic limit
axis.set_ylim(minY,maxY)
axis.set_xlim(min(xValues),max(xValues))
axis.grid()

fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')


def _destroyWindos():
    root.quit()
    root.destroy()


root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindos)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
