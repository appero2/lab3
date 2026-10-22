"""
Generowanie ścieżek - część II: Krzysztof Guz
Link do repozytorium: https://github.com/appero2/lab3.git
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


def rozwin_dni(zakres):
    # Funkcja przyjmuje zakres dni w formacie "pt-nd" i zwraca listę ['pt', 'sb', 'nd']

    if "-" in zakres:
        pocz, kon = zakres.split("-")
        return list(DNI.keys())[list(DNI.keys()).index(pocz):list(DNI.keys()).index(kon)+1]
    else:
        return [zakres]
    

def generuj_sciezki(lista_miesiecy, lista_dni, lista_por, formaty):
    """
    Generuje ścieżki na podstawie podanych parametrów, zgodnie z poleceniem. 
    Zwraca listę ścieżek, gdzie każda ścieżka jest w formacie miesiąc/dzień/pora/Dane.csv (albo Dane.json).
    Przyjmuje dane postaci:
    ["styczen", "luty"], [["pn", "wt"], ["pt"]], ["r", "w"], ["json", "csv"] lub równoważnie
    ["styczen", "luty"], [["pn", "wt"], ["pt"]], ["r", "w", "r"], ["json", "csv", "csv"] 
    
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
    # Test przy samodzielnym uruchomieniu path_handler.py
    
    lista_miesiecy = ["styczen", "luty"]
    lista_dni = [["pn", "wt"], ["pt"]]
    lista_por = ["r", "w"]
    formaty = ["csv", "json"]
    lista_dni_test= ["pn-wt", "pt-nd", "cz"]

    for s in generuj_sciezki(lista_miesiecy, lista_dni, lista_por, formaty): 
        print(s)

    for zakres in lista_dni_test:
        print(rozwin_dni(zakres))