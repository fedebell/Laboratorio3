/* 
Questo sketch serve per realizzare un processo di carica e scarica
di un condensatore C attraverso una resistenza R. La tensione di carica 
viene fornita dal pin (porta digitale) 7; la tensione viene campionata sull'ingresso
analogico A0; il campionamento avviene su 250 punti nella fase di carica
e 250 punti in quella di scarica; l'intervallo temporale di campionamento
nominale è aggiustabile in unità di 100 us
*/

// Blocco dichiarazioni
const int analogPin_uno=0; // Definisice la porta A0 usata per la lettura
const int digitalPin_uno=7; // Definisce la porta 7 usata per la carica
int i; // Definisice la variabile intera i (contatore)
int delays; // Definisce la variabile intera delays
int V1[250]; // Definisce l'array intero V1
long t[250]; // Definisice l'array t come intero long
long StartTime; // Definisce il valore StartTime come intero long 
int start=0; // Definisce il valore start (usato come flag)
int trash; // Definisce la variabile di trash (prima lettura, da cestinare)

// Istruzioni di inizializzazione
void setup()
  {
   Serial.begin(9600); // Inizializza la porta seriale a 9600 baud
   Serial.flush(); // Pulisce il buffer della porta seriale 
   pinMode(digitalPin_uno,OUTPUT); // Definisce digitalPin_uno come output
   digitalWrite(digitalPin_uno,LOW); // e lo pone a valore low
   bitClear(ADCSRA,ADPS0); // Istruzioni necessarie per velocizzare
   bitClear(ADCSRA,ADPS2); // il rate di acquisizione analogica
  }

// Istruzioni del programma
void loop()
  {
    if (Serial.available() >0) // Controlla se il buffer seriale ha qualcosa
      {
        delays = (Serial.read()-'0')*100; // Legge il byte e lo interpreta come ritardo in us
        Serial.flush(); // Svuota la seriale
	start=1; // Pone il flag start a uno
      }
 
  if(!start) return // Se il flag è start=0 non esegue le operazioni qui di seguito
                    // altrimenti le fa partire (quindi aspetta di ricevere l'istruzione
                    // di partenza)
    delay(2000); // Aspetta 2000 ms per permettere di partire con condensatore scarico
    digitalWrite(digitalPin_uno,HIGH); // Pone digitalPin_uno a livello alto per la carica
    StartTime=micros(); // Misura il tempo iniziale con l'orologio interno (lettura in us)
    trash = analogRead(analogPin_uno); // Mette la prima lettura, da cestinare, in trash
    for(i=0;i<250;i++) // Loop per la carica 
      {
          t[i]=micros()-StartTime; // Legge il timestamp in us, sottrae lo StartTime e mette il risultato in array t
          V1[i]=analogRead(analogPin_uno); // Legge analogPin e lo mette in array V1
          delayMicroseconds(delays); // Aspetta tot us 
      }
  
    for(i=0;i<250;i++) // Loop per la scrittura su porta seriale dei 250 dati della carica
      {
        Serial.print(t[i]); // Scrive t[i]
        Serial.print(" "); // Mette uno spazio
        Serial.println(V1[i]); // Scrive V1[i] e va a capo
      }
  
   delay(1000); // Aspetta 1000 ms per completare la carica
   digitalWrite(digitalPin_uno,LOW); // Pone chargePin a livello basso per la scarica
   StartTime=micros(); // Misura il tempo iniziale con l'orologio interno (lettura in us)
    trash = analogRead(analogPin_uno); // Mette la prima lettura, da cestinare, in trash
    for(i=0;i<250;i++) // Loop per la carica 
      {
          t[i]=micros()-StartTime; // Legge il timestamp in us, sottrae lo StartTime e mette il risultato in array t
          V1[i]=analogRead(analogPin_uno); // Legge analogPin e lo mette in array V1
          delayMicroseconds(delays); // Aspetta tot us 
      }
  
    for(i=0;i<250;i++) // Loop per la scrittura su porta seriale dei 250 dati della carica
      {
        Serial.print(t[i]); // Scrive t[i]
        Serial.print(" "); // Mette uno spazio
        Serial.println(V1[i]); // Scrive V1[i] e va a capo
      }
  start=0; // Annulla il flag
    Serial.flush(); // Pulsice il buffer della porta seriale (si sa mai)
}
