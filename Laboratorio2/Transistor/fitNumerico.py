import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

V1, V2 = pylab.loadtxt("dati1.txt", unpack="True")

dV1 = numpy.array([1.0 for i in range(len(V1))])
dV2 = numpy.array([1.0 for i in range(len(V2))])

V1 = (V1/1023)*5
dV1 = (dV1/1023)*5
V2 = (V2/1023)*5
dV2 = (dV2/1023)*5

Rc = 1000

Ic = 1000*(V1-V2)/Rc #Controllare il segno

I = Ic

V = V2
dV = dV2
dI = (dV1+dV2)/Rc


pylab.title("Retta di carico")
pylab.xlabel("Vce(V)")
pylab.ylabel("I(mA)") #modificare gradi
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, "o", color="black")


V1, V2 = pylab.loadtxt("dati4.txt", unpack="True")


dV1 = numpy.array([1.0 for i in range(len(V1))])
dV2 = numpy.array([1.0 for i in range(len(V2))])

V1 = (V1/1023)*5
dV1 = (dV1/1023)*5
V2 = (V2/1023)*5
dV2 = (dV2/1023)*5

Rc = 1000

Ic = 1000*(V1-V2)/Rc #Controllare il segno

I = Ic

V = V2
dV = dV2
dI = (dV1+dV2)/Rc

pylab.errorbar(V, I, dI, dV, "o", color="black")

V1, V2 = pylab.loadtxt("dati5.txt", unpack="True")

dV1 = numpy.array([1.0 for i in range(len(V1))])
dV2 = numpy.array([1.0 for i in range(len(V2))])

V1 = (V1/1023)*5
dV1 = (dV1/1023)*5
V2 = (V2/1023)*5
dV2 = (dV2/1023)*5

Rc = 1000

Ic = 1000*(V1-V2)/Rc #Controllare il segno

I = Ic

V = V2
dV = dV2
dI = (dV1+dV2)/Rc

pylab.errorbar(V, I, dI, dV, "o", color="black")

V1, V2 = pylab.loadtxt("dati1.txt", unpack="True")

dV1 = numpy.array([1.0 for i in range(len(V1))])
dV2 = numpy.array([1.0 for i in range(len(V2))])

V1 = (V1/1023)*5
dV1 = (dV1/1023)*5
V2 = (V2/1023)*5
dV2 = (dV2/1023)*5

Rc = 1000

Ic = 1000*(V1-V2)/Rc #Controllare il segno

I = Ic

V = V2
dV = dV2
dI = (dV1+dV2)/Rc

pylab.errorbar(V, I, dI, dV, "o", color="black")

V1, V2 = pylab.loadtxt("dati7.txt", unpack="True")

dV1 = numpy.array([1.0 for i in range(len(V1))])
dV2 = numpy.array([1.0 for i in range(len(V2))])

V1 = (V1/1023)*5
dV1 = (dV1/1023)*5
V2 = (V2/1023)*5
dV2 = (dV2/1023)*5

Rc = 1000

Ic = 1000*(V1-V2)/Rc #Controllare il segno

I = Ic

V = V2
dV = dV2
dI = (dV1+dV2)/Rc

pylab.errorbar(V, I, dI, dV, "o", color="black")

#I dati della retta di carico si misurano manualmente sul circuito con il multimetro Vce e Ic, anche Ib era misurata con il multimetro


#Dati retta di carico di cui fare il fit
Vce = numpy.array([4.40, 4.40, 4.72])
#dVce = numpy.array([0.0, 0.0, 0.0])
Ic = numpy.array([1.0, 1.8, 2.9])
dIc = numpy.array([0.1, 0.1, 0.1])

#Smagheggi a caso da togliere e inserire i dati puliti
#Ic = (4.97-Vce)/1000
Vce = 4.97-Ic


init = numpy.array([0.1, 1.0])
#error = dI +dV/k  k--> k è il fattore di conversione
popt, pcov = curve_fit(fit_function, Vce, Ic, init, dIc) 
a, b = popt
vara, varb = pylab.sqrt(pcov.diagonal())

pylab.errorbar(Vce, Ic, dIc, 0, "o", color="black")

covarab = pcov[1,0]

print(pcov)
print("Parametri del fit")
print("R = ", a, "dR = ", vara)
print("I_0", b, "dI_0", varb)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (Vce.max())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = fit_function(bucket[i], a, b)

pylab.plot(bucket, retta, color = "red")

#Calcolo di un valore di I e della sua incertezza, dato un valore di Vce calcolo usando il fit fatto prima quanto vale con incertezza il punto di lavoro
Vingresso = 2
Iteorico = a + b*Vingresso
dIteorico = (vara**2 + (Vingresso * varb)**2 + 2*(Vingresso)*covarab)**0.5

print("I' = ", Iteorico, "dI' = ", dIteorico)

pylab.show()
