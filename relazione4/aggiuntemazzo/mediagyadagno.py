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
INPUT = "datiguadagno.txt"

Vin,dVin,Vout, dVout = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori


VOUT = unumpy.uarray(Vout, dVout)
VOUT3 = unumpy.uarray(Vout, (dVout**2 + (0.03*Vout)**2)**0.5)
VIN = unumpy.uarray(Vin/1000, dVin/1000)
VIN3 = unumpy.uarray(Vin/1000, ((dVin**2 + (0.03*Vin)**2)**0.5)/1000)
A=VOUT3/VIN3
mediaA = A.mean()