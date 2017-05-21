import numpy
import pylab
from scipy.optimize import curve_fit
vout, dvout, f1, f, df1, df = pylab.loadtxt('/home/federico/Laboratorio3/relazione15/datiBode1.txt', unpack = True)
vin=0.0071
dvin=0.0001

A = vout/vin
#df = pylab.sqrt(df**2 + (f*20./10**6)**2)
#dvin = pylab.sqrt(dvin**2 + (vin*3./100)**2)
#dvout = pylab.sqrt(dvout**2 + (vout*3./100)**2)
dA = (dvin/vin + dvout/vout)*A

#fit un par
initial_values = ( 16.0, 770.0)
def fit_function(f, ft, a):
    return a/(1 + (f/ft)**2)**0.5
#TODO Viene tutto meglio se non metto gli errori
pars,covm = curve_fit(fit_function, f, A, initial_values)
ft, a = pars
dft = pylab.sqrt(covm.diagonal())[0]
da = pylab.sqrt(covm.diagonal())[1]

print("Matrice di covarianza")
print(covm)
print('ft 2 par = ', pars[0], pars[1], '+/-', dft, da)
#chi2
z = (A - fit_function(f, ft, a))/dA
s = sum(z**2)
ndof = len(f) - 2
print('Chi2 2 par = %f ' % (s))
print('ndof 2 par = %f \n' % (ndof))
#plot fit nuemerico
print(dA)

dA=8.7*dA/A
A=20*pylab.log10(A)
print(dA)

pylab.figure(1)
pylab.xscale('log')
pylab.errorbar(f, A, dA, df, linestyle='', marker = '.')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequency [kHz]')
pylab.ylabel('Gain [dB]')
#pylab.xlim(80,1500000)
pylab.title('Bode plot passa basso')
pylab.grid()

#FIXME rendere piu smooth questa cosa usando il mio metodo della suddivisione per tracciare i punti.

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (f.max()-f.min())/div
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + f.min()
        retta[i] = 20*pylab.log10(fit_function(bucket[i], ft, a))

pylab.plot(bucket, retta, color = "red")

pylab.show()



