import pylab
import numpy
from scipy.optimize import curve_fit

# data load
x,Dx,y,Dy=pylab.loadtxt('nomefile.txt',unpack=True)

# scatter plot with error bars
pylab.errorbar(x,y,Dy,Dx,linestyle = '', color = 'black', marker = 'o')

# bellurie 
pylab.rc('font',size=16)
pylab.xlabel('$\Delta V$  [V]')
pylab.ylabel('$I$  [mA]')
pylab.title('Data plot w numerical fit')
pylab.minorticks_on()

# make the array with initial values
init=(0,2)

# set the error
sigma=Dy
w=1/sigma**2

# define the linear function
# note how parameters are entered
# note the syntax
def ff(x, aa, bb):
    return aa+bb*x

# call the routine
pars,covm=curve_fit(ff,x,y,init,sigma)

# calculate the chisquare for the best-fit funtion
# note the indexing of the pars array elements
chi2 = ((w*(y-ff(x,pars[0],pars[1]))**2)).sum()

# determine the ndof
ndof=len(x)-len(init)

# print results on the console
print(pars)
print(covm)
print (chi2, ndof)

# print the same in a slightly more readible version
print('a = ', pars[0], '+/-', numpy.sqrt(covm[0,0]))
print('b = ', pars[1], '+/-', numpy.sqrt(covm[1,1]))
print('norm cov = ', covm[0,1]/(numpy.sqrt(covm[0,0]*covm[1,1])))

# prepare a dummy xx array (with 100 linearly spaced points)
xx=numpy.linspace(min(x),max(x),100)

# plot the fitting curve
pylab.plot(xx,ff(xx,pars[0],pars[1]), color='red')

# save the plot in pdf format for further use
pylab.savefig('fig3bestfit.pdf') 

# show the plot
pylab.show()
