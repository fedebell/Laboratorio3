/*
Programma per l'acquisizione  digitale di d.d.p. inviate 
all'ingresso A0 di Arduino. Vengono acquisiti 600 punti a intervalli temporali
quasi-costanti, determinati dalla variabile delay_ms. I valori digitalizzati sono 
accumulati nell'array di interi V1. Inoltre si pone un'uscita digitale
a livello alto per scopi di "calibrazione".
NOTA: IN QUESTO SCRIPT V_ref = 1.1 V (nominali)
*/

//Dichiarazione variabili
const int analogPin_uno=0;  // Decide di usare pin A0 per lettura V1
const int digitalPin_uno=7; // Decide di usare pin 7 per uscita digitale
int i=0;  // Definisce la variabile intera che viene incrementata nel loop
int V1[600];  // Definisce l'array di interi per memorizzare V1 (d.d.p. letta da analogPin_uno) 
int delay_ms;  // Definisce la variabile intera che contiene il ritardo tra due step successivi (in unita' di 10 ms)
int start=0;  // Crea il flag di controllo (che diventa uno alla fine del processo) 
int trash; // Crea la variabile intera che conterra' la prima lettura (da buttare)

//Inizializzazione
void setup()
{
  pinMode(digitalPin_uno,OUTPUT); // Configura il pin digital_Pin_uno come output digitale
  digitalWrite(digitalPin_uno,HIGH); // E lo pone "alto"
  analogReference(INTERNAL); // Sceglie il riferimento V_ref = 1.1 V (nominali)
  Serial.begin(9600);  // Inizializzazione della porta seriale
  Serial.flush(); // Svuota il buffer della porta seriale 
}

//Ciclo di istruzioni del programma
void loop()
{
    if (Serial.available() >0) // Controlla se il buffer seriale ha qualcosa
      {
        delay_ms = (Serial.read()-'0')*10; // Legge il byte e lo interpreta come ritardo (unita' 10 ms)
        Serial.flush(); // Svuota il buffer della seriale
	start=1; // Pone il flag start a uno in modo da avviare l'acquisizione
      } 
  if(!start) return // Quando il flag è zero termina l'acquisizione
    delay(500); // Attende 500ms per evitare problemi
    trash=analogRead(analogPin_uno); // Fa una prima lettura (che non verra' considerata) per evitare spikes
    delay(delay_ms); // Aspetta il tempo impostato
    for(i=0;i<600;i++)  // Avvia il loop di acquisizione  
      {
       V1[i]=analogRead(analogPin_uno);   // Legge il pin analogPin_uno
       delay(delay_ms);   // Aspetta il tempo impostato
      }
     for(i=0;i<600;i++)  // Nuovo ciclo che scorre l'array di dati e lo scrive sulla seriale 
     {
       Serial.println(V1[i]);  // Scrive il dato sulla seriale e va a capo
     }
    start=0; // Annulla il flag in modo da uscire dall'acquisizione
    Serial.flush(); // Svuota il buffer della porta seriale
  }



