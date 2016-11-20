import numpy
import pylab
from scipy.optimize import curve_fit
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

f, df, vout, dvout, t, dt = pylab.loadtxt('/home/federico/Laboratorio3/relazione6/datiDerivatore.txt', unpack = True)
t = t/1000000
dt=dt/1000000
vin=0.448
dvin=0.004
pylab.figure(1)
A = vout/vin
#dvin = pylab.sqrt(dvin**2 + (vin*3.0/100)**2)
#dvout = pylab.sqrt(dvout**2 + (vout*3.0/100)**2)
dvin = pylab.sqrt(dvin**2)
dvout = pylab.sqrt(dvout**2)
dA = (dvin/vin + dvout/vout)*A
#Federico
T = unumpy.uarray(t, dt)
F = unumpy.uarray(f, df)
PHI = 2*F*T
#IMPORTANTE:Questo e' solo un aggiustamento
PHI = 1-PHI
phi = unumpy.nominal_values(PHI)
dphi = unumpy.std_devs(PHI)
#per come abbiamo preso le misure facciamo vedere che il circuito 
print(PHI)

''''
#fit due pars
initial_values = ( 1.,1. )
def fit_function(f, a, ft):
    return a/((1 + (f/ft)**2)**0.5)
pars,covm = curve_fit(fit_function, f, A, initial_values)
a, ft = pars
da, dft = pylab.sqrt(covm.diagonal())

print('a 2 pars = ', pars[0], '+/-', numpy.sqrt(covm[0,0]))
print('ft 2 pars = ', pars[1], '+/-', numpy.sqrt(covm[1,1]))
print('norm cov 2 pars= ', covm[0,1]/(numpy.sqrt(covm[0,0]*covm[1,1])))
#plot fit nuemerico
pylab.xscale('log')
pylab.yscale('log')
pylab.xlim(10**1.5, 10**4.5)
pylab.errorbar(f, A, dA, df, linestyle='', marker = '', label = 'data')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequenza [Hz]')
pylab.ylabel('Attenuazione')
pylab.title('Fit due parametri')
pylab.grid()
pylab.plot(f, fit_function(f, a, ft), color = 'green', label = 'fit')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.show()
#residui normalizzati
r = (A - fit_function(f, a, ft))/dA
pylab.subplot(2,1,2)
pylab.xlim(10**1.5, 10**4.5)
pylab.xscale('log')
#pylab.yscale('log')
pylab.plot(f,r,color='blue',linestyle ='--', marker='o')
pylab.xlabel('Frequenza [Hz]')
pylab.title('Residui normalizzati')
pylab.grid()
#chi2
z = (A - fit_function(f, a, ft))/dA
s = sum(z**2)
ndof = len(f) - len(initial_values)
print('Chi2 2 pars = %f ' % (s))
print('ndof 2 pars = %f \n' % (ndof))
'''
#tutto con 1 par

#fit un par
initial_values = (1.0, 1.0)
def fit_function(f, ft, Amax):
    return Amax/((1 + (ft/f)**2)**0.5)
pars,covm = curve_fit(fit_function, f, A, initial_values)
ft = pars[0]
Amax = pars[1]
dft = pylab.sqrt(covm.diagonal())[0]
dAmax = pylab.sqrt(covm.diagonal())[1] 

print('frequenza di taglio  = ', pars[0], '+/-', dft)
print('ampiezza_massima  = ', pars[1], '+/-', dAmax)
#chi2
z = (A - fit_function(f, ft, Amax))/dA
s = sum(z**2)
ndof = len(f) - 2
print('Chi2 1 par = %f ' % (s))
print('ndof 1 par = %f \n' % (ndof))

dA=8.7*dA/A
A=20*pylab.log10(A)
print(A)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.xscale('log')
pylab.errorbar(f, A, dA, df, linestyle='', marker = '')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequency [kHz]', size = "16")
pylab.ylabel('Gain [dB]', size = "16")
#pylab.xlim(0.05, 100)
pylab.title('Bode plot per circuito derivatore.', fontsize = "18")
pylab.grid()


#pylab.plot(f, 20*pylab.log10(fit_function(f, ft, Amax)), color = 'green', label = 'fit')
#pylab.legend(numpoints=1, loc = 'upper right')

pars[0]=3.425154700154
pars[1]=11.5976908540
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (f.max()-f.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + f.min()
        retta[i] = 20*pylab.log10(fit_function(bucket[i], pars[0], pars[1]))


pylab.plot(bucket, retta, color = "red")

pylab.savefig("bodeDerivatore.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)


print(covm)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.xscale('log')
pylab.errorbar(f, phi, dphi, df, linestyle='', marker = '')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequency [kHz]', size = "16")
pylab.ylabel(' $\phi$ [$\pi$ rad]', size = "16")
#pylab.xlim(0,2000)
pylab.title('Sfasamento dell\'uscita del circuito derivatore.', fontsize = "18")
pylab.grid()

pylab.savefig("derivatoreSfasamento.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()

'''
#deltaphi
phi = 2*f*t/1000
dphi = (df/f + dt/t)*phi
#bode
A1=20*pylab.log10(A)+0.0000001
pylab.figure(3)
pylab.xscale('log')
dA1=20*dA/(A*pylab.log(10))
#dA1[0]=0.
pylab.errorbar(f,A1,dA1,df, label = 'data')
pylab.legend(numpoints=1, loc = 'upper right')
#bodeplot: scegliere i punti con cura ( magari fino al corner )
A1 = numpy.array([-5.54476640, -9.22774443,  -11.9396092,  -15.2125380,-16.5351316,  -22.1581078,  -25.4167041,-31.4373040])
f1=f
dA1 = numpy.array([dA1[8],dA1[9],dA1[10],dA1[11],dA1[12],dA1[13],dA1[14],dA1[15]])
f = numpy.array([f[8],f[9],f[10],f[11],f[12],f[13],f[14],f[15]])
df = numpy.array([df[8],df[9],df[10],df[11],df[12],df[13],df[14],df[15]])
#fit
#fit due pars
initial_values = ( 1. )
def fit_function(f, a):
    return a -20*pylab.log10(f)
pars,covm = curve_fit(fit_function, f, A1, initial_values)
a= pars
da = pylab.sqrt(covm.diagonal())

print('a bode = ', pars[0], '+/-', numpy.sqrt(covm[0]))
#plot fit nuemerico

pylab.xscale('log')
#pylab.xlim(10**1.5, 10**4.5)
#pylab.errorbar(f, A1, dA1, df, linestyle='', marker = '')
pylab.xlabel('Frequenza [Hz]')
pylab.ylabel('Attenuazione [dB]')
pylab.title('passabasso Bode')
pylab.grid()
x=pylab.linspace(10**(2.5),10**4.3,100)
pylab.plot(x, fit_function(x, a), color = 'green', label ='fit')
pylab.legend(numpoints=1, loc = 'upper right')
y=pylab.zeros(len(f1))
pylab.plot(f1,y,linestyle='--')
pylab.show()
ft = 10**(a/20)
dft = da*(a/20.)*10**((a/20)-1) 
print(ft, dft)
#chi2
z = (A1 - fit_function(f, a))/dA1
s = sum(z**2)
ndof = len(f) - 1
print('Chi2 bode = %f ' % (s))
print('ndof bode = %f ' % (ndof))
'''
