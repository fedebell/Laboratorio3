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
	return a*x+b

INPUT = "/home/federico/Laboratorio3/relazione6/datiDerivatore.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione6/datiDerivatoreEstesi.txt"

file = open(OUTPUT,"w")

f, df, Vout, dVout, t, dt = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

F = unumpy.uarray(f, df)
T = unumpy.uarray(t, dt)/1000000
V_OUT = unumpy.uarray(Vout, dVout)
PHI = 2*F*T
PHI = 1-PHI

for i in range(len(f)):
	file.write(str(f[i]))
	file.write("\t")
	file.write(str(df[i]))
	file.write("\t")
	file.write(str(Vout[i]))
	file.write("\t")
	file.write(str(dVout[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(PHI)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(PHI)[i]))
	file.write("\n")

file.close()


