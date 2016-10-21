import lab
import pylab
import numpy
from scipy.optimize import curve_fit
import math
import scipy.stats

ts, Vs = pylab.loadtxt("datiProva91115_S.txt", unpack=True)
tc, Vc = pylab.loadtxt("datiProva91115_C.txt", unpack=True)

#Settare errore a 1 us oppure a deltat/2
dts = numpy.array([1.0 for i in range(len(ts))])
dVs = numpy.array([1.0 for i in range(len(Vs))])
dtc = numpy.array([1.0 for i in range(len(tc))])
dVc = numpy.array([1.0 for i in range(len(Vc))])

def f(t, a, tau, c):
    return a*numpy.exp(-t/tau)+c
    
initial = numpy.array([1000.0, 4000.0, 1.0])
#Propagazione statistica
error = (dts**2+dVs**2)**(0.5)
poptc, pcovc = curve_fit(f, tc, Vc, initial, error)
ac, tauc, cc = poptc
dac, dtauc, dcc = pylab.sqrt(pcovc.diagonal())
print("Carica Condensatore")
print("V_0", ac, dac, "Tau", tauc, dtauc, "c", cc, dcc)
print(pcovc)

    
initial = numpy.array([1000.0, 4000.0, 1.0])
popts, pcovs = curve_fit(f, ts, Vs, initial, error)
sa, taus, cs = popts
dsa, dtaus, dcs = pylab.sqrt(pcovs.diagonal())
print("Scarica Condensatore")
print("V_0", sa, dsa, "Tau", taus, dtaus, "c", cs, dcs)
print(pcovs)
#FIXME: printare le covarianze normalizzate

pylab.figure(1)
pylab.subplot(211)

pylab.title("Carica condensatore")
pylab.xlabel("Tempo (us)")
pylab.ylabel("Volt (Digit)")
pylab.grid(color = "gray")
pylab.errorbar(tc, Vc, dVc, dtc, "o", color="black")

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (tc.max()-tc.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + tc.min()
        funzione[i] = f(bucket[i], ac, tauc, cc)
pylab.plot(bucket, funzione, color = "black")

#calcolo il chi quadro
chisq = (((Vc- f(tc, ac, tauc, cc))/error)**2).sum()
ndof = len(tc) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(tc)-3)
print("Carica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)

pylab.subplot(212)
pylab.title("Scarica condensatore")
pylab.xlabel("Tempo (us)")
pylab.ylabel("Volt (Digit)")
pylab.grid(color = "gray")
pylab.errorbar(ts, Vs, dVs, dts, "o", color="black")

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (ts.max()-ts.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ts.min()
        funzione[i] = f(bucket[i], sa, taus, cs)
pylab.plot(bucket, funzione, color = "black")

#calcolo il chi quadro
chisq = (((Vs- f(ts, sa, taus, cs))/error)**2).sum()
ndof = len(ts) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(ts)-3)
print("Scarica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)

pylab.figure(2)
pylab.subplot(211)
pylab.title("Carica condensatore - Residui normalizzati")
pylab.xlabel("Tempo (us)")
pylab.ylabel("(data-fit)/data")
pylab.grid(color = "gray")
#Inserisco errore propagato sulle y
#Da origine a una divisione per 0 il primo dato della carica
pylab.errorbar(tc, (Vc-f(tc, ac, tauc, cc))/Vc, 0, dtc, "o", color="black")


pylab.subplot(212)
pylab.title("Scarica condensatore - Residui normalizzati")
pylab.xlabel("Tempo (us)")
pylab.ylabel("(data-fit)/data")
pylab.grid(color = "gray")
#Inserisco errore propagato sulle y
pylab.errorbar(ts, (Vs-f(ts, sa, taus, cs))/Vs, 0, dts, "o", color="black")

pylab.figure(3)
pylab.subplot(211)
pylab.title("Carica condensatore - Semilogarirmica")
pylab.yscale("log")
pylab.xlabel("Tempo (us)")
pylab.ylabel("(data-fit)/data")
pylab.grid(color = "gray")
#Inserisco errore propagato sulle y
pylab.errorbar(tc, Vc, dVc, dtc, "o", color="black")


pylab.subplot(212)
pylab.title("Scarica condensatore - Semilogaritmica")
pylab.yscale("log")
pylab.xlabel("Tempo (us)")
pylab.ylabel("(data-fit)/data")
pylab.grid(color = "gray")
#Inserisco errore propagato sulle y
pylab.errorbar(ts, Vs, dVs, dts, "o", color="black")



pylab.show()

#Uso tutte e due le volte per charge e discharge il modello Ae^(-t/tau)+c, tuttavia se nella discharge c rappresenta l'offset nella carica a e c dovrebbero essere totalmente correlati
#questo mi dice che dalla loro differenza posso ricavare informazioni sulla precisione del fit. Fare il chiquadro sul fatto che siano uguali.

#L'offset è chiaramnte zero quando lo zero di Arduino è impostato come zero di riferimento.
#100 pF e 10 kOhm

#Ottengo due tau leggermente diversi per la scarica e la carica. Come metto l'errore sui tempi
