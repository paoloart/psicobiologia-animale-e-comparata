import tkinter as tk
import tkinter.messagebox as messagebox
import random
from time import time
import pandas as pd
from functions import leggi_domande, scegli_domanda, salva_risultato

PRIMA_PARTE = 'prima_parte.txt'
SECONDA_PARTE = 'seconda_parte.txt'
TERZA_PARTE = 'terza_parte.txt'
RISULTATI_FILE = 'risultati.csv'

start_time = None
paused = False


def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Riprendi")
    else:
        pause_button.config(text="Pausa")


def seleziona_file_domande():
    file_selezionati = []
    if check_var_1.get():
        file_selezionati.append(PRIMA_PARTE)
    if check_var_2.get():
        file_selezionati.append(SECONDA_PARTE)
    if check_var_3.get():
        file_selezionati.append(TERZA_PARTE)
    return file_selezionati


domande_gia_fatte = []


def nuova_domanda(event=None):
    global start_time, domande_gia_fatte
    file_domande = seleziona_file_domande()
    if not file_domande:
        domanda_label.config(text="Seleziona almeno un file di domande.")
        return
    domande = []
    for file in file_domande:
        domande.extend(leggi_domande(file))
    domanda = scegli_domanda(domande, domande_gia_fatte)
    if domanda:
        domanda_label.config(text=domanda)
        domande_gia_fatte.append(domanda)
        start_time = time()
        reset_button.pack(padx=20, pady=20)  # Mostra il bottone reset
    else:
        result = messagebox.askquestion(
            "Domande esaurite", "Hai finito tutte le domande! Vuoi ricominciare con le stesse domande?")
        if result == 'yes':
            domande_gia_fatte = []
            nuova_domanda()
        else:
            result = messagebox.askquestion(
                "Scegli nuovo gruppo di domande", "Vuoi scegliere un nuovo gruppo di domande?")
            if result == 'yes':
                domande_gia_fatte = []
            else:
                domanda_label.config(text="Non ci sono più domande!")


def reset_program():
    global start_time, domande_gia_fatte
    start_time = None
    domande_gia_fatte = []
    domanda_label.config(text="")
    inizia_button.pack(pady=20, padx=20)
    app.bind('<Return>', inizia_domanda)
    reset_button.pack_forget()  # Nasconde il bottone reset


def salva_tempo(event=None):
    global start_time
    end_time = time()
    tempo = end_time - start_time
    # Use cget() method to get the current question text
    current_question = domanda_label.cget("text")
    salva_risultato(RISULTATI_FILE, current_question, tempo)
    nuova_domanda()


def termina_programma():
    app.destroy()


def update_time():
    global start_time, paused
    if start_time is not None and not paused:
        current_time = time()
        elapsed_time = int(current_time - start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        time_label.config(text=f"Tempo trascorso: {minutes:02d}:{seconds:02d}")
    app.after(1000, update_time)


def inizia_domanda(event=None):
    global start_time
    file_domande = seleziona_file_domande()
    if not file_domande:
        messagebox.showerror("Errore", "Seleziona almeno un file di domande.")
        return
    start_time = time()
    inizia_button.pack_forget()
    app.bind('<Return>', salva_tempo)
    nuova_domanda()


def conferma_cancella_risultati():
    result = messagebox.askquestion(
        "Conferma", "Sei sicuro di voler cancellare tutti i risultati?")
    if result == 'yes':
        cancella_risultati()


def cancella_risultati():
    result_df = pd.DataFrame(columns=["Domanda", "Tempo"])
    result_df.to_csv(RISULTATI_FILE, index=False)


app = tk.Tk()

app.title("Quiz Domande")
app.geometry("800x800")
app.iconbitmap("luca-bonini.ico")
title_label = tk.Label(
    app, text="Domande esame Psicobiologia Animale e Comparata", font=("Helvetica", 24))
title_label.pack(pady=20)

check_var_1 = tk.BooleanVar()
check_var_2 = tk.BooleanVar()
check_var_3 = tk.BooleanVar()

check_button_container = tk.Frame(app)
check_button_container.pack(pady=10)

check_button_1 = tk.Checkbutton(
    check_button_container, text="Prima parte", variable=check_var_1)
check_button_1.pack(side="left", padx=10)

check_button_2 = tk.Checkbutton(
    check_button_container, text="Seconda parte", variable=check_var_2)
check_button_2.pack(side="left", padx=10)

check_button_3 = tk.Checkbutton(
    check_button_container, text="Terza parte", variable=check_var_3)
check_button_3.pack(side="left", padx=10)

domanda_label = tk.Label(app, text="", wraplength=600,
                         justify="center", font=("Helvetica", 24))
domanda_label.pack(padx=20, pady=20)

time_label = tk.Label(app, text="Tempo trascorso: 00:00",
                      font=("Helvetica", 14))
time_label.pack(pady=20)

inizia_button = tk.Button(
    app, text="Inizia con le domande", command=inizia_domanda)
inizia_button.pack(pady=20)

reset_button = tk.Button(app, text="Reset programma",
                         bg="blue", command=reset_program)
pause_button = tk.Button(app, text="Pausa", bg="yellow", command=toggle_pause)
pause_button.pack(padx=20, pady=20)

# Crea un nuovo frame per i bottoni
button_frame = tk.Frame(app)
button_frame.pack(side="bottom", pady=100)

# Aggiungi i bottoni al frame

next_button = tk.Button(
    button_frame, text="Prossima domanda", bg="green", command=salva_tempo)
next_button.pack(side="left", padx=20, pady=20)

cancella_risultati_button = tk.Button(
    button_frame, text="Cancella risultati", bg="red", command=conferma_cancella_risultati)
cancella_risultati_button.pack(side="left", padx=20, pady=20)

exit_button = tk.Button(
    button_frame, text="Termina il programma", bg="red", command=termina_programma)
exit_button.pack(side="left", padx=20, pady=20)

app.bind('<Return>', inizia_domanda)
nuova_domanda()
update_time()

app.mainloop()
