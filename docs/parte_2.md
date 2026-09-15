# Parte 2 — Spiegare, predire, rappresentare

## Obiettivo

Estendere l'analisi della Parte 1 passando dalla descrizione alla modellazione, sullo
stesso dataset e nello stesso notebook, aggiungendo nuove sezioni.

L'obiettivo qui si sdoppia:

- **spiegare**: usare modelli di regressione per quantificare le relazioni fra le
  variabili e capire il peso dei fattori in gioco — *di quanto cresce la pressione per
  ogni anno di età in più?*;
- **predire**: costruire un sistema che stimi valori o classifichi casi nuovi, con un
  valore pratico — *si può riconoscere il diabete dai soli esami del sangue, evitando
  accertamenti più invasivi?*

## 1. Spiegare

Qui contano l'interpretazione dei coefficienti e la loro incertezza, non la prestazione
predittiva.

- **Scelta delle variabili.** Partendo dall'analisi esplorativa, individuate una o più
  variabili risposta e un insieme di predittori che abbiano senso nel problema.
- **Modello.** Con `statsmodels`: regressione lineare se la risposta è quantitativa,
  logistica o multinomiale se è categorica; termini di interazione dove servono.
- **Interpretazione.** Che cosa significa ogni coefficiente nelle unità del problema, a
  parità delle altre variabili. Quali predittori sono distinguibili dal caso, e con quale
  intervallo. Quanto il modello si adatta ai dati.
- **Diagnostica.** Controllate le assunzioni: i residui contro i valori predetti, la
  collinearità fra i predittori, i valori influenti.

## 2. Ragionare sulle cause

Un coefficiente non è un effetto causale. Disegnate che cosa causa che cosa, dichiarate i
confondenti e gli effetti di selezione che vedete, e dite esplicitamente per che cosa il
vostro modello aggiusta e per che cosa no. Dove l'aggiustamento non basta, scrivetelo:
è una conclusione, non una lacuna.

## 3. Predire

**Il problema, prima del modello.** Che strumento automatico si può costruire con questi
dati? Descrivete lo scenario d'uso, perché varrebbe la pena risolverlo, e che cosa
guadagna chi lo usa. Se il dataset non ha una risposta ovvia da prevedere, la si può
costruire — per esempio discretizzando una variabile continua in classi, se interessa più
la fascia che il valore esatto.

**Il protocollo, prima dei risultati.**

- Separate i dati in addestramento e verifica, e tenete la parte di verifica fuori da ogni
  scelta fino alla fine.
- Le trasformazioni (codifica delle categoriche, standardizzazione) si stimano dentro la
  procedura di validazione, non prima: altrimenti l'informazione della parte tenuta fuori
  rientra dalla finestra.
- Riportate i punteggi come **media ± deviazione standard** fra le ripetizioni, mai come
  un numero solo.

**I modelli.** Una **baseline obbligatoria** che ignora i predittori, poi almeno due
modelli fra quelli del corso, scelti perché adatti a questi dati e non perché esistono
(niente metodi basati sulle distanze su decine di variabili, per dire). Gli iperparametri
si scelgono con una ricerca sulla parte di addestramento.

**La valutazione.** Le metriche adatte al problema — errore quadratico o assoluto in
regressione; precisione, richiamo, F1, matrice di confusione e curva ROC in
classificazione, con attenzione allo sbilanciamento delle classi. Poi il confronto
critico: quale modello vince, di quanto, e se quel «di quanto» è distinguibile dal rumore.
Chiudete guardando **gli errori**: su quali casi sbaglia il modello migliore?

## 4. Rappresentare

Tecniche non supervisionate, da applicare **solo dove aggiungono qualcosa**. Un
«non applicabile, perché…» argomentato con le evidenze vale quanto un'applicazione
riuscita; una PCA fatta perché era nel programma, no.

- **Riduzione della dimensionalità.** Proiettare su due o tre componenti per vedere i dati,
  colorando i punti con la classe: le classi si separano? Il problema di classificazione è
  geometricamente facile o difficile? Guardate i pesi delle componenti per capire quali
  variabili originali contano. Se avete incontrato instabilità o tempi lunghi, provate a
  usare le componenti come ingresso dei modelli della sezione precedente.
- **Clustering.** Cercate raggruppamenti naturali e chiedetevi se hanno senso nel dominio.
  Se il problema era di classificazione, confrontate i gruppi trovati con le classi vere:
  si sovrappongono? L'etichetta di gruppo può anche diventare una variabile in più.
- **Stima della densità.** Per vedere la forma di una distribuzione meglio di un istogramma,
  soprattutto se ha più mode, e per notare le zone a bassa densità: punti isolati che il
  boxplot non aveva segnalato, che possono essere errori o casi interessanti.

## Che cosa si consegna

Il notebook si chiude con una sintesi che tiene insieme le due parti: le relazioni
principali emerse, la prestazione del modello migliore e che cosa significherebbe usarlo
nello scenario descritto, e i limiti dell'analisi.

Poi le **slide della presentazione** (al massimo 15), che devono contenere una slide
dedicata alla domanda **«che cosa potrebbe spiegare diversamente questo risultato?»**.

Non è obbligatorio applicare tutte le tecniche elencate: si applicano quelle che hanno
senso per i propri dati e per il problema formulato. Le celle di testo contano quanto il
codice: spiegate perché avete scelto così.
