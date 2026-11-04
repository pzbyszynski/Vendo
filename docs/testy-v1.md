# Rzeczywiste Wyniki Testów Aplikacji Vendo v1

* **Data testów:** 2026-11-04[cite: 8].
* **Środowisko:** Windows 11, Python 3.11.4, Flask 3.0.2[cite: 9, 11].

| ID Testu | Scenariusz / Dane Wejściowe | Oczekiwany Wynik | Wynik Rzeczywisty | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T01** | Uruchomienie `python init_db.py`[cite: 10] | Utworzenie bazy `vendo.db` i rekordu użytkownika demo nr 1[cite: 10]. | Baza utworzona, wyświetlono komunikat w konsoli. | **Działa** |
| **T02** | Otwarcie widoku `http://127.0.0.1:5000/` (W01)[cite: 9] | Wyświetlenie listy z produktem testowym "Kurtka Nike". | Wyświetlono kartę ze statusem "Aktywny" i ceną 149.99 PLN. | **Działa** |
| **T03** | F01/F02: Próba wysłania pustego formularza w W02 | Odrzucenie formularza z komunikatem o błędzie. | Wyświetlono alert "Wprowadź słowo kluczowe...". | **Działa**[cite: 11] |
| **T04** | F01/F02: Wpisanie "Bluza Adidas" w W02 i podanie zdjęcia | Wygenerowanie propozycji AI i przekierowanie do W03. | Dodano rekord w statusie "Szkic" i przeniesiono do edycji W03. | **Działa**[cite: 11] |
| **T05** | F03: Edycja ceny na `-50` PLN w W03 | Odrzucenie formularza z komunikatem walidacji. | Wyświetlono alert "Cena musi być wartością wyższą niż 0 PLN!". | **Działa**[cite: 11] |
| **T06** | F03: Edycja ceny na `120.00` PLN i zmiana statusu na "Aktywny" | Zapis do bazy danych i powrót do W01. | Rekord zaktualizowany, zielony badge "Aktywny" na liście. | **Działa**[cite: 11] |
| **T07** | F04: Usuwanie produktu z W03 | Usunięcie rekordu z bazy danych i powrót do W01. | Wyświetlono komunikat "Produkt został usunięty". | **Działa**[cite: 11] |
| **T08** | Trwałość danych: Zatrzymanie serwera (Ctrl+C) i ponowny start[cite: 9, 11] | Przechowanie wcześniej wprowadzonych i zmienionych danych[cite: 11]. | Zapisane dane zostały zachowane w pliku `vendo.db`. | **Działa**[cite: 11] |
