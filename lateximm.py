'''
INserimento immagine formattata
'''

OUTPUT = "/home/federico/Scaricati/immagine.txt"


import pylab
import numpy

file = open(OUTPUT,"w")


file.write("\\begin{figure}[h]\n\\centering\n\\includegraphics[scale=0.6]{NOME.ESTENSIONE}\n")
\centering
\includegraphics[scale=0.6]{part2.jpg}
file.write("\\caption{CAPTION}\n")
file.write("\\end{figure}")

file.close()


