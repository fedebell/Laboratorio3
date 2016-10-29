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

INPUT = "/home/federico/Laboratorio3/relazione4/datiAmpiezza.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione4/datiAmpiezzaEstesi.txt"

Vin, dVin, Vout, dVout, t, dt = pylab.loadtxt(INPUT, unpack=True)

f = ufloat(5.00, 5.00/100.0)

VIN = unumpy.uarray(Vin, dVin)
VIN3 = unumpy.uarray(Vin, ((dVin)**2 + (0.03*Vin))**0.5)
VOUT = unumpy.uarray(Vout, dVout)
VOUT3 = unumpy.uarray(Vout, ((dVout)**2 + (0.03*Vout))**0.5)
T = unumpy.uarray(t, dt)
PHI = 2*3.14*T*f
A = VOUT/VIN
mediaA = A.mean()

file = open(OUTPUT,"w")

for i in range(len(A)):
	file.write(str(unumpy.nominal_values(VIN3)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(VIN3)[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(VOUT3)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(VOUT3)[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(A)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(A)[i]))
	file.write("\n")


file.close()








