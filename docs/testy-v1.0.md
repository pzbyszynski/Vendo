# Rzeczywiste Wyniki Testów Aplikacji Vendo v1.0.0 (MVP 1.0)

* **Data przeprowadzenia testów:** 2026-11-11[cite: 8].
* **Środowisko:** Windows 11 / macOS, Python 3.11, Flask 3.0.2, SQLite 3[cite: 8, 9, 11].
* **Wersja aplikacji:** v1.0.0 (Architektura MVC)[cite: 12, 15].

---

## Tabela Wyników Testów Rzeczywistych

| ID Testu | Scenariusz / Dane Wejściowe | Przebieg i Oczekiwany Wynik | Rzeczywisty Wynik | Status[cite: 15] |
| :--- | :--- | :--- | :--- | :--- |
| **T01** | Inicjalizacja bazy: `python init_db.py`[cite: 10] | Utworzenie tabel w SQLite oraz konta demo ID=1[cite: 10]. | Plik `vendo.db` utworzony. Wyświetlono komunikat sukcesu w konsoli. | **Działa**[cite: 15] |
| **T02** | Otwarcie trasy głównej `GET /` (W01)[cite: 9, 14] | Kontroler wywołuje model `pobierz_produkty()` i renderuje `w01_magazyn.html`[cite: 13, 14]. | Wyświetlono magazyn z produktem startowym "Kurtka Nike". | **Działa**[cite: 15] |
| **T03** | F01/F02: Próba przesłania pustego formularza W02[cite: 14] | Odrzucenie formularza przez kontroler i alert błędu[cite: 14]. | Alert "Wprowadź słowo kluczowe...". Brak wpisu w bazie. | **Działa**[cite: 15] |
| **T04** | F01/F02: Wpisanie "Bluza Puma" w W02[cite: 14] | Model `utworz_produkt_szkic_ai()` generuje sugerowane dane, dodaje Szkic w bazie i przekierowuje do edycji[cite: 13, 14]. | Przekierowano do `/edycja/2`. Wyświetlono dane AI [AI] Bluza Puma. | **Działa**[cite: 15] |
| **T05** | F03 (Błąd): Podanie ceny `-30` PLN w W03[cite: 14] | Model `zaktualizuj_produkt()` waliduje wartość i zwraca `False`[cite: 13, 14]. | Wyświetlono komunikat "Cena musi być wartością wyższą niż 0 PLN!". | **Działa**[cite: 15] |
| **T06** | F03 (Sukces): Poprawna edycja (Cena: `110.00`, Status: "Aktywny")[cite: 14] | Zapis w bazie danych, powrót na W01 z zielonym badge'em statusu[cite: 13, 14]. | Rekord zaktualizowany w bazie SQLite, powrót na listę magazynu. | **Działa**[cite: 15] |
| **T07** | F04: Usuwanie przedmiotu (`POST /usun/2`)[cite: 14] | Model `usun_produkt()` wykonuje `DELETE` i przekierowuje na W01[cite: 13, 14]. | Produkt usunięty z listy W01 i bazy danych. | **Działa**[cite: 15] |
| **T08** | Test Trwałości Danych po Restarcie[cite: 11, 15] | Zatrzymanie serwera (`Ctrl+C`), ponowne uruchomienie `python app.py` i odświeżenie W01[cite: 9, 11, 15]. | Wszystkie dodane i zmodyfikowane produkty pozostały w bazie `vendo.db`. | **Działa**[cite: 15] |
