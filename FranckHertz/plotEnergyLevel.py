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
import numpy as np
from scipy.signal import argrelextrema

#Prendo in due file ognuno contenenti i valori di U_E e quelli dei relativi massimi e minimi.

INPUTMIN = "/home/federico/Laboratorio3/FranckHertz/MIN.txt"
INPUTMAX = "/home/federico/Laboratorio3/FranckHertz/MAX.txt"

#Continuare a inserire gli errori e plottare i grafici e i fit con uan costante
#Indicare sul grafico il miglior valore da cui si sceglie di eseguire il fit succesivo

#L'errore su ue si prende dalle manopoline

ue, due, min1, dmin1, min2, dmin2, min3, dmin3 = pylab.loadtxt(INPUTMIN, unpack=True)
ue, due, max1, dmax1, max2, dmax2, max3, dmax3 = pylab.loadtxt(INPUTMAX, unpack=True)

UE = unumpy.uarray(ue, due)
MIN1 = unumpy.uarray(min1, dmin1)
MIN2 = unumpy.uarray(min2, dmin2)
MIN3 = unumpy.uarray(min3, dmin3)

MAX1 = unumpy.uarray(max1, dmax1)
MAX2 = unumpy.uarray(max2, dmax2)
MAX3 = unumpy.uarray(min3, dmax3)

pylab.figure(num=1, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('MIN', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$U_E$ (V)', size = "14")
pylab.ylabel('$U_A$ (V)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN1), 
	unumpy.std_devs(MIN1), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN2), 
	unumpy.std_devs(MIN2), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN3), 
	unumpy.std_devs(MIN3), unumpy.std_devs(UE), "o", color="black")


pylab.savefig("min.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)


pylab.figure(num=2, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('MAX', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('U_E (V)', size = "14")
pylab.ylabel('U_A (V)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX1), 
	unumpy.std_devs(MAX1), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX2), 
	unumpy.std_devs(MAX2), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX3), 
	unumpy.std_devs(MAX3), unumpy.std_devs(UE), "o", color="black")

pylab.savefig("max.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()

