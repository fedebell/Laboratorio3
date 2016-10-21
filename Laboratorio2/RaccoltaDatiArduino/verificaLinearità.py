import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

import pylab
import numpy

#FIXME: Aggiungere gli errori sulle tensioni misurate da voltmetro, usare funzioni di Petrillo
#Dati di più tensioni:
pylab.rc("font", size = 18)
V = numpy.array([0.20, 0.46, 0.80, 1.10, 1.86, 2.21, 2.53])
mis = numpy.array([40.89, 92.98, 162.045, 224.0, 379.8, 450.0, 515.0])
err = numpy.array([0.323, 0.227, 0.207, 0.13, 0.412, 0.134, 0.285])
print(V, mis, err)
pylab.title("Curva Calibrazione Arduino")
pylab.xlim(0, 3)
pylab.xlabel("DeltaV (V)")
pylab.ylabel("digit") #modificare gradi
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(V, mis, err, 0,  "o", color="black")

