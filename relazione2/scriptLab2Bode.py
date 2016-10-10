from lab import *
from pylab import *

#Misuro a mano con il tester i valori che poi vado a mettere nel file, posso anche lasciare lo sfasamento vuoto

f, Vin, Vout, phi = loadtxt('data.txt', unpack=True)

A = Vout / Vin
dB = 20 * log10(A)

fun_A = lambda f, fT: sqrt(1 / (1 + f/fT))
fun_phi = lambda f, fT: arctan(f/fT)

par, cov = curve_fit_patched(fun_A, f, A, p0=(365.0))

fT = par[0]
dfT = sqrt(cov[0,0])

par, cov = curve_fit_patched(fun_phi, f, phi, p0=(365.0))

fTp = par[0]
dfTp = sqrt(cov[0,0])

#Ricordarsi che il grafico di Bode è logaritmico su entrambi gli assi

title('Bode diagram of low-pass RC filter')
subplot(211)
xlabel('frequency [Hz]')
ylabel('gain [dB]')
xscale('log')
plot(f, dB)
subplot(212)
xlabel('frequency [Hz]')
ylabel('phase [pi rad]')
xscale('log')
plot(f, -phi)
savefig('plot.png')

print("\ncut frequency: %s Hz" % util_format(fT, dfT))
print("\ncut frequency (from phase): %s Hz\n" % util_format(fTp, dfTp))

show()

