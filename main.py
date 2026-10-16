'''
    Autor: Kacper Kułak
'''

import argparse
import sys

miesiace = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
dni_tygodnia = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
pory_dni = ["rano", "wieczor"]

def stworz_parser():
    """
    Funkcja tworzy parser pobierający argumenty.
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument("miesiace", help = "lista miesiecy do wybrania")
    
    parser.add_argument("dzien", help = "lista dni do wybrania")
    
    parser.add_argument("pory_dnia", help = "lista póra dnia: r (rano) lub w (wieczorem) np. [r, w]. Domyślnie rano", nargs = "?")

    parser_trybu = parser.add_mutually_exclusive_group()

    parser_trybu.add_argument("-t", action = "store_true", help = "tworzy pliki")
    parser_trybu.add_argument("-o", action = "store_true", help = "odczytuje pliki")

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

    if args.tworz:
        tryb = "tworzenie"
    else:
        tryb = "odczyt"

    formaty = []
    if args.json:
        formaty.append("json")
    if args.csv or len(formaty) == 0:
        formaty.append("csv")

    return lista_miesiecy, lista_dni, lista_por, tryb, formaty

def main():
    parser = stworz_parser()
    args = parser.parse_args()
    
    try:
        argumenty = parsuj_i_sprawdz_argumenty(args)
    except ValueError as e:
        parser.error(str(e))

if __name__ == "__main__":
    main()