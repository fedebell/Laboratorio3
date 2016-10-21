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


#IMPORTANTE
#Nuova gestione degli errori: da ora in avanti si usa solo piu' la libreria uncertainties, questo rende inutile anche 
#un programma potente come shockwave, usate questo come riferimento per i futuri scrpt.
#E' possibile gestire anche le matrici di covarianza sui vettori con il formalismo di uncertainties ma finche' non ci serve non 
#lo implemento

f = 9.897
x = 2
print("%.2f", f)

Vl, Vce, dVl, dVce = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/dati2.txt', unpack=True)

VL = unumpy.uarray(Vl, dVl)
VCE = unumpy.uarray(Vce, dVce)


Rb = ufloat(46700, 400) 
Rl = ufloat(977, 8)

IC = VL/Rl

pylab.figure(2)
pylab.title('I_c vs V_be')
pylab.xlabel('V_ce (V)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")

pylab.errorbar(unumpy.nominal_values(VCE), 1000*unumpy.nominal_values(IC), 
	1000*unumpy.std_devs(IC), unumpy.std_devs(VCE), "o", color="black")

pylab.show()
