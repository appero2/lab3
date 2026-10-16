# lab3
## Zadanie małe (zajęcia 3 skrytptowy Python)

Zadanie jest grupowe, a jego celem jest stworzenie skryptu w Pythonie.

Żyjemy w społeczeństwie informacyjnym. Jest duża szansa, że w naszej pracy konieczne będzie przetwarzanie danych. W ramach tego zadania nie będziemy wykonywać złożonych analiz. Załóżmy, że mamy zebrać informacje z wielu plików przechowywanych w skomplikowanej strukturze katalogów. Mogą to być wyniki eksperymentalne doświadczeń naukowych, dane medyczne, dane z ankiet, logi z naszej aplikacji...

Załóżmy, że nasza struktura składa się z następujących poziomów: Poziom 1 - katalogi o nazwach będących nazwami miesięcy; Poziom 2 - katalogi o nazwach dni tygodnia; Poziom 3 - katalogi rano, wieczór; Poziom 4 - własciwe pliki z danymi o popularnych formatach `csv` i `json`.

Stwórz repozytorium w git-cie a w nim skrypt tworzący lub czytający pliki, według zasad opisanych poniżej.

**Ważne:** istnieje duża dowolność interpretacji poniższych wymagań. Należy uzgodnić je w ramach grupy, a program ma jasno przedstawić swoje możliwości z wykorzystaniem biblioteki `argparse`, np. dzięki uruchomieniu `moj_skrypt.py -h`.

### Wymagania

Skrypt, ma pozwalać na określenie w parametrach następujących opcji:

**a)** wybór miesięcy (można wybrać dowolną ilość)

**b)** wybór *zakresu* dni tygodnia (tyle samo argumentów co w (a) )

**c)** wybór pory dnia, rano albo wieczorem (domyślnie rano), dla każdego z dni wynikłych z rozpisania zakresów powyżej

Jeżeli wybraliśmy styczeń i luty, w styczniu poniedziałek-wtorek (2 dni), a w lutym piątek (1 dzień), to oczekujemy w sumie 3 parametry pory dnia: dla poniedziałków w styczniu, dla wtorków w styczniu i piątków w lutym. Nie podane parametry pory dnia przyjmują wartość domyślną (rano).

Zadane parametry służą do wygenerowania struktury katalogów, patrz przykład poniżej:

**Przykład:**

```text
Wejście: [styczeń, luty], [pn-wt, pt], [r,w]

Styczeń/poniedziałek/rano
Styczeń/wtorek/wieczorem
Luty/piątek/rano (bo domyślnie)
```

**d)** wybór opcji tworzenie / odczyt

np. parametry `-t` (tworzenie) `-o` (odczytywanie); oczywiście można też założyć, że domyślnie pliki są odczytywane, a jest tylko jedna opcja `-t`, i gdy uruchamiamy `moj_skrypt -t` pliki są tworzone; w grupie ustalamy, co jeśli plik już jest, czy tworzymy go na nowo, czy nie; podobnie każda grupa ustala we własnym zakresie, co robi skrypt jak nie ma pliku do odczytu, czy ignorowany jest taki przypadek, czy wypisywany jest komunikat na ekran ect.

**e)** wybór formatu pliku csv / json

podobnie jednym z rozwiązań mogą być flagi `-c` (csv) `-j` (json); analogicznie jak wyżej, w grupie można ustalić, czy są to wykluczające się opcje, czy skrypt może wygenerować dwa pliki; opis jak tworzyć pliki znajduje się poniżej;

Oczekujemy, aby dla każdego określonego parametrami zbioru ścieżek, w zależności od parametru, albo:

- utworzyć pliki zadanego typu
- wczytać pliki zadanego typu i podać wynik

**UWAGI:**

Zalecamy grupy 3 lub 4 osobowe. W przypadku grupy 3-osobowej skrypt nie musi umożliwiać tworzenia/odczytu dla jednego z formatów json/csv. Podobnie w przypadku grupy 2-osobowej.

Proponujemy następujący podział zadań:

**Osoba 1**

- tworzy repozytorium w git-cie i zarządza skryptem z najwyższego poziomu (obsługuje parametry korzystając z biblioteki argparse)

**Osoba 2**

- tworzy część generującą ścieżki i tworzącą pliki (na tych ścieżkach) lub odczytującą informację z takich plików

**Osoba 3 / Osoba 1**

- tworzy zapis do pliku csv

Plik `Dane.csv` ma składać się z dokładnie dwóch linii:

```text
Model; Wynik; Czas; 
A ; 17 ; 465s;
```

Pierwsza linia ma być identyczna dla wszystkich plików.

Druga linia ma być generowana losowo (x in {A,B,C}, 0-1000, 0-1000s)

- tworzy odczyt z pliku csv

Interesuje nas tylko i wyłącznie suma wartości z kolumny `Czas` dla wszystkich plików, gdzie w kolumnie `Model` mamy wartość `A`.

**Osoba 4 / Osoba 2**

- odczyt i zapis do pliku json z analogicznymi wymaganiami jak dla csv

**UWAGI:**

Oczekujemy, że każdy członek zespołu zakomituje własną część do repozytorium.