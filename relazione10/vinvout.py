import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
from uncertainties import ufloat, unumpy

Vi, Vo = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\relazione10\\VinVout.txt", unpack = True)

dVi =  Vi*0.5/100
dVo = Vo*0.5/100
pylab.errorbar(Vi, Vo, dVo, dVi, marker = '', color = 'blue', linestyle = '')
pylab.title('ddp in uscita vs ddp in ingresso della porta not')
pylab.ylabel('$V_{OUT}$ (V)', fontsize = 16)
pylab.xlabel('$V_{IN}$ (V)', fontsize = 16)
pylab.grid()
pylab.show()
