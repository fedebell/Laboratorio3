# Questo script serve per interfacciarsi con Arduino nell'esperienza
# di carica e scarica del condensatore

# L'interfacciamento avviene attraverso:
# 1. scrittura di un carattere (byte) che esprime l'intervallo di campionamento
# 2. lettura dei dati disponibili su porta seriale

import serial # libreria per gestione porta seriale (USB)
import time # libreria per temporizzazione

Directory='/home/federico/Documenti/Laboratorio2/ScaricaCaricaCondensatore-5/'   # nome directory dati
                                                    # << DA CAMBIARE SECONDO NECESSITA'
FileName='datiProva91115'  # parte comune nome file << DA CAMBIARE SECONDO NECESSITA'
FileNameC=(Directory+FileName+'_C.txt') # crea nome file dati carica
FileNameS=(Directory+FileName+'_S.txt') # crea nome file dati scarica

ard=serial.Serial('/dev/ttyACM0',9600)  # apre porta seriale (occhio alla sintassi, dipende
                                # dal sistema operativo!)
time.sleep(2)   # aspetta due secondi per evitare casini

ard.write(b'2') # scrive il carattere per l'intervallo di campionamento
                # in unita' di 100 us << DA CAMBIARE A SECONDA DEI GUSTI
                # l'istruzione b indica che e' un byte (carattere ASCII)

time.sleep(2) # aspetta due secondi per evitare casini

outputFileC = open(FileNameC, "w" ) # apre file dati carica per scrittura
outputFileS = open(FileNameS, "w" ) # apre file dati scarica per scrittura

# loop lettura dati da seriale (500, di cui 250 per carica e 250 per scarica)
for i in range (0,500):
    data = ard.readline().decode() # legge il dato e lo decodifica
    if data:
        if i<250:
            outputFileC.write(data) # scrive i primi 200 in file di carica
        else:
            outputFileS.write(data) # scrive i secondi 200 in file di scarica
            
outputFileC.close() # chiude il file dei dati di carica
outputFileS.close() # chiude il file dei dati di scarica
ard.close() # chiude la comunicazione seriale con Arduino

print('end') # scrive sulla console che ha finito
