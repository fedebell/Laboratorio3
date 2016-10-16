import numpy
import pylab
from scipy.optimize import curve_fit
vout, dvout, f, df = pylab.loadtxt('/home/federico/Laboratorio3/relazione2/datiPassaBasso.txt', unpack = True)
vin=5
dvin=0.15
pylab.figure(1)
pylab.subplot(2,1,1)
A = vout/vin
df = pylab.sqrt(df**2 + (f*20./10**6)**2)
dvin = pylab.sqrt(dvin**2 + (vin*3./100)**2)
dvout = pylab.sqrt(dvout**2 + (vout*3./100)**2)
dA = (dvin/vin + dvout/vout)*A
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
initial_values = ( 1. )
def fit_function(f, ft):
    return 1./((1 + (f/ft)**2)**0.5)
pars,covm = curve_fit(fit_function, f, A, initial_values)
ft = pars
dft = pylab.sqrt(covm.diagonal())

print('ft 1 par = ', pars[0], '+/-', numpy.sqrt(covm[0]))
#chi2
z = (A - fit_function(f, ft))/dA
s = sum(z**2)
ndof = len(f) - 1
print('Chi2 1 par = %f ' % (s))
print('ndof 1 par = %f \n' % (ndof))
#plot fit nuemerico
print(dA)

dA=8.7*dA/A
A=20*pylab.log10(A)
print(dA)

pylab.figure(1)
pylab.xscale('log')
pylab.errorbar(f, A, dA, df, linestyle='', marker = '', label = 'data' )
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Gain [dB]')
pylab.xlim(80,1500000)
pylab.title('one-parameter fit')
pylab.grid()
pylab.plot(f, 20*pylab.log10(fit_function(f, ft)), color = 'green', label = 'fit')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.show()
#residui normalizzati
r = (A - 20*pylab.log10(fit_function(f, ft)))/dA
pylab.figure(2)
pylab.xscale('log')
pylab.xlim(80,1500000)
#pylab.yscale('log')
pylab.plot(f,r,color='blue',linestyle ='--', marker='o')
pylab.xlabel(' Frequency[Hz]')
pylab.title('Normalized residuals')
pylab.grid()
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
