import pylab
import numpy
import scipy
import scipy.optimize as optimization
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.stats


# Array-stored data version 

# Normal import
f,Df,V,DV=pylab.loadtxt('/Users/damides/Desktop/dati.txt',unpack=True)

# x=pylab.log10(f)
# Dx=Df/(pylab.log(10)*f)
x=f
Dx=Df

yy=V/5.04
Dyy=pylab.sqrt( (DV/V)**2 + (0.25/5.04)**2) *yy

y=20*pylab.log10(yy)
Dy=20 *Dyy/(pylab.log(10)*yy)

# Scatter plot with error bars
plt.figure(0)
pylab.errorbar(x,y,linestyle = '', color = 'black', marker = 'o')

# Bellurie 
pylab.rc('font',size=16)
pylab.xlabel('Frequenza $f$  [Hz]') #Edit accordingly
pylab.ylabel('$A(f)$')
pylab.title('Curva di risonanza e Sfasamento') #Edit accordingly
pylab.minorticks_on()

sigma=Dy

# Fit Routine, alter only the function and init values.
def func(x, a):
    return 20*pylab.log10( (1/pylab.sqrt(1+(x/a)**2) ))
    
init = numpy.array([2100]) #Edit init values

pval, pcov = optimization.curve_fit(func, x, y, init, sigma)

error = [] #Get the error on parameters
for i in range(len(pval)):
    try:
     error.append(numpy.absolute(pcov[i][i])**0.5)
    except:
     error.append( 0.00 )

# cor_cof=numpy.array([pcov[0][1] / (pylab.sqrt(pcov[0][0] * pcov[1][1]) ), pcov[1][0] / (pylab.sqrt(pcov[0][0] * pcov[1][1]) )])  #norm_cov the old way just to be sure
# 
# normcov = numpy.zeros((len(pval), len(pval)))  #Norm_cov calculation (a manual check wouldn't be harmful...)
# for i in range(len(pval)):
#     for j in range(len(pval)):
#         normcov[i][j]= (pcov[i][j]) / (numpy.sqrt(numpy.absolute(pcov[i][i] * pcov[j][j])))

chisq = ( ((y-func(x,pval[0]))/sigma)**2).sum() #Edit number of parameter p[i]
ndof = len(x)-len(init) #edit dof
prob=1.0-scipy.stats.chi2.cdf(chisq, ndof)


print("Fit parameters =", pval)
print("Parameters errors =", error)
print('Chi2, RedChi2 ndof, p-value = %f, %f, %d,  %f' % (chisq, chisq/ndof, ndof, prob))
# print("\nCovariance matrix:\n ", pcov)
# print("\nManual correlation value (works only with 2 parameters): \n ", cor_cof)
# print("\nNormalized covariance matrix (my auto script)): \n ", normcov)
# 


# Plot printing
plt.figure(1)
gs = gridspec.GridSpec(2, 1, height_ratios=[2,1])
ax0=plt.subplot(gs[0])

pylab.title('Risultato grafico Fit')
pylab.ylabel(r'Corrente $I$ [$\mu$A]') #Y LABEL
pylab.grid(color = 'gray')
u=numpy.linspace(min(x)-min(x)*0.05,max(x)*1.05,1000)

pylab.errorbar(x, y,Dy,Dx,linestyle = '', color = 'black', marker = '.')
plt.plot(u, func(u, pval[0]))  #edit function accordingly

pylab.minorticks_on()


ax1=plt.subplot(gs[1])

pylab.xlabel('Angolo $\\theta$  [°]') #X Title
pylab.xlim(min(x),max(x)*1.1)
pylab.ylabel(r'Residui')
pylab.grid(color = 'gray')
plt.errorbar(x,(func(x,pval[0])-y)/(sigma), color='black', fmt='.') #edit
j=numpy.linspace(0, max(x)*1.1, 10000)
z=j*0
pylab.plot(j ,z, color="black")


# show the plot
pylab.show()
