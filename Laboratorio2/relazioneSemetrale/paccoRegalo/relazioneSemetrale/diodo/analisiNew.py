import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*(numpy.exp(V2/b)-1)


def fit_function_1(x, a, b):
	return a*(math.exp(V2/b)-1)

FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiEstesi.txt'
V, I, errI, errV = pylab.loadtxt(FileName, unpack="True")

pylab.title("Curva I-V del diodo")
pylab.xlabel("V (V)")
pylab.ylabel("I (A)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(V, I, errI, errV, "o", color="black")


pylab.show()
