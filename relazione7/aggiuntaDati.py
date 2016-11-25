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

INPUT = "/home/federico/Laboratorio3/relazione7/ampiezze.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione7/ampiezzeEstese.txt"

file = open(OUTPUT,"w")

#aplificatore di carica
Vmeno = ufloat(200, 4)/1000
CT = ufloat(1.01, 1.01*0.04)
CF = ufloat(1.02, 1.02*0.04)
C1 = ufloat(21.9, 21.9*0.04)
R3 = ufloat(97.8, ((0.008*97.8)**2+0.1**2)**0.5)
R2 = ufloat(99.9, ((0.008*99.9)**2+0.1**2)**0.5)
R1 = ufloat(98.3, ((0.008*98.3)**2+0.1**2)**0.5)
VIN = unumpy.uarray([6.00, 4.00, 2.02], [0.06, 0.04, 0.01])
deltaT = unumpy.uarray([336, 293, 220], [4, 4, 4])

Vin, dVin = pylab.loadtxt(INPUT, unpack=True)
VIN = unumpy.uarray(Vin, dVin)

print("C1 = ", C1)
print("CT = ", CT)
print("CF = ", CF)
print("R3 = ", R3)
print("R2 = ", R2)
print("R1 = ", R1)

VSHMAXATT = VIN*CT/CF

print("V SH ATT MAX = ", VSHMAXATT)

dtatteso = -R1*CF*unumpy.log(Vmeno*CF/(VIN*CT))
print(dtatteso)

for i in range(len(Vin)):
	file.write(str(Vin[i]))
	file.write("\t")
	file.write(str(dVin[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(dtatteso)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(dtatteso)[i]))
	file.write("\n")

file.close()
