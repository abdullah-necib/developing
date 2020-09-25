from pylab import show,arange,sin, plot,pi
x = arange(0.0,2.0,0.01)
print(type(x))
print(x)
plot(x,sin(2*x*pi))
show()