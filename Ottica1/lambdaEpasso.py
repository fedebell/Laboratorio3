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
import numpy as np
from scipy.signal import argrelextrema

#ricavare lunghezza d'onda dal fit del cadmio

# a=1
# da=1
# b=1
# db=1
# 
# alpha = pylab.array(1)
# dalpha = 1
# 
# lamb= a/(alpha-b)
# dlamb = lamb*((da/a)+(db/b)+(dalpha/alpha)
# L = unumpy.uarray(lamb,dlamb)
# 
# print("lunghezze d'onda l=",L)



#ricavare passo reticolare

alpha0=
dalpha0=
dalpha1=
dalpha1=


thetai=(180-alpha0)*0.5
dthetai= (dalpha0/alpha0)*thetai
thetad = 180-alpha1-thetai
dthetad = dalpha1+dthetai
lhg= 546.074
dlhg=0.001

d= lhg/(pylab.sin(thetai)-pylab.sin(thetad))

dd= d*((dlhg/lhg)+(dthetai/thetai)+(dthetad/thetad))

print(d,"+-", dd)