import numpy
import pylab
from scipy.optimize import curve_fit
vout, dvout, f1, f, df1, df = pylab.loadtxt('/home/federico/Laboratorio3/relazione15/datiBode2Ridotti.txt', unpack = True)
vin=0.0286
dvin=0.0001

def fit_function(f, A0, omega0, tau):
	return A0*(tau)*pylab.sqrt((f**2/((f**2-omega0**2)**2+f**2*tau**2)))

A = vout/vin
#df = pylab.sqrt(df**2 + (f*20./10**6)**2)
#dvin = pylab.sqrt(dvin**2 + (vin*3./100)**2)
#dvout = pylab.sqrt(dvout**2 + (vout*3./100)**2)
dA = (dvin/vin + dvout/vout)*A


#fit un par
initial_values = (150, 6.34, 1.56)
pars, covm = curve_fit(fit_function, f, A, initial_values, dA)
A0, omega0, tau = pars
dA0 = pylab.sqrt(covm.diagonal())[0]
domega0 = pylab.sqrt(covm.diagonal())[1]
dtau = pylab.sqrt(covm.diagonal())[2]

print("Matrice di covarianza")
print(covm)

#TODO attenzione nonostante il nome tau e una frequenza angolare 
print(A0, dA0)
print(omega0, domega0)
print((tau), (dtau))
#chi2
z = (A - fit_function(f, A0, omega0, tau))/dA
s = sum(z**2)
ndof = len(f) - 3
print('Chi2 3 par = %f ' % (s))
print('ndof 3 par = %f \n' % (ndof))
#plot fit nuemerico
print(dA)

dA=8.7*dA/A
A=20*pylab.log10(A)
print(dA)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (f.max()-f.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + f.min()
        retta[i] = 20*pylab.log10(fit_function(bucket[i], pars[0], pars[1], pars[2]))

pylab.plot(bucket, retta, color = "red")

pylab.xscale('log')
pylab.errorbar(f, A, dA, df, linestyle='', marker = '.')
pylab.xlabel('Frequency [kHz]')
pylab.ylabel('Gain [dB]')
pylab.title("Bode Plot filtro passa banda - Dati ridotti")
#pylab.xlim(80,1500000)
pylab.grid()
pylab.show()


