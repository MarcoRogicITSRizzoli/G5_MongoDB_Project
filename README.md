# G5_MongoDB_Project

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Indice</summary>
  <ol>
    <li>
      <a href="#il-progetto">Il Progetto</a>
      <ul>
        <li><a href="#librerie-principali">Librerie principali</a></li>
      </ul>
    </li>
    <li>
      <a href="#come-iniziare">Come iniziare</a>
      <ul>
        <li><a href="#prerequisiti">Prerequisiti</a></li>
        <li><a href="#installazioni">Installazioni</a></li>
        <li><a href="#avvio-del-software">Avvio del software</a></li>
      </ul>
    </li>
    <li>
      <a href="#istruzioni">Istruzioni</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#fonti">Fonti</a></li>
  </ol>
</details>


## Il Progetto

Abbiamo realizzato un sistema di gestionale di ricerca e acquisto di biglietti per concerti con l'utilizzo di MongoDBper la memorizzazione dei vari eventi. La struttura è suddivisa in vari moduli, ognuno dei quali si occupa di specifiche funzionalità. Il tutto è coordinato dal modulo principale, main.py, che gestisce le interazioni tramite interfaccia utente.

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>



### Librerie principali

- `pymongo`: Per interagire con il server MongoDB.
- `bson`: Per la gestione del file Json all'interno del database.
- `geopy`: Per la codifica delle coordinate geografiche

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>



## Come iniziare


### Prerequisiti

Prima di eseguire l'applicazione, assicurarsi di avere i seguenti prerequisiti installati:

1. **Python V 3.12:** Per installare la versione di python necessaria, potete scaricarlo dal sito ufficiale https://www.python.org/downloads/

2. **Server MongoDB:** Nel codice è già inserito un server MongoDB Compass per il salvataggio dei json, se si vuole utilizzare un proprio server e visualizzare i dati, si dovrà scaricare il softare "MongoDBCompass" del seguente sito web: https://www.mongodb.com/products/tools/compass
Dopo aver scaricato e aperto il software dalla sua interfaccia sarà possibile creare un proprio database con le proprie credenziali.
Una volta creato il database sarà possibile copiare la sua uri sempre da Compass, questa uri dovrà essere messa al posto della uri già presente nel modulo main.py



### Installazioni
1° Metodo

1. Clonare la repository in locale aprendo il terminale dalla cartella in cui si vuole inserire il progetto
   ```sh
   git clone https://github.com/MarcoRogicITSRizzoli/G5_MongoDB_Project.git
   ```

2° Metodo
1. Clonare la repository in locale aprendo il terminale dalla cartella in cui si vuole inserire il progetto
   ```sh
   git clone https://github.com/MarcoRogicITSRizzoli/G5_MongoDB_Project.git
   ```
2. Installazione di pip
    Comando per Windows:
   ```sh
   py -m ensurepip --upgrade
   ```
   Comando per Mac:
   ```sh
   python3 -m ensurepip --upgrade
   ```
3. Creazione dell'ambiente di sviluppo venv usando requirements.txt (Per Windows)
   Aprire il terminale tenendo come percorso la cartella in cui si vuole installare l'ambiente
   ```sh
   python -m venv venv
   ```
   ```sh
   venv\Scripts\activate
   ```
   ```sh
   pip install -r requirements.txt
   ```
4. Scaricare le librerie necessarie tramite pip
    Comando per Windows:
    '''sh
    pip install pymongo geopy
    '''
    Comando per Mac:
     '''sh
    pip install pymongo geopy
    '''

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>


### Avvio del software

Il modulo main.py funge da contenitore del main per il lancio del software ma è possibile avviarlo direttamente da terminale

1. Avvio del software da terminale
    Comando per Windows
   ```sh
   py .\main.py
   ```
   Comando per Mac
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>


## Istruzioni

Il software ha due funzionalità principali, descritte di seguito:

1. Ricerca dei concerti o eventi:
L'utente può cercare i vari concerti o eventi in base a diversi parametri:
  - Per artista, ovvero tutti gli eventi in cui un certo artista è presente
  - Per nome dell'evento 
  - Per data, l'utente può vedere quali eventi ci sono in un range di giorni
  - Per distanza, l'utente inserendo le proprie coordinate potrà vedere quali sono gli eventi più vicini a lui (a meno di 7 Km)

2. Acquisto dei biglietti:
L'utente una volta cercato l'evento in base ai parametri scelti prima, potrà poi scegliere il concerto e il numero di biglietti che vuole acquistare per esso, siccome il numero di biglietti è conteggiato, se i posti disponibili sono zero all'utente verrà impedito di comprare il biglietto

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] *Ricerca evento o concerto per nome artista o nome concerto
- [x] *Ricerca evento o concerto per intervallo di date e vicinanza dall'utente a meno di 7 Km 
- [x] *Visualizazione di tutti gli eventi in base al filtro scelto
- [x] *Possibilità di acquistare uno o più biglietti a patto che il numero di posti disponibili sia maggiore

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>


<!-- Fonti -->
## Fonti

Fonti consultate per la realizzazione del progetto

* [Documentazione per l'utilizo delle funzioni di MongoDB](https://www.mongodb.com/docs/languages/python/)
* [Documentazione di geopy per la ricerca in base alla distanza](https://geopy.readthedocs.io/en/stable/)

<p align="right">(<a href="#readme-top">torna in cima</a>)</p>