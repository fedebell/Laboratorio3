# Laboratorio3


## Git

Git è un *version control system*, cioè man mano che lavori su dei file lui salva delle istantanee. È utile per poter tornare indietro in caso di pocci e per lavorare in modo condiviso sui file: le uniche modifiche che si possono condividere sono quelle già catturate in un'istantanea.

Fare un *commit* significa fare una di queste istantanee. Si suppone che gli utenti facciano il commit solo quando lo stato delle loro modifiche è 'consistente' (es. il codice LaTeX compila senza errori).

L'insieme delle istantanee è la *repository*. Per lavorare in condivisione, la 'versione ufficiale' della repository viene tenuta su un server (in questo caso GitHub). Ogni utente copia (*clona*) tutta la repository sul suo computer per poterci lavorare.

### Usare git

Il ciclo tipico di utilizzo è:

1. Aggiornare la repository locale (*pullare*).
2. Modificare i file.
3. Fare il commit.
4. Pullare, per gestire eventuali conflitti (se qualcun altro ha modificato gli stessi file).
5. Eventualmente fare un commit dopo la risoluzione dei conflitti (**importante**).
6. Aggiornare la repository remota (*pushare*).

Per eseguire questi passaggi, si può usare un programma a interfaccia grafica (**consigliato**) oppure direttamente `git` da terminale.

I programmi GUI che consiglio:

* [GitHub desktop](https://desktop.github.com) il programma ufficiale di GitHub. Molto semplice da usare.
* [SourceTree](https://www.sourcetreeapp.com) comunque semplice da usare ma con più funzionalità. Anche lui supporta direttamente gli account GitHub.

Altri programmi (anche per Linux) si trovano [sul sito di git](https://git-scm.com/download/gui/linux).

Elenchiamo ora gli specifici comandi di `git`. Dovrebbe essere facile trovare i comandi corrispondenti nei programmi a interfaccia grafica.

#### Creare la copia locale

Per iniziare a lavorare sulla repository bisogna clonarla. Spostarsi nella cartella dove si vuole tenere la repository ed eseguire il comando:

`git clone https://github.com/fedebell/Laboratorio3.git`

Questo crea una cartella `Laboratorio3` nella cartella corrente. Prima di eseguire gli altri comandi, **spostarsi nella cartella `Laboratorio3`**.

#### Pullare e pushare

Per aggiornare la copia **locale**:

`git pull`

Per aggiornare la copia **remota** da quella locale:

`git push`

#### Commit

Per fare un commit, il comando è

`git commit`

Tuttavia c'è qualche dettaglio in più da sapere. Se abbiamo creato nuovi file, git non ne tiene traccia se non glielo diciamo esplicitamente con il comando:

`git add file.estensione`

Se abbiamo aggiunto molti file ci conviene metterli in una cartella e scrivere:

`git add nomecartella`

Ovviamente c'è anche il comando per rimuovere file:

`git rm file.estensione`

Se volete cambiare nome a un file, anziché [rimuoverlo, rinominarlo, riaggiungerlo] si può usare:

`git mv file.estensione nuovonome.estensione`

Prima di fare il commit, per sapere quali file sono stati modificati rispetto al commit precedente e se ci sono file aggiunti o rimossi, usare:

`git status`

Per vedere gli ultimi commit:

`git log`

##### Messaggio di commit

`git` vi imporrà di scrivere un messaggio di commit. Il messaggio di commit tipico ha questa struttura:

* Una riga corta (≲ 50 caratteri) che riassume le modifiche.
* Eventualmente tutti i commenti che vi passano per la testa (*dopo* la riga corta).

Quando usate semplicemente `git commit` di solito venite infognati in un editor da terminale. In pratica la cosa più comoda da fare è:

`git commit -a -F -`

Dove `-a` aggiunge in automatico i nuovi file e `-F -` vi fa digitare il messaggio di commit direttamente come da riga di comando (non potete cancellare dopo essere andati a capo, e per terminare il messaggio dovete usare `Ctrl+D`).

Per sapere quali file vanno aggiunti da `-a` e quali non interessano, `git` legge il file `.gitignore`. Dopo averci dato un occhiata, è abbastanza intuitivo come usarlo.

Scritto da Giacomo Petrillo
