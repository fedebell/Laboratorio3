import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
from uncertainties import ufloat, unumpy

Vi, dVi, Ii, flag = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\relazione10\\VinIin.txt", unpack = True)
dIi = 0.8/100*Ii
dVi =  Vi*0.5/100 
pylab.errorbar(Vi, Ii*1000, dIi*1000, dVi, marker = '', color = 'blue', linestyle = '')
pylab.title('Corrente in ingresso alla porta NOT in funzione della ddp in ingresso')
pylab.ylabel('$I_{IN}$ ($\mu$A)', fontsize = 16)
pylab.xlabel('$V_{IN}$ (V)', fontsize = 16)
pylab.grid()
pylab.show()
