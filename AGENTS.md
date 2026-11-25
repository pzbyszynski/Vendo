# Instrukcje dla agentów kodowania – Projekt Vendo

## Projekt i granice zmian
* **Stos technologiczny:** Python 3, Flask (Blueprints), SQLite (`sqlite3`), HTML5/CSS3 (Jinja2).
* **Architektura:** Zachowuj ścisły podział MVC:
  * Reguły biznesowe, walidację danych i zapytania SQL umieszczaj wyłącznie w warstwie Modelu (`models/produkt.py`).
  * Obsługę żądań HTTP (GET/POST), odczyt formularzy i przekierowania umieszczaj w Kontrolerze (`controllers/produkty.py`).
  * Prezentację danych i komunikatów umieszczaj w Widokach (`templates/produkty/`).
