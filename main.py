'''
    Główny plik zarządzający parametrami, wywołujący funkcje.
    Autor: Kacper Kułak
    Link github: https://github.com/appero2/lab3
'''

import argparse
from csv_handler import zapisz_csv, suma_czasu_modelu_a
from path_handler import generuj_sciezki, rozwin_dni

miesiace = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
dni_tygodnia = ["pn", "wt", "sr", "cz", "pt", "sb", "nd"]
pory_dni = ["r", "w"]

def stworz_parser():
    """
    Funkcja tworzy parser pobierający argumenty.
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument("miesiace", help = "lista miesiecy do wybrania")
    
    parser.add_argument("dzien", help = "lista dni do wybrania")
    
    parser.add_argument("pory_dnia", help = "lista pór dnia: r (rano) lub w (wieczorem) np. [r, w]. Domyślnie rano", nargs = "?")

    parser_trybu = parser.add_mutually_exclusive_group()

    parser_trybu.add_argument("-t", "--tworz", dest = "tworz", action = "store_true", help = "tworzy pliki")
    parser_trybu.add_argument("-o", "--odczytaj", dest = "odczytaj", action = "store_true", help = "odczytuje pliki")

    parser.add_argument("-c", "--csv", action = "store_true", help = "tworzenie / odczyt plikow w formacie csv.")
    parser.add_argument("-j", "--json", action = "store_true", help = "tworzenie / odczyt plikow w formacie json.")
    
    return parser

def parsuj_liste(tekst):
    """
    Przekształca napis w formacie "[styczen, luty]" na listę [styczeń, luty].
    Modyfikuje też wielkość napisów - zapisuje tylko małe litery.
    """
    if not tekst:
        return []

    oczyszczony = tekst.strip("[] ")

    if not oczyszczony:
        return []
    
    return [element.strip().lower() for element in oczyszczony.split(",") if element.strip()]

def parsuj_i_sprawdz_argumenty(args):
    """
    Przekształca argumenty na poprawne wyjście, a następnie weryfikuje ich poprawność. 
    W przypadku, gdy pewien argument nie jest poprawny zwraca błąd.
    
    Jeśli użytkownik nie podaje trybu odczytu (-o), ani tworzenia (-t) to 
    domyślnie wybierany jest tryb odczytu.

    Jeśli użytkownik nie podał ani tryb csv, ani json domyślnie wybierany jest csv.
    """

    lista_miesiecy = parsuj_liste(args.miesiace)
    lista_dni = parsuj_liste(args.dzien)
    lista_por = parsuj_liste(args.pory_dnia) if args.pory_dnia else []

    if not lista_miesiecy:
        raise ValueError("Lista miesięcy nie może być pusta!")
    if not lista_dni:
        raise ValueError("Lista dni nie może być pusta!")

    if len(lista_miesiecy) != len(lista_dni):
        raise ValueError(f"Liczba miesięcy ({len(lista_miesiecy)}) musi być równa liczbie zakresów dni ({len(lista_dni)})!")

    for m in lista_miesiecy:
        if m not in miesiace:
            raise ValueError(f"Nieznany miesiąc: '{m}'")

    for p in lista_por:
        if p not in pory_dni:
            raise ValueError(f"Nieznana pora dnia: '{p}'. Dopuszczalne wartości to: {', '.join(pory_dni)}")

    rozwiniete_dni = [rozwin_dni(zakres) for zakres in lista_dni]
    for dni in rozwiniete_dni:
        for d in dni:
            if d not in dni_tygodnia:
                raise ValueError(f"Nieznany dzień tygodnia: '{d}'. Dopuszczalne skróty to: {', '.join(dni_tygodnia)}")

    if args.tworz:
        tryb = "tworzenie"
    else:
        tryb = "odczyt"

    formaty = []
    if args.json:
        formaty.append("json")
    if args.csv or len(formaty) == 0:
        formaty.append("csv")

    return lista_miesiecy, rozwiniete_dni, lista_por, tryb, formaty

def main():
    parser = stworz_parser()
    args = parser.parse_args()
    
    try:
        lista_miesiecy, rozwiniete_dni, lista_por, tryb, formaty = parsuj_i_sprawdz_argumenty(args)
        sciezki = generuj_sciezki(lista_miesiecy, rozwiniete_dni, lista_por, formaty)
    except (ValueError, KeyError) as e:
        parser.error(str(e))

    sciezki_csv = [s for s in sciezki if s.suffix == ".csv"]
    sciezki_json = [s for s in sciezki if s.suffix == ".json"]

    if sciezki_json:
        print("Format JSON nie jest obsługiwany w tej wersji programu.")

    if not sciezki_csv:
        print("Brak ścieżek CSV do przetworzenia.")
        return

    if tryb == "tworzenie":
        print(f"Tworzenie plików CSV ({len(sciezki_csv)}):")
        for sciezka in sciezki_csv:
            zapisz_csv(sciezka)
            print(f"Utworzono: {sciezka}")
    else:
        print(f"Odczyt plików CSV ({len(sciezki_csv)}):")
        istniejace_csv = []
        for sciezka in sciezki_csv:
            if sciezka.exists():
                istniejace_csv.append(sciezka)
            else:
                print(f"Brak pliku: {sciezka}")

        if not istniejace_csv:
            print("Nie znaleziono żadnych istniejących plików CSV do odczytu.")
            return

        suma = suma_czasu_modelu_a(istniejace_csv)
        print(f"\nŁączny czas dla rekordów z modelem A: {suma}s")

if __name__ == "__main__":
    main()
