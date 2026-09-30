# Parte 1 — Analisi esplorativa e inferenziale

## Obiettivo

Applicare le metodologie viste nel corso per condurre un'analisi completa del dataset
assegnato: partendo dai dati grezzi, esplorarli, pulirli, visualizzarli e infine
interrogarli con strumenti statistici.

Lo scopo è trasformare i dati in conoscenza: identificare regolarità, scoprire relazioni
fra le variabili, verificare ipotesi. L'analisi non è una sequenza di comandi, ma una
narrazione sostenuta da evidenze quantitative e grafiche. **Le domande le scrivete voi**:
l'e-mail di assegnazione descrive il dataset, non dice che cosa chiedergli.

## 1. Comprensione del dataset

- **Caricamento e prima ispezione.** Numero di righe e colonne, nomi delle colonne, tipi
  di dato riconosciuti automaticamente.
- **Dizionario dei dati.** Che cosa rappresenta ogni variabile, in quale unità di misura,
  e di che tipo è: categorica (nominale, ordinale) o numerica (discreta, continua).
- **Domande dell'analisi.** Formulate 4-5 domande sul fenomeno rappresentato nei dati, e
  scrivetele **prima** di guardare i risultati. Potrete raffinarle più avanti — il punto è
  che una domanda inventata dopo tende a essere quella a cui i dati rispondono per caso.
  Su un dataset clinico, per esempio: quali fattori si accompagnano alla diagnosi? C'è una
  relazione fra età e parametri metabolici? Il BMI si associa a un rischio maggiore?

## 2. Pulizia e preparazione

Da questa fase dipende l'affidabilità di tutto il resto.

- **Valori mancanti.** Quantificateli per colonna, scegliete una strategia e motivatela.
- **Duplicati.** Individuate ed eliminate le righe interamente duplicate.
- **Tipi e incoerenze.** Convertite ciò che è stato letto come testo e dovrebbe essere
  numero o data; uniformate le categorie scritte in modi diversi (`USA`, `U.S.A.`,
  `Stati Uniti`).
- **Valori anomali.** Individuateli (per esempio con un boxplot) e decidete: errore di
  inserimento da correggere o rimuovere, oppure valore estremo ma legittimo da tenere —
  eventualmente trasformandolo, per esempio con un logaritmo. In entrambi i casi, dite
  perché.
- **Conteggio delle righe.** Riportate quante righe avevate all'inizio e quante ne
  sopravvivono a ogni passo. Una pulizia che elimina in silenzio metà dei dati è un
  risultato dell'analisi, non un dettaglio tecnico.

## 3. Analisi esplorativa

**Una variabile alla volta.**

- Numeriche: indici di posizione (media, mediana, moda) e di dispersione (deviazione
  standard, varianza, campo di variazione, IQR); istogrammi e boxplot.
- Categoriche: tabelle di frequenza assolute e relative, e il grafico adatto a mostrarle.

**Più variabili insieme.**

- Numerica con numerica: grafico a dispersione per vedere la forma della relazione,
  e coefficienti di correlazione per quantificarla.
- Numerica con categorica: distribuzioni a confronto fra i gruppi, e gli indici di sintesi
  calcolati per gruppo.
- Categorica con categorica: tabella di contingenza, $\chi^2$ e V di Cramér; grafici a
  barre impilate o raggruppate per confrontare le proporzioni.

## 4. Inferenza

L'analisi esplorativa suggerisce («il gruppo A sembra avere una media più alta del gruppo
B»); l'inferenza stabilisce se quello che si è osservato è compatibile con il caso.

1. **Partite da un'osservazione** emersa nella fase precedente e formulate una domanda
   precisa: la differenza di prezzo fra prodotti «bio» e «standard» è reale, o è una
   fluttuazione del campione?
2. **Stimate con un intervallo**, dove ha senso, invece che con un solo numero. Una
   differenza fra medie riportata con il suo intervallo di confidenza dice molto più di
   un p-value: dice *quanto* è grande, e con quanta incertezza.
3. **Scegliete il confronto adatto** al tipo di dati, fra quelli visti a lezione:
   - una media contro un valore di riferimento → test t a un campione;
   - due gruppi indipendenti su una variabile quantitativa → test t a due campioni;
   - associazione fra due variabili categoriche → $\chi^2$ di indipendenza;
   - una distribuzione osservata contro una attesa → $\chi^2$ di adattamento;
   - due variabili quantitative → test sul coefficiente di correlazione.

   Se il vostro confronto ha **più di due gruppi**, confrontate le coppie che vi
   interessano davvero e dite quante ne avete confrontate (punto 5); nella Parte 2 i
   modelli di regressione vi permetteranno di trattare tutti i gruppi in una volta sola.
4. **Verificate le assunzioni** prima di fidarvi del risultato: la normalità con un Q-Q
   plot o un test (Shapiro-Wilk, D'Agostino), e guardate la dimensione dei gruppi. Se
   l'assunzione non regge, ditelo e trattate il risultato per quello che è.
5. **Eseguite, interpretate e concludete** nel contesto del problema, riportando
   **quanto è grande** l'effetto e non solo se è significativo: la differenza fra le medie
   nelle unità del problema con il suo intervallo, il coefficiente di correlazione, la V di
   Cramér per l'associazione fra categoriche. Con un campione grande quasi tutto risulta
   significativo — lo avete visto a lezione, lo stesso scarto che a $n=1000$ dava $p=0.11$
   a $n=5000$ dà $p=0.02$ — quindi dite che cosa è anche abbastanza grande da contare.
6. **Dichiarate quanti test avete eseguito** in tutto, compresi quelli che non avete
   riportato perché non davano niente. Se ne fate dieci a $\alpha=0.05$, uno «significativo»
   per puro caso è l'esito atteso, non una scoperta: chi legge deve poterlo sapere.

## Che cosa si consegna

Un notebook che si legge da solo: il codice di pulizia, analisi e inferenza, commentato;
i grafici leggibili, con titolo, assi etichettati con l'unità di misura e legenda dove
serve; e le celle di testo che guidano chi legge attraverso l'analisi — motivando le
scelte di pulizia, commentando che cosa si vede nei grafici e negli indici, e spiegando
come è stato impostato e come va letto ogni confronto statistico.

Si chiude tornando alle domande di partenza: a quali hanno risposto i dati, a quali no, e
che cosa servirebbe per rispondere alle altre.
