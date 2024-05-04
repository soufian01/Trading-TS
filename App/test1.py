from yahoo_fin.stock_info import get_day_gainers, get_day_losers, get_day_most_active
import pandas as pd
import time

# Funzione per ottenere i migliori guadagnatori
def get_best_gainers():
    start_time = time.time()  # Registra il tempo di inizio
    gainers = get_day_gainers()
    end_time = time.time()  # Registra il tempo di fine
    elapsed_time = end_time - start_time  # Calcola il tempo trascorso
    print("Tempo impiegato per ottenere i migliori guadagnatori:", elapsed_time, "secondi")

    gainers = gainers.to_dict(orient="records")
    return gainers

print(get_best_gainers())
