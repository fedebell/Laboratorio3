'''
Lettura di dati dal file "INPUT", scrittura in "OUTPUT"
Legge i dati e li inserisce in una tabella Latex formattata
'''

INPUT = "/home/federico/Laboratorio3/relazione3/dati1.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione3/dati1formlatexstrong.txt"


import pylab
import numpy
import fpformat

#La matrice dati contiene i valori
dati = pylab.loadtxt(INPUT,unpack=True)
dati = dati.transpose() #utlizziamo cos gli indici standard

row = numpy.shape(dati)[0]
col = numpy.shape(dati)[1] 


dati_s=[] 
for i in range(row):     
    dati_s.append([])
for i in range(row):
    for j in range(col):
        dati_s[i].append("")


for i in range (0, col/2):
	for j in range(row):
		tmp = dati[j][2*i+1]
		n = 0
		while(not(1 <= tmp <= 10)): #Controllare che vada bene
			tmp = 10.0*tmp
			n = n + 1
		tmp = round(dati[j][2*i+1], n)
		n = 0
		while(not(1 <= tmp <= 10)): #Controllare che vada bene
			tmp = 10.0*tmp
			n = n + 1
		dati_s[j][2*i+1] = fpformat.fix(dati[j][2*i+1], n)
		dati_s[j][2*i] = fpformat.fix(dati[j][2*i], n)

file = open(OUTPUT,"w")

#s la stringa da ritornare
file.write("\\begin{table}[!htb]")
file.write("\\centering\n")
#MODIFICARE
file.write("\\begin{tabular}{|c|c|c|c|c|c|}\n\\hline\n")


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



