import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

V, dV, I, dI = pylab.loadtxt("data00.txt", unpack="True")

#Best fit analitico
#Dy e Dx sono le colonne di errori
x = V
Dx = dV
y = I
Dy = dI

#set error an statistical weight
sigma = Dy
w = 1/(sigma**2)

#determine the coefficients
c1 = (w*(x**2)).sum()
c2 = (w*y).sum()
c3 = (w*x).sum()
c4 = (w*x*y).sum()
c5 = (w).sum()
Dprime = c5*c1-c3**2

a = (c1*c2-c3*c4)/Dprime
b = (c5*c4-c3*c2)/Dprime

Da = numpy.sqrt(c1/Dprime)
Db = numpy.sqrt(c5/Dprime)

#define the linear function
#note how paramters are entered
#note the syntax

def ff(x, aa, bb):
        return aa+bb*x
        
#calculate the chisquare for the best fit function
chi2 = ((w*(y-ff(x, a, b))**2)).sum()

#determine the ndof
ndof = len(x)-2

#print results on the console
print("I_0 = ", a, " DI_0 = ", Da, "R = ", 1/b, Db/(b**2))
print(chi2, ndof)

#prepare a dummy xx array (with 100 linearly spaced points)
xx = numpy.linspace(min(x), max(x), 100)

pylab.title("Best fit analitico")
pylab.xlabel("Delta V (V)")
pylab.ylabel("I (mA)") #modificare gradi
pylab.grid(color = "gray")
pylab.xlim(0, 1.1*max(V)) 
pylab.ylim(0, 1.1*max(I))
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, "o", color="black")

#plot the fitting curve 
pylab.plot(xx, ff(xx, a, b), color = 'red')

chisq = (((I - ff(V, a, b))/dI)**2).sum()
ndof = len(V) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof 2 = %f/%d" % (chisq, ndof))
print("p = ", p)

pylab.show()

