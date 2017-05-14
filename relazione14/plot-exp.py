import pylab
import numpy
from scipy.optimize import curve_fit
import matplotlib
import math

n, V, dV = pylab.loadtxt('C:\\Users\\Lisa\\Desktop\\Lab3\\Lock-In\\dati2marco.txt', unpack=True)

y=V
dy=dV

pylab.figure(1)

pylab.rc('font',size=13)

pylab.title('Assorbimento', fontsize = "16")

pylab.xlabel('numero lastrine', size = "14")

pylab.ylabel('$V_{out}$ [$V$]', size = "14")

pylab.xlim(-0.5,7.5)
pylab.grid(color = "gray")
pylab.plot(n,y, '.', label='data', color = 'black')
pylab.errorbar(n, y, dy, linestyle='', marker='+', color = 'black')


def exponential(x, v0, n0):
        return v0*pylab.exp(-x/n0)
#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
n0 = 1
v0 = 1
#Contollare unit di misura
error = pylab.sqrt(dy**2)
init = numpy.array([n0, v0])
par, cov = curve_fit(exponential, n, y, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

n0 = par[0]
v0 = par[1]

chisq = (((y-exponential(n, v0, n0))/error)**2)
print('le differenze sono', chisq)
somma = sum(chisq)
ndof = len(n) - 2 #Tolgo due parametri estratti dal fit
#p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
#print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (n.max()-n.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + n.min()
        retta[i] = exponential(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "black")


dn0=cov[0][0]**0.5
dv0=cov[1][1]**0.5

print("Si ricavano n0 = ",(-1)*n0  ,"+-" ,dn0, "e di v0 =",  v0, "+-", dv0)



pylab.show()