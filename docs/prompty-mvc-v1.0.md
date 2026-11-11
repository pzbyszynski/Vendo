# Rejestr promptów i inżynieria promptów (Wersja v1.0.0)

* **Użyty czat AI:** Google Gemini (Dostęp bezpłatny)[cite: 8].
* **Data wykonania:** 2026-11-11 [cite: 8].
---

## 1. Porównanie promptu ogólnego i precyzyjnego (Sekcja 2 Laba 04)[cite: 12]

* **Prompt Ogólny (Niepoprawny):**
  > "Zrób mi podział na MVC w Flasku dla sklepu."
  * *Wada:* Brak informacji o istniejących plikach, brakuje podania schematu bazy danych, brakuje reguł walidacji oraz nazwy używanego narzędzia (SQLite/Blueprint)[cite: 12].

* **Prompt Precyzyjny (Poprawny – Zastosowany w projekcie):**
  > "W obecnym projekcie Vendo przeorganizuj płaski kod z `app.py` do struktury MVC. Przenieś operacje bazodanowe do `models/produkt.py`, trasy Flask do kontrolera `controllers/produkty.py` jako Blueprint, a funkcję połączenia do `db.py`. Zachowaj działające funkcje F01-F04 oraz obsługę użytkownika demo nr 1. Podaj pełny kod zmienionych plików oraz strukturę katalogów."[cite: 12, 13, 14]

---

## 2. Szablony promptów użytych w projekcie (P1 - P4)[cite: 13, 14, 15]

### Prompt P1: Plan MVP i mapa MVC[cite: 13]
> **Treść:** Pomóż nam zaplanować MVP 1.0 projektu Vendo. Cel użytkownika: Szybkie dodawanie przedmiotów z sugerowanymi przez AI danymi i zarządzanie własnym magazynem. Stos: Python 3, Flask, SQLite, HTML/CSS. Zakres: F01 (dodawanie), F02 (generowanie AI), F03 (edycja/walidacja), F04 (zarządzanie/usuwanie). Widoki i dane: W01-W03, tabele `uzytkownik`, `produkt`, `zdjecie_produktu`. Aktualny kod zawiera wszystko w jednym pliku `app.py`. Przygotuj plan podziału na modele, widoki i kontroler Blueprint.[cite: 13]

### Prompt P2: Działający szkielet MVC[cite: 14]
> **Treść:** Wykonaj pierwszy etap zaakceptowanego planu dla Vendo. Technologie: Python 3 + Flask Blueprint + SQLite. Wyodrębnij model `models/produkt.py`, widoki w `templates/produkty/` oraz kontroler `controllers/produkty.py`. Kontroler ma odbierać żądanie, wywoływać model i wybierać widok lub przekierowanie. Podaj kod `db.py`, `app.py` oraz zmienionych kontrolerów. Kryterium: Aplikacja startuje i pokój listę z bazy na W01.[cite: 14]

### Prompt P3: Jedna funkcja MVP z przykładami wyników (F03 Edycja i Walidacja)[cite: 14]
> **Treść:** W aktualnym kodzie MVC wykonaj funkcję F03 (edycja i zatwierdzenie danych przedmiotu). Użytkownik: Demo nr 1. Dane wejściowe: `ostateczny_tytul`, `ostateczny_opis`, `ostateczna_cena`, `status`. Reguły modelu: Tytuł i opis nie mogą być puste. Cena musi być float > 0 PLN. Przykład poprawny: Tytuł "Kurtka Nike", Cena 120.00 -> Zapis w bazie i komunikat sukcesu. Przykład błędny: Cena -15.00 -> Odrzucenie i komunikat "Cena musi być wartością wyższą niż 0 PLN!". Zwróć zmienione pliki.[cite: 14]

### Prompt P4: Diagnoza i poprawka przed odbiorem
> **Treść:** Sprawdź zgłoszoną niezgodność w Vendo MVP 1.0. Uruchomiono aplikację poleceniem `python app.py`. Problem: Po przeniesieniu do Blueprintu odnośniki w szablonach HTML zwracały błąd `BuildError` dla `url_for('w01_magazyn')`. Oczekiwane działanie: Prawidłowe generowanie adresów tras Blueprintu. Przestudiuj przyczyny, wskaż najmniejszą poprawkę (zmiana nazw tras na `produkty.w01_magazyn`) i przedstaw scenariusz weryfikacji.

---

## 3. Poprawka promptu i iteracja z dowodami (Sekcja 1 Laba 04)[cite: 12]
* **Wkryty problem:** Pierwsza wersja wygenerowana przez AI nie uwzględniła zmiany przestrzeni nazw tras w funkcji `url_for()` w szablonach Jinja2 po przejściu na Blueprint `produkty_bp`[cite: 13, 15].
* **Działanie zespołu:** Wygenerowano nakierowany prompt diagnozujący błąd P4. Poprawiono wpisy w szablonach z `url_for('w01_magazyn')` na `url_for('produkty.w01_magazyn')`, przywracając pełną stabilność nawigacji[cite: 13, 15].
