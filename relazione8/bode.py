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

def linear(x, a, b):
	return a*x+b


f, df, t, dt, Va, dVa = pylab.loadtxt('/home/federico/Laboratorio3/relazione8/dati.txt', unpack = True)
VIN = ufloat(252, 2)/1000
T = unumpy.uarray(t, dt)/10**6
VA = unumpy.uarray(Va, dVa)
F = unumpy.uarray(f, df)
PHI = 2*F*T
phi = unumpy.nominal_values(PHI)
dphi = unumpy.std_devs(PHI)
Ai = VA/VIN
A = unumpy.nominal_values(Ai)
dA = unumpy.std_devs(Ai)
print(A)

INPUT = "/home/federico/Laboratorio3/relazione8/dati.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione8/datiEstesi.txt"

file = open(OUTPUT,"w")

for i in range(len(f)):
	file.write(str(f[i]))
	file.write("\t")
	file.write(str(df[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(VA)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(VA)[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(Ai)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(Ai)[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(PHI)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(PHI)[i]))
	file.write("\n")

file.close()


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


def fit_function(f, ft, Amax):
	return Amax*ft*f/((ft**2-f**2)**2+9*ft**2*f**2)**0.5

#fit un par
initial_values = (1000.0, 40.0)

pars, covm = curve_fit(fit_function, f, A, initial_values)

ft = pars[0] 
Amax = pars[1]

dft = pylab.sqrt(covm.diagonal())[0]
dAmax = pylab.sqrt(covm.diagonal())[1]


print('frequenza di taglio  = ', pars[0], '+/-', dft)
print('ampiezza_massima_alto  = ', pars[1], '+/-', dAmax)

print(covm)

#dft = 0
#dAmax = 0



#chi2
z = (A - fit_function(f, ft, Amax))/dA
s = sum(z**2)
ndof = len(f) - 3
print('Chi2 1 par = %f ' % (s))
print('ndof 1 par = %f \n' % (ndof))

dA=8.7*dA/A
A=20*pylab.log10(A)
print(A)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.xscale('log')
pylab.xlim(400, 3200)
pylab.errorbar(f, A, dA, df, linestyle='', marker = '')
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('Frequency [kHz]', size = "16")
pylab.ylabel('Gain [dB]', size = "16")
#pylab.xlim(0.05, 100)
pylab.title('Bode plot', fontsize = "18")
pylab.grid()


pylab.legend(numpoints=1, loc = 'upper right')


div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (f.max()-f.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + f.min()
        retta[i] = 20*pylab.log10(fit_function(bucket[i], pars[0], pars[1]))

pylab.plot(bucket, retta, color = 'red', label = 'fit')

pylab.savefig("bode.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)


print(covm)


logF = unumpy.log10(F)
logf =  unumpy.nominal_values(logF)
dlogf =  unumpy.std_devs(logF)


pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.errorbar(logf, phi, dphi, dlogf, linestyle='', marker = '')
#pylab.xscale("log")
#pylab.xlim(400, 3200)
pylab.legend(numpoints=1, loc = 'upper right')
pylab.xlabel('log(f/1kHz)', size = "16")
pylab.ylabel(' $\phi$ [$\pi$ rad]', size = "16")
#pylab.xlim(0,2000)
pylab.title('Sfasamento', fontsize = "18")
pylab.grid()


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = ((unumpy.std_devs(logF))**2.0+(1.0*unumpy.std_devs(PHI))**2.0)**0.5
#error = unumpy.std_devs(I_D)
init = numpy.array([-2.0, 0.0])
#Errori tutti statistici
par, cov = curve_fit(linear, unumpy.nominal_values(logF), unumpy.nominal_values(PHI), init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]

print("Fit lineare!!!!!!")
print(par, cov)


chisq = ((unumpy.nominal_values(PHI)-linear(unumpy.nominal_values(logF), a, b))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(PHI)) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (logf.max()-logf.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + logf.min() 
        retta[i] = linear(bucket[i], par[0], par[1])


pylab.plot(bucket, retta, color = "red")

pylab.savefig("sfasamento.png", dpi=None, facecolor='w', edgecolor='w',
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
