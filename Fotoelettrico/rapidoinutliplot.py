import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
from uncertainties import ufloat, unumpy

l = numpy.array([577, 546, 499, 449])
dl = numpy.array([11, 546*2/100, 11, 449*2/100])
f = 1/l * 3*10**5
df = f*dl/l
#Vmax = numpy.array([801, 876, 1095, 1289])
V = numpy.array([693, 808, 962, 1290])
dV = numpy.array([20, 10, 30, 30])
#dV = numpy.array([1, 4, 3, 3])*10
#V = (Vmax + Vmin)/2
#dV = (Vmax-Vmin)/2

#dati scarto
l2 = numpy.array([602, 405])
dl2 = numpy.array([12, 11])
V2 = numpy.array([926, 785])
dV2 = numpy.array([10, 10])
#dV2 = numpy.array([5, 3])*10
f2 =1/l2 *3*10**5
df2  =f2*dl2/l2

def ff(x, a, b):
    return a*x + b

popt = (3, 0)
pars, covm = curve_fit(ff, f, V, popt, dV, absolute_sigma = "true")
print("h/e=", pars[0],"pm", covm[0][0]**0.5)
print("W0=", pars[1],"\pm", covm[1][1]**0.5)

w = 1/((3.5*df)**2+dV**2)
chi2=(w*(ff(f, pars[0], pars[1])-V)**2).sum()
ndof = len(f)-2
print("chi2/ndof=",chi2,"/",ndof)

div = numpy.linspace(min(f)-200, max(f)+100, 1000)
pylab.plot(div, ff(div, pars[0], pars[1]), color = "black") 
pylab.errorbar(f, V, dV, df, linestyle = '', marker = 'o')
pylab.errorbar(f2, V2, dV2, df2, linestyle = "", color = "red", marker = "v")
pylab.xlabel("f (THz)", size = 16)
pylab.ylabel("V (mV)", size = 16)
pylab.title("Potenziale di azzeramento vs Frequenza", size = 16)
pylab.xlim(min(f2)-50, max(f2)+50)
pylab.ylim(min(V-200), max(V+200))
pylab.grid()
pylab.show()