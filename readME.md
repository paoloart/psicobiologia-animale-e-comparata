# Guida all'uso dell'applicazione Domande Psicobiologia Comparata

<<<<<<< HEAD
L'applicazione Quiz Domande permette di svolgere un quiz con domande caricate da file di testo, monitorando il tempo impiegato per rispondere a ciascuna domanda. E' possibile modificare o aggiungere domande modificando i file prima_parte.txt, seconda_parte.txt, terza_parte.txt
=======
L'applicazione permette di svolgere un quiz con domande caricate da file di testo, monitorando il tempo impiegato per rispondere a ciascuna domanda. Il file è OpenSource e pensato per coloro che devono sostenere l'esame di Psicobiologia Animale e Comparata ma può essere riadattato per qualsiasi altro utilizzo. Il programma non è una risorsa ufficiale del corso, ma uno strumento per randomizzare le domande sviluppato da uno studente.
>>>>>>> 0819f6eb423697a29bbc0fad402692915ca36d6f

## Installazione

Prima di poter utilizzare l'applicazione, è necessario installare le dipendenze Python richieste. Questo può essere fatto installando i pacchetti elencati nel file `requirements.txt` con il seguente comando:

pip install -r requirements.txt

<<<<<<< HEAD
Da incollare nel terminale.

Assicurati di avere installato Python e pip sul tuo sistema prima di eseguire questo comando. Per usare Python puoi usare risorse gratuite come Visual Studio Code
=======
Assicurati di avere installato Python e pip sul tuo sistema prima di eseguire questo comando.
>>>>>>> 0819f6eb423697a29bbc0fad402692915ca36d6f

## Avvio dell'applicazione

Dopo aver installato le dipendenze, l'applicazione può essere avviata eseguendo il file Python principale ('main.py`). Se stai usando un terminale, puoi farlo con il seguente comando:

python main.py

Se stai usando Visual Studio Code vai sul file main.py e clicca la freccia che si trova in alto a destra per runnare il codice

## Utilizzo dell'applicazione

Dopo aver avviato l'applicazione, segui i passaggi seguenti per utilizzarla:

### Seleziona i file delle domande

L'applicazione fornisce tre opzioni per caricare i file di domande:
1. "Prima parte"
2. "Seconda parte"
3. "Terza parte"

Spunta le caselle corrispondenti ai file che desideri utilizzare per il tuo quiz. Le domande fanno riferimento all'anno accademico 2020/2021. Se sei di un altro anno puoi andare a modificare i file di testo aggiornandoli con le domande degli anni successivi.

### Inizia le domande

Clicca sul pulsante "Inizia con le domande" per iniziare il quiz. Il tempo inizierà a contare dal momento in cui la domanda viene visualizzata.

### Rispondi alle domande

Ogni volta che rispondi a una domanda, premi il tasto "Return" sulla tua tastiera o clicca sul pulsante "Prossima domanda". Questo fermerà il timer, salverà il tempo impiegato per rispondere alla domanda e visualizzerà la prossima domanda.

### Pausa

Se hai bisogno di una pausa, puoi premere il pulsante "Pausa". Premilo di nuovo per riprendere. Questa parte presenta ancora un bug da risolvere ma non compromette il funzionamento del programma

### Resetta il programma

Se vuoi ricominciare il quiz da capo, premi il pulsante "Reset programma". Questo cancellerà tutte le risposte date e permetterà di ricominciare il quiz.

### Termina il programma

Quando hai finito, puoi chiudere l'applicazione premendo il pulsante "Termina il programma".

### Cancella i risultati

Se vuoi cancellare tutti i risultati salvati, clicca sul pulsante "Cancella risultati". Prima di farlo, assicurati di aver salvato i risultati in un altro luogo, poiché questa azione non può essere annullata.


