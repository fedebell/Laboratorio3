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

INPUT = "datiGuadagno.txt"
OUTPUT = "datiGuadagnoEstesi.txt"

Vin, dVin, Vout, dVout = pylab.loadtxt(INPUT, unpack=True)

f = ufloat(5.00, 5.00/100.0)

VIN = unumpy.uarray(Vin, dVin)/1000
VIN3 = unumpy.uarray(Vin, ((dVin)**2 + (0.03*Vin)**2)**0.5)/1000
VOUT = unumpy.uarray(Vout, dVout)
VOUT3 = unumpy.uarray(Vout, ((dVout)**2 + (0.03*Vout)**2)**0.5)
A = VOUT3/VIN3
mediaA = A.mean()
print(A)









