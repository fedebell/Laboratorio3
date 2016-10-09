'''
Lettura di dati dal file "INPUT", scrittura in "OUTPUT"
Legge i dati e li inserisce in una tabella Latex formattata
'''

INPUT = "/home/federico/Scaricati/tableinput.txt"
OUTPUT = "/home/federico/Scaricati/tableoutput.txt"


import pylab
import numpy

#La matrice dati contiene i valori
dati = pylab.loadtxt(INPUT,unpack=True)
dati = dati.transpose() #utlizziamo cos gli indici standard


file = open(OUTPUT,"w")

#s la stringa da ritornare
file.write("\\begin{table}[h]")
file.write("\\centering\n")
#MODIFICARE
file.write("\\begin{tabular}{|c|c|c|c|c|c|}\n\\hline\n")


row = numpy.shape(dati)[0]
col = numpy.shape(dati)[1] 


for i in range(row):
    for j in range(col):
        if j==0:
            file.write(str(dati[i][j]))
        else:
            file.write(" & " +  str(dati[i][j]))
    file.write("\\")
    file.write("\\")
    file.write("\n")

file.write("\\hline\n\\end{tabular}")
file.write("\\\caption{Inserire la caption}")#MODIFICARE
file.write("\\end{table}")

file.close()








