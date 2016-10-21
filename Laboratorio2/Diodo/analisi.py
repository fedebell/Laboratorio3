import numpy
import math
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

def fit_function(x, a, b):
	return b*(numpy.exp(x/a)-1)

FileName='/home/federico/Documenti/Laboratorio2/Diodo/dati_arduino/dati.txt'
N1, N2 = pylab.loadtxt(FileName, unpack="True")

errN2 = numpy.array([1.0 for i in range(len(N2))])
errN1 = numpy.array([1.0 for i in range(len(N1))])

Rd = 3280.0
errRd = 30.0

eta = 4.89/1000
erreta = 0.02/1000

V1 = eta*N1
V2 = eta*N2

I = (V1-V2)/Rd

#Inserire errori per i i V
errV2 = (erreta/eta + errN2/N2)*V2
errV1 = (erreta/eta + errN1/N1)*V1

errI = (errRd/Rd)*I


#for i in range(len(I)):
#        errI[i] = 50e-06

for i in range(len(I)):
        if(I[i]==0.0): I[i] = 1.0e-11*i

for i in range(len(V2)):
        if(V2[i]==0.0): V2[i] = 1.0e-11*i

#da finire vorrei implementare quella cosa che sostituisco le colonne di punti con un solo punto ma non ne ho voglia
        
#number = 150
#minV = 0.30
#maxV = 0.70
#inc = (maxV - minV)/number

#volt = numpy.array([(minV + i*inc) for i in range(number)])
#voltaggiVeri = numpy.array([])
#ampere = numpy.array([])
#errVolt = numpy.array([0.0 for i in range(number)])
#errAmpere = numpy.array([0.0 for i in range(number)])
#count = numpy.array([])

#for i in range(number):
#        for j in range(len(V2)):
#                if(volt[i]<=V2[j]<=volt[i+1]):
#                        voltaggiVeri = numpy.append(voltaggiVeri, V2[
#                        errVolt[i] = errV2[j]
#                        errAmpere[i] = errI[j]
#                        ampere[i] += I[j]
#                        count[i] += 1
                        
#nonnulli = len(numpy.nonzero(count))
#aNonNulli = numpy.array([0.0 for i in range(nonnulli)])

#for i in range(nonnulli):
#        index = (numpy.nonzero(ampere))[i]
#        print(index)
#        aNonNulli[i] = ampere[index]


#V2 = volt
#I = ampere
#errI = errAmpere
#errV2 = errVolt

print(V2, I, errV2, errI)


pylab.title("Curva corrente tensione")
pylab.xlabel("V (V)")
pylab.ylabel("I (A)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(V2, I, errI, errV2, "o", color="black")


initial = numpy.array([0.0515, 6.75e-09])
error = errI+errV2/100 #NON posso prendere errore squadrato perchè mescolerei le unità di misura
popt, pcov = curve_fit(fit_function, V2, I, initial, error)
a, b = popt
print(a, b)
print(pcov)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (V2.max()-V2.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + V2.min()
        funzione[i] = fit_function(bucket[i], a, b)
pylab.plot(bucket, funzione, color = "red")

#calcolo il chi quadro
chisq = (((I - fit_function(V2, a, b))/error)**2).sum()
ndof = len(V2) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(V2)-3)
print("Carica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)


pylab.show()

#number = 150
#minV = 0.30
#maxV = 0.70
#inc = (maxV -minV)/number

#volt = numpy.array([(minV + i*inc) for i in range(number)])
#ampere = numpy.array([0.0 for i in range(number)])
#count = numpy.array([0 for i in range(number)])

#for i in range(number):
#        for j in range(len(V2)):
#                if(V2[j] == volt[i]):
#                        ampere[j] += I[i]
#                        count[j] += 1

#ampere = ampere/count

#V2 = volt
#I = ampere

                

