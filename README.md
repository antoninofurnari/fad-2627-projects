# Progetto — Fondamenti di Analisi dei Dati 2026/27

Template per il progetto del corso. Si lavora su un dataset assegnato per gruppo, in due
parti, e si presenta il lavoro all'esame.

**Gruppo:**
 - Nome e Cognome
 - Nome e Cognome
 - Nome e Cognome

**Dataset assegnato:** (nome)

## Le due parti

| | Cosa si fa | Quando |
|:--|:--|:--|
| **[Parte 1](docs/parte_1.md)** | analisi esplorativa e inferenziale | rivista in aula il giorno della prima prova in itinere |
| **[Parte 2](docs/parte_2.md)** | modellare: spiegare, predire, rappresentare | ripresa in aula prima della pausa di Natale |

**La consegna è una sola, a fine gennaio**: un notebook con tutte e due le parti. La
revisione di novembre serve a correggere la rotta finché c'è tempo, e non fa media.

La presentazione finale vale anche come prova orale: parlano tutti i componenti del
gruppo, e le domande riguardano l'intera analisi.

## Come organizzare i file

**Un unico notebook basta.** Le due parti sono due sezioni dello stesso documento:
`notebooks/analisi.ipynb` è vuoto, e la Parte 2 continua dove finisce la Parte 1. Chi
preferisce può dividere in più notebook, ma non serve.

- `notebooks/` — il notebook (o i notebook) dell'analisi.
- `data/` — i dati, che **non** vanno committati: `data/README.md` spiega come
  procurarseli, così chi clona il repository può rifare tutto.
- `environment.yml` — l'ambiente. Se il notebook importa qualcosa, va aggiunto qui, non
  installato dentro una cella.

## Come consegnare

Si lavora su un fork di questo repository. Tre modi, quello che preferite:

- fork **pubblico** e mandate il link;
- fork **privato** con `antoninofurnari` aggiunto come collaboratore;
- oppure uno **zip** del repository via e-mail.

## Prima di consegnare

`python tools/check_repo.py` verifica che il repository sia consegnabile — dati non
committati, notebook leggero, nessun percorso assoluto — ed è lo stesso controllo che
gira automaticamente a ogni push sul vostro fork. Le condizioni sono sulla
[pagina del corso](https://antoninofurnari.github.io/fad-2627/projects.html).
