import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0,5,0.1)
y = np.sin(x)**2
plt.plot(x,y)
show()
