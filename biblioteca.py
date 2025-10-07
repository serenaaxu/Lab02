import csv

def carica_da_file(filename):
    """Carica i libri dal file"""
    # TODO
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            reader = csv.reader(f)
            righe = list(reader)
    except FileNotFoundError:
        print("File not found")
        return None
    num_sezioni = 5

    biblioteca = [[] for i in range(num_sezioni)]
    for riga in righe[1:]:
        campi = [c.strip() for c in riga]
        if len(campi) != num_sezioni:
            continue

        titolo, autore, anno, pagine, sezione = campi
        libro = {"titolo" : titolo,
        "autore" : autore,
        "anno" : int(anno),
        "pagine" : int(pagine),
        "sezione" : int(sezione)}

        if 1 <= libro["sezione"] <= num_sezioni:
            biblioteca[libro['sezione'] - 1].append(libro)

    return biblioteca



def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, filename):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    for sezione_libri in biblioteca:
        for libro in sezione_libri:
            if libro["titolo"].lower() == titolo.lower():
                print("Il libro è già presente.")
                return None

    nuovo_libro = {"titolo" : titolo,
                "autore" : autore,
                "anno" : int(anno),
                "pagine" : int(pagine),
                "sezione" : int(sezione)
                }

                biblioteca[sezione-1].append(nuovo_libro)

                try:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{titolo},{autore},{anno},{pagine},{sezione}\n")
                        return nuovo_libro
                except FileNotFoundError:
                    return "errore"


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for sezione_libri in biblioteca:
        for libro in sezione_libri:
            if libro["titolo"].lower() == titolo.lower():
                return f"{libro['titolo']}, {libro['autore']}, {libro['anno']}, {libro['pagine']}, {libro['sezione']}"
    return None

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if sezione < 1 or sezione > len(biblioteca):
        return None
    titoli = [libro["titolo"] for libro in biblioteca[sezione-1]]
    return sorted(titoli)


def main():
    biblioteca = []
    filename = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il nome del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip('"')
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro_aggiunto = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, filename)
            if libro_aggiunto == "duplicato":
                print("Il libro è già presente nella biblioteca.")
            elif libro_aggiunto == "errore":
                print("Errore durante scrittura.")
            elif libro_aggiunto is not None:
                print("Libro aggiunto con successo!")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

