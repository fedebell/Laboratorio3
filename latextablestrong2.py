'''
Lettura di dati dal file "INPUT", scrittura in "OUTPUT"
Legge i dati e li inserisce in una tabella Latex formattata
'''

INPUT = 'C:\\Users\\marco\\Desktop\\Laboratorio3\\relazione10\\VinIin.txt'
OUTPUT = 'C:\\Users\\marco\\Desktop\\Laboratorio3\\relazione10\\VinIintabella.txt'


import pylab
import numpy
#import fpformat

#La matrice dati contiene i valori
dati = pylab.loadtxt(INPUT,unpack=True)
dati = dati.transpose() #utilizziamo cos gli indici standard

row = numpy.shape(dati)[0]
col = numpy.shape(dati)[1] 


dati_s=[] 
for i in range(row):     
    dati_s.append([])
for i in range(row):
    for j in range(col):
        dati_s[i].append("")


for i in range (0, int(col/2)):
	for j in range(row):
		tmp = dati[j][2*i+1]
		if(tmp <= 1.0):
			n = 0
			while(not(1 <= tmp <= 10)): #Controllare che vada bene
				tmp = 10.0*tmp
				n = n + 1
			tmp = round(dati[j][2*i+1], n)
			n = 0
			while(not(1 <= tmp <= 10)): #Controllare che vada bene
				tmp = 10.0*tmp
				n = n + 1
			tmp = round(dati[j][2*i+1], n)
			#dati_s[j][2*i+1] = fpformat.fix(dati[j][2*i+1], n)
			#dati_s[j][2*i+1] = {":.*f"}.format(dati[j][2*i+1], n)
			dati_s[j][2*i+1] = "%.*f" % (n, dati[j][2*i+1])
			#dati_s[j][2*i] = fpformat.fix(dati[j][2*i], n)
			#dati_s[j][2*i] = {":.*f"}.format(dati[j][2*i], n)
			dati_s[j][2*i] = "%.*f" % (n, dati[j][2*i])
		else:
			n = 0
			while(not(1 <= tmp <= 10)): #Controllare che vada bene
				tmp = tmp/10.0
				n = n + 1

			tmp = tmp/10.0
			tmp = round(tmp, 1) #L'errore sta sempre a una cifra dopo la virgola
			tmp = tmp*pow(10.0, n+1)

			a = dati[j][2*i]/pow(10.0, n)
			a = round(a, 0)
			a = a*pow(10.0, n)

			dati[j][2*i] = a
			dati[j][2*i+1] = tmp

			#dati_s[j][2*i+1] = fpformat.fix(dati[j][2*i+1], 0)
			#dati_s[j][2*i+1] = {":.*f"}.format(dati[j][2*i+1], 0)
			dati_s[j][2*i+1] = "%.*f" % (0, dati[j][2*i+1])
			#dati_s[j][2*i] = fpformat.fix(dati[j][2*i], 0)
			#dati_s[j][2*i] = {":.*f"}.format(dati[j][2*i], 0)
			dati_s[j][2*i] = "%.*f" % (0, dati[j][2*i])
		tmp = 0.0
		a = 0.0

file = open(OUTPUT,"w")

#s la stringa da ritornare
file.write("\\begin{table}[!htb]")
file.write("\\centering\n")
#MODIFICARE

file.write("\\begin{tabular}{|")
for i in range(col):
	file.write("c|")
file.write("}\n\\hline\n")

for i in range(row):
    for j in range(col):
        if j==0:
            file.write(dati_s[i][j])
        else:
            file.write(" & " +  dati_s[i][j])
    file.write("\\")
    file.write("\\")
    file.write("\n")

file.write("\\hline\n\\end{tabular}\n")
file.write("\\caption{Inserire la caption}\n")#MODIFICARE
file.write("\\label{Inserire la label}\n")#MODIFICARE
file.write("\\end{table}\n")

file.close()



