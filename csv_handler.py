"""Obsługa zapisu i odczytu CSV — część III: Zuzanna Lubas.

Zgodnie z poleceniem:
- każdy plik Dane.csv ma dokładnie dwa wiersze;
- pierwszy wiersz jest stały i identyczny we wszystkich plikach;
- drugi wiersz zawiera losowe wartości: model A/B/C, wynik 0–1000, czas 0–1000 s;
- odczyt zwraca sumę czasu tylko dla rekordów z modelem A.
"""

import random
from pathlib import Path

NAGLOWEK_CSV = "Model; Wynik; Czas; "


def zapisz_csv(sciezka):
    """Zapisuje plik CSV z jednym stałym nagłówkiem i jednym losowym rekordem."""
    sciezka = Path(sciezka)
    sciezka.parent.mkdir(parents=True, exist_ok=True)

    model = random.choice(["A", "B", "C"])
    wynik = random.randint(0, 1000)
    czas = random.randint(0, 1000)

    # Tryb 'w' tworzy plik lub zastępuje jego dotychczasową zawartość.
    with sciezka.open("w", encoding="utf-8", newline="") as plik:
        plik.write(NAGLOWEK_CSV + "\n")
        plik.write(f"{model} ; {wynik} ; {czas}s;\n")


def odczytaj_csv(sciezka):
    """Odczytuje Dane.csv i zwraca dane jako słownik."""
    sciezka = Path(sciezka)

    with sciezka.open("r", encoding="utf-8", newline="") as plik:
        linie = [linia.rstrip("\r\n") for linia in plik]

    if len(linie) != 2:
        raise ValueError(f"{sciezka}: plik musi zawierać dokładnie dwa wiersze.")

    if linie[0] != NAGLOWEK_CSV:
        raise ValueError(f"{sciezka}: niepoprawny nagłówek CSV.")

    wartosci = [element.strip() for element in linie[1].rstrip(";").split(";")]
    if len(wartosci) != 3:
        raise ValueError(f"{sciezka}: drugi wiersz musi zawierać Model, Wynik i Czas.")

    model, wynik, czas = wartosci

    if model not in {"A", "B", "C"}:
        raise ValueError(f"{sciezka}: Model musi mieć wartość A, B lub C.")
    if not wynik.isdigit() or not 0 <= int(wynik) <= 1000:
        raise ValueError(f"{sciezka}: Wynik musi być liczbą całkowitą z zakresu 0–1000.")
    if not czas.endswith("s") or not czas[:-1].isdigit():
        raise ValueError(f"{sciezka}: Czas musi mieć format np. 465s.")
    sekundy = int(czas[:-1])
    if not 0 <= sekundy <= 1000:
        raise ValueError(f"{sciezka}: Czas musi być z zakresu 0–1000 sekund.")

    return {"Model": model, "Wynik": int(wynik), "Czas": sekundy}


def suma_czasu_modelu_a(sciezki):
    """Sumuje kolumnę Czas tylko z plików, w których Model ma wartość A."""
    suma = 0
    for sciezka in sciezki:
        dane = odczytaj_csv(sciezka)
        if dane["Model"] == "A":
            suma += dane["Czas"]
    return suma


if __name__ == "__main__":
    # Samodzielny test: uruchom `python csv_handler.py`.
    plik_testowy = Path("dane_testowe") / "Dane.csv"
    zapisz_csv(plik_testowy)
    print(f"Zapisano plik: {plik_testowy}")
    print("Dane odczytane z pliku:", odczytaj_csv(plik_testowy))
    print("Suma czasu dla modelu A:", suma_czasu_modelu_a([plik_testowy]), "s")
