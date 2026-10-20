"""
Generowanie ścieżek - część II: Krzysztof Guz
"""


from pathlib import Path

MIESIACE = {"styczen": "Styczeń","luty": "Luty", "marzec": "Marzec", 
    "kwiecien": "Kwiecień", "maj": "Maj", "czerwiec": "Czerwiec",
    "lipiec": "Lipiec", "sierpien": "Sierpień","wrzesien": "Wrzesień", 
    "pazdziernik": "Październik", "listopad": "Listopad", "grudzien": "Grudzień",
}
DNI = {"pn": "poniedziałek", "wt": "wtorek", "sr": "środa", "cz": "czwartek",
       "pt": "piątek", "sb": "sobota", "nd": "niedziela"}

PORY = {"r": "rano", "w": "wieczorem"}


def generuj_sciezki(lista_miesiecy, lista_dni, lista_por, formaty):
    """
    Generuje ścieżki na podstawie podanych parametrów, zgodnie z poleceniem. 
    Zwraca listę ścieżek, gdzie każda ścieżka jest w formacie miesiąc/dzień/pora/Dane.csv .
    """
    
    sciezki, i = [], 0

    for miesiac, dni in zip(lista_miesiecy, lista_dni):
        for dzien in dni:

            if (i < len(lista_por)):
                pora = PORY[lista_por[i]]
            else: 
                pora = "rano"

            if (i < len(formaty)):
                format = formaty[i]
            else:
                format = "csv"

            i += 1

            sciezki.append(Path(f"{MIESIACE[miesiac]}/{DNI[dzien]}/{pora}/Dane.{format}"))

    return sciezki


if __name__ == "__main__":
    # Test przy samodzielnym uruchomieniu pliku path_handler.py
    lista_miesiecy = ["styczen", "luty"]
    lista_dni = [["pn", "wt"], ["pt"]]
    lista_por = ["r", "w"]
    formaty = ["csv", "json"]

    for s in generuj_sciezki(lista_miesiecy, lista_dni, lista_por, formaty): 
        print(s)