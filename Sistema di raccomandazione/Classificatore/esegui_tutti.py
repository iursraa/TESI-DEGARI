import os
import subprocess
import sys

# --- CONFIGURAZIONE ---
CARTELLA_FILE = "../prototipi_14_termini"  # Il nome della cartella con i tuoi txt
SCRIPT_RECOMMENDER = "Recommender.py"  # Il nome del tuo script


# ----------------------

def main():
    # Controllo che il file Recommender e la cartella esistano
    if not os.path.exists(SCRIPT_RECOMMENDER):
        print(f"Errore: Non trovo '{SCRIPT_RECOMMENDER}'. È nella stessa cartella?")
        return
    if not os.path.exists(CARTELLA_FILE):
        print(f"Errore: Non trovo la cartella '{CARTELLA_FILE}'. Creala e mettici i file dentro.")
        return

    # Prendo tutti i file nella cartella, ignorando le sottocartelle o i file nascosti
    files = [f for f in os.listdir(CARTELLA_FILE) if
             os.path.isfile(os.path.join(CARTELLA_FILE, f)) and not f.startswith('.')]

    if not files:
        print(f"La cartella '{CARTELLA_FILE}' è vuota!")
        return

    print(f"Trovati {len(files)} file. Inizio l'analisi...\n")

    # Ciclo su ogni file e lancio il Recommender
    for filename in files:
        filepath = os.path.join(CARTELLA_FILE, filename)

        print(f"{'=' * 60}")
        print(f" ESECUZIONE PER: {filename}")
        print(f"{'=' * 60}")

        try:
            # sys.executable assicura che usi la stessa versione di Python (python o python3)
            result = subprocess.run(
                [sys.executable, SCRIPT_RECOMMENDER, filepath],
                capture_output=True,
                text=True
            )

            # Stampa quello che esce dal Recommender (print)
            if result.stdout:
                print(result.stdout.strip())

            # Se ci sono errori (es. file formattato male), li stampa
            if result.stderr:
                print("\n[!] ATTENZIONE - ERRORI RILEVATI:")
                print(result.stderr.strip())

        except Exception as e:
            print(f"Impossibile eseguire lo script per {filename}: {e}")

        print("\n")  # Spazio tra un file e l'altro

    print("Analisi completata su tutti i file!")


if __name__ == "__main__":
    main()