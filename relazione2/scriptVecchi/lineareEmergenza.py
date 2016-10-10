import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

V = numpy.array([ 2.         ,2.30103    , 2.47712125,  2.69897   ,  3.00302947 , 3.17695898,
  3.30103    , 3.47712125 , 3.60205999 , 3.69897  ,   3.90308999  ,4.00603795,
  5.0    ,     6.0        ])

I = numpy.array([  0.25674449  , 0.34066679  , 0.34066679  ,-0.06976656 , -0.72424345,
  -1.68145577,   -3.19787811,   -5.3521248  ,  -7.21027021 ,  -9.11863911, 
 -12.91783122 , -14.70364354 , -33.97940009,  -47.95880017]
)

dV = numpy.array([ 0.00434294 , 0.00434294 , 0.00434294 , 0.00434294  ,0.00434294 , 0.00434294,
  0.00434294  ,0.00434294  ,0.00434294 , 0.00434294,  0.00434294  ,0.00434294,
  0.00434294  ,0.00434294])
dI = numpy.array([  0.36377407  , 0.37387187   ,0.37387187 ,  0.37060107,   0.37179407,
   0.42693458 ,  0.43822515   ,0.49354726 ,  0.54540382 ,  0.435     ,   0.46509346,
   0.54007917  , 3.48977377  ,17.40195739])


pylab.title("Best fit numerico, errore extra")
pylab.xlabel("Delta V (V)")
pylab.ylabel("I (mA)") #modificare gradi
pylab.rc('font',size=16)
pylab.grid(color = "gray")
pylab.xlim(0, 1.1*max(V)) 
pylab.ylim(0, 1.1*max(I))
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, "o", color="black")


init = numpy.array([0.0, 0.0])
popt, pcov = curve_fit(fit_function, V, I, init, dI) 
a, b = popt
vara, varb = pylab.sqrt(pcov.diagonal())

covarab = pcov[0,1]

print(covarab)
print("Parametri del fit")
print("R = ", 1/a, "dR = ", vara/(a*a))
print("I_0", b, "dI_0", varb)

#Cambio errore per ogni file dove aver fatto il calcolo su fitNumerico.py
chisq = (((I - fit_function(V, a, b))/(dI+(1/0.469758796618)*dV))**2).sum() 
ndof = len(V) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof 2 = %f/%d" % (chisq, ndof))
print("p = ", p)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (V.max())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = fit_function(bucket[i], a, b)

pylab.plot(bucket, retta, color = "red")

#Calcolo di un valore di I e della sua incertezza
Vingresso = 2
Iteorico = a + b*Vingresso
dIteorico = (vara**2 + (Vingresso * varb)**2 + 2*(Vingresso)*covarab)**0.5

print("I' = ", Iteorico)

#Rifaccio il fit considerando anche l'errore sulla V


pylab.show()
