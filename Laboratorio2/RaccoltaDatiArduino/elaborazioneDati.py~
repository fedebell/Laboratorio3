import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

import pylab
import numpy

#carico dal un file i valori del la posizione dell'oggetto nelle x e per la posizione delle immagini nelle y nessun errore.
dati = pylab.loadtxt("dataProva.txt", unpack=True)
#dati = pylab.loadtxt("dataBoccoleFlottanti.txt", unpack=True)
print(dati)
# Format the plot.
pylab.rc("font", size = 18)
pylab.title("Istogramma", y = 1.02)
pylab.xlabel("Ingresso")
pylab.ylabel("Counts", labelpad = -5)
pylab.ylim(0, 600)
pylab.grid(color = "gray")
# Create the histogram.
pylab.hist(dati, bins = 7, range = (512, 519), color = "black")
#pylab.plot(dati, color = "black")

media = dati.sum()/(len(dati))
dev = (((dati-media)**2).sum()/(len(dati)))**0.5
print(media, dev)

#Dati:
#V = 1.51 +- 0.01 V (multimetro)
#n = (304.5 +- 0.6)
#fattore calibrazione = (496 +- 4) * 10^(-2) mV/digit
#Determinazione alternativa 
#V = (5.02 +- 0.03) V
#calibrazione = (491 +- 4) * 10^(-2) mV/digit

