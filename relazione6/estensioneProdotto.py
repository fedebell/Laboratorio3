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

INPUT = "/home/federico/Laboratorio3/relazione6/prodottoCostante.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione6/datiProdottoEstesi.txt"

file = open(OUTPUT,"w")

Vout, dVout, VoutFede, f, df = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

R1 = ufloat(218, ((0.008*218)**2+1)**0.5)
P1 = ufloat(97.8, ((0.008*97.8)**2+0.1**2)**0.5)*1000
V_IN = ufloat(0.340, 0.002)

V_OUT = unumpy.uarray(Vout, dVout)
F = unumpy.uarray(f, df)

A_V = V_OUT/V_IN

G = A_V * f

for i in range(len(V_OUT)):
	file.write(str(Vout[i]))
	file.write("\t")
	file.write(str(dVout[i]))
	file.write("\t")
	file.write(str(f[i]))
	file.write("\t")
	file.write(str(df[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(A_V)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(A_V)[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(G)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(G)[i]))
	file.write("\n")

file.close()

pylab.show()
