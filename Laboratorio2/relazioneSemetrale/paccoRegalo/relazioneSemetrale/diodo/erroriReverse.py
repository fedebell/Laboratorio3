import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiDiretta.txt'
V, I = pylab.loadtxt(FileName, unpack="True")

errV = numpy.array([0.0 for i in range(len(V))])
fullscaleV = numpy.array([0.0 for i in range(len(V))])
rV = numpy.array([0.0 for i in range(len(V))])

for i in range(len(V)):
    errV[i], fullscaleV[i], rV[i] = lab.util_mm_esr(V[i], 'digital', 'volt')
    
errI = numpy.array([0.0 for i in range(len(V))])
fullscaleI = numpy.array([0.0 for i in range(len(V))])
rI = numpy.array([0.0 for i in range(len(V))])

for i in range(len(I)):
    errI[i], fullscaleI[i], rI[i] = lab.util_mm_esr(I[i], 'digital', 'ampere')

for i in range(len(I)):
    print(V[i], I[i], errI[i], errV[i])
