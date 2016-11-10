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

def linear(x, a, b):
	return a*(x-b)**2

INPUT = "/home/federico/Laboratorio3/relazione5/ampiezzaSourceFollower.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione5/ampiezzaSourceFollowerEstesa.txt"

file = open(OUTPUT,"w")

Vin, dVin, Vout, dVout = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

V_IN = unumpy.uarray(Vin, dVin)
V_OUT = unumpy.uarray(Vout, dVout)

A_V = V_OUT/V_IN

for i in range(len(Vin)):
	file.write(str(Vin[i]))
	file.write("\t")
	file.write(str(dVin[i]))
	file.write("\t")
	file.write(str(Vout[i]))
	file.write("\t")
	file.write(str(dVout[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(A_V)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(A_V)[i]))
	file.write("\n")

file.close()
print(A_V)
mediaA = A_V.mean()

print("A medio = ", mediaA)
