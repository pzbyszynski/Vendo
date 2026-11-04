# Rejestr promptów AI i poprawek – Iteracja v1

* **Użyty czat AI:** Google Gemini (Plan bezpłatny)[cite: 8].
* **Data wykonania:** 2026-11-04[cite: 8].

## 1. Prompt P1 – Generowanie stosu technologicznego
> **Treść promptu:** Pracujemy we dwoje nad projektem Vendo. Cel v1: Stworzenie funkcjonalnego MVP pozwalającego na wprowadzanie produktów, generowanie treści z AI oraz trwałe zapisywanie w magazynie. Widoki: W01 Lista produktów, W02 Formularz AI, W03 Edycja i Szczegóły. Dane: uzytkownik, produkt, zdjecie_produktu. Zaproponuj prosty zestaw technologii bez płatnych usług i przygotuj plan.[cite: 9]

* **Decyzja zespołu:** Wybrano proponowany zestaw Python 3 + Flask + SQLite[cite: 8, 9]. Uznano go za najprostszy do uruchomienia lokalnie[cite: 8, 9].

---

## 2. Prompt P2 – Generowanie struktury bazy danych i aplikacji Flask[cite: 9, 10]
> **Treść promptu:** Przygotuj skrypt `init_db.py` w SQLite oraz główny plik `app.py` obsługujący widoki W01, W02 i W03 dla użytkownika demo nr 1. Zastosuj zapytania parametryzowane, włącz klucze obce PRAGMA i dodaj pełne szablony HTML Jinja2 z obsługą komunikatów błędów.[cite: 10]

---

## 3. Własne poprawki zespołu (Weryfikacja wygenerowanego kodu)
1. **Błąd w walidacji formularza edycji (W03):** Początkowy kod AI akceptował ujemną cenę przedmiotu. Zespół dodał własny warunek w `app.py`: `if ostateczna_cena <= 0: flash("Cena musi być wartością wyższą niż 0 PLN!", "error")`.
2. **Klucze obce SQLite:** AI zapomniało o wymuszeniu sprawdzania relacji w połączeniu. Zespół dodał komendę `conn.execute("PRAGMA foreign_keys = ON;")` w funkcji `get_db_connection()`.
