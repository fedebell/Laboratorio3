import pylab
import numpy
from scipy.optimize import curve_fit
import matplotlib
import math

n, V, dV = pylab.loadtxt('C:\\Users\\Lisa\\Desktop\\Lab3\\Lock-In\\dati2marco.txt', unpack=True)

V= -1*V
y=pylab.log(V)
dy=dV/V

pylab.figure(1)

pylab.rc('font',size=13)

pylab.title('Assorbimento', fontsize = "16")

pylab.xlabel('numero lastrine', size = "14")

pylab.ylabel('$V_{out}$ [$V$]', size = "14")

pylab.xlim(-0.5,7.5)
pylab.grid(color = "gray")
pylab.plot(n,y, '.', label='data', color = 'black')
pylab.errorbar(n, y, dy, linestyle='', marker='+', color = 'black')

def linear(x,a,b):
    return a*x+b
    
#a=-1/n_o
#b=lnV_o
    
#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = -0.2
b = 0.4
#Contollare unit di misura
error = pylab.sqrt(dy**2)
init = numpy.array([a, b])
par, cov = curve_fit(linear, n, y, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

a = par[0]
b = par[1]
chisq = (((y-linear(n, a, b))/error)**2)
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
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "black")


da=cov[0][0]**0.5
db=cov[1][1]**0.5

print("Si ricavano a = ", a ,"+-" ,da, "e di b =",  b, "+-", db)



pylab.show()