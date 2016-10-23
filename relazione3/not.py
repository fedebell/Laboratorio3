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


R_1 = ufloat(146, 0.2)
R_2 = ufloat(100, 1)
R_L = ufloat(2.1, 0.1)

Vini = 0.0
Vins = 5.00
Vcc = ufloat(5.00, 0.03) 
Vbs = ufloat(0.680, 0.008)
Vbi = ufloat(0.0026, 0.0002)
Vcs = ufloat(0.0376, 0.008)
Vci = ufloat(4.8, 0.08)

Ibs = Vbs/R_2 + (Vins - Vbs)/R_1
Ibi = Vbi/R_2 + (Vini - Vbi)/R_1
Ics = (Vcc-Vcs)/R_L
Ici = (Vcc-Vci)/R_L

print("Ibs = ", Ibs, "\n")
print("Ibi = ", Ibi, "\n")
print("Ics = ", Ics, "\n")
print("Ici = ", Ici, "\n")
