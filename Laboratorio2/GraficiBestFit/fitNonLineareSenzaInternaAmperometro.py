import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a/(x+b)

R = numpy.array([6.94E6, 3.30E6, 0.694E6, 0.328E6, 67.6E3, 32.0E3, 6.72E3, 3.28E3, 0.670E3, 0.327E3, 67.6, 33.1])
I = numpy.array([0.72E-6, 1.5E-6, 7.10E-6, 14.75E-6, 72.8E-6, 151.1E-6, 0.729E-3, 1.468E-3, 7.15E-3, 14.08E-3, 58.6E-3, 98.5E-3])

dR = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
dI = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

r = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

flagR = numpy.array([6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
flagI = numpy.array([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])


for i in range(0, 12):
        if(flagR[i] == 6): dR[i] = 0.01*R[i] + 2.0*0.01E6 #20MOhm
        elif(flagR[i] == 5): dR[i] = 0.008*R[i] + 1000.0
        elif(flagR[i] == 4): dR[i] = 0.008*R[i] + 100.0
        elif(flagR[i] == 3): dR[i] = 0.008*R[i] + 10.0
        elif(flagR[i] == 2): dR[i] = 0.008*R[i] + 1.0
        elif(flagR[i] == 1): dR[i] = 0.008*R[i] + 3*0.1

print(R)
print(dR)

for i in range(0, 12):
        if(flagI[i] == 6): dI[i] = 0.012*I[i] + 1.0E-3 #2A
        elif(flagI[i] == 5): 
                dI[i] = 0.012*I[i] + 0.1E-3 
                r[i] = 1.0
        elif(flagI[i] == 4): 
                dI[i] = 0.008*I[i] + 0.01E-3
                r[i] = 10.0
        elif(flagI[i] == 3): 
                dI[i] = 0.008*I[i] + 0.001E-3
                r[i] = 100.0
        elif(flagI[i] == 2): 
                dI[i] = 0.008*I[i] + 0.1E-6
                r[i] = 1000.0
        elif(flagI[i] == 1): 
                dI[i] = 0.008*I[i] + 0.01E-6
                r[i] = 1.0E4
        
print(I)
print(dI)

pylab.title("Best fit numerico non lineare senza resistenza interna amperometro")
pylab.xlabel("log R (Ohm)")
pylab.ylabel("log I (mA)") #modificare gradi
pylab.grid(color = "gray")
pylab.xscale('log')
pylab.yscale('log')
pylab.xlim(0, 1.1*max(R)) 
pylab.ylim(0, 1.1*max(I))
pylab.grid(color = "gray")
pylab.errorbar(R, I, dI, dR, "o", color="black")


init = numpy.array([0.0, 0.0])
popt, pcov = curve_fit(fit_function, R, I, init, dI) 
a, b = popt
vara, varb = pylab.sqrt(pcov.diagonal())

covarab = pcov[1,0]

print(pcov)
print("Parametri del fit")
print("V0 = ", a, vara)
print("Rint = ", b, varb)

chisq = (((I - fit_function(R, a, b))/dI)**2).sum()
ndof = len(R) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (R.max()-R.min())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc + R.min()
        retta[i] = fit_function(bucket[i], a, b)

pylab.plot(bucket, retta, color = "red")

pylab.show()