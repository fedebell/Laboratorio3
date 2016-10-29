import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import uncertainties 
from uncertainties import unumpy
#in MHz ed esce in Hz
Rin=ufloat(15.2,0.2)
Cin=ufloat(230,10)
a=ufloat(19.6,0.1)
b=ufloat(94,1)
m=ufloat(17.6,0.3)
logft=(a-b)/m
ft=unumpy.pow(10,logft)*numpy.power(10,6)
print(ft)
# secondo taglio
a1=ufloat(19.6,0.1)
b1=ufloat(-1.4,0.1)
m1=ufloat(-19.6,0.2)
logft1=(a1-b1)/m1
ft1=unumpy.pow(10,logft1)*numpy.power(10,6)
print('ft1= ',ft1)
#attesoprimotaglio
ftatt=1/(pylab.pi*2*Rin*Cin)
print(ftatt)
