import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiGialliasintoto.txt", unpack = True)

def ff(x, b):
    return b + 0*x

popt = (-2)
pars, covm = curve_fit(ff, V, I, popt, dI, absolute_sigma = "true")
print("I_as=", pars[0],"\pm", covm[0][0]**0.5)

w = 1/dI**2
chi2=(w*(ff(V, pars[0])-I)**2).sum()
ndof = len(f)-1
print("chi2/ndof=",chi2,"/",ndof)

div = numpy.linspace(min(V), max(V), 1000)
pylab.plot(div, ff(div, pars[0]), color = "black") 
pylab.errorbar(V, I, dI, dV, color = "blue", linestyle = "", marker = "o")
pylab.xlabel("V (mV)")
pylab.ylabel("I (nA)")
pylab.grid()
pylab.show()