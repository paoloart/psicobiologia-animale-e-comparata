import random
import pandas as pd


def leggi_domande(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        domande = [line.strip() for line in file.readlines()]
    return domande


def scegli_domanda(domande, domande_gia_fatte):
    domande_disponibili = [
        domanda for domanda in domande if domanda not in domande_gia_fatte]
    if domande_disponibili:
        return random.choice(domande_disponibili)
    else:
        return None


def salva_risultato(file_risultati, domanda, tempo):
    try:
        risultati_df = pd.read_csv(file_risultati)
    except pd.errors.EmptyDataError:
        risultati_df = pd.DataFrame(columns=["Domanda"])

    if domanda not in risultati_df["Domanda"].values:
        nuova_riga = pd.DataFrame({"Domanda": [domanda]})
        risultati_df = pd.concat([risultati_df, nuova_riga], ignore_index=True)

    domanda_row = risultati_df.loc[risultati_df["Domanda"] == domanda]
    colonna_tempo = None

    for i in range(1, len(risultati_df.columns) + 1):
        colonna_corrente = f"Tempo_{i}"
        if colonna_corrente not in risultati_df.columns:
            risultati_df[colonna_corrente] = None
        if colonna_corrente not in domanda_row.columns or pd.isna(domanda_row[colonna_corrente].values[0]):
            colonna_tempo = colonna_corrente
            break

    risultati_df.loc[domanda_row.index, colonna_tempo] = tempo
    risultati_df.to_csv(file_risultati, index=False)