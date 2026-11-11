# Architektura MVC w projekcie Vendo (Wersja v1.0.0)

## 1. Podział odpowiedzialności (MVC)
Wersja v1.0.0 aplikacji Vendo została ustrukturyzowana według wzorca architektury MVC (Model-View-Controller) w celu rozdzielenia logiki przetwarzania danych, 
sterowania aplikacją oraz prezentacji interfejsu [cite: 12, 13].

| Warstwa | Odpowiedzialność | Pliki w projekcie |
| :--- | :--- | :--- |
| **Model (M)** | Zarządzanie danymi w bazie SQLite, realizacja zapytań SQL, walidacja reguł biznesowych (np. cena > 0) oraz generowanie propozycji AI. | `models/produkt.py`, `db.py` |
| **Widok (V)** | Szablony HTML (Jinja2) odpowiadające za wyświetlanie danych użytkownikowi, formularze wejściowe oraz komunikaty błędów/sukcesu. | `templates/base.html`, `templates/produkty/w01_magazyn.html`, `w02_nowy_ai.html`, `w03_edycja.html` |
| **Kontroler (C)** | Obsługa tras HTTP (GET/POST), odbieranie parametrów żądań, wywoływanie odpowiednich funkcji z modelu i przekazywanie wyników do widoku lub przekierowań. | `controllers/produkty.py`, `app.py` |

---

## 2. Mapa plików projektu
```text
vendo/
├── controllers/
│   ├── __init__.py
│   └── produkty.py          # Blueprint kontrolera dla tras / i /nowy, /edycja, /usun
├── models/
│   ├── __init__.py
│   └── produkt.py           # Model danych: zapytania SQL, logiki biznesowa i walidacja
├── templates/
│   ├── base.html            # Szablon bazowy ze spójną nawigacją i alertami
│   └── produkty/
│       ├── w01_magazyn.html # Widok listy i filtrowania magazynu (W01)
│       ├── w02_nowy_ai.html # Widok formularza wyliczania treści z AI (W02)
│       └── w03_edycja.html  # Widok edycji i szczegółów przedmiotu (W03)
├── static/
│   └── style.css            # Arkusz stylów CSS
├── docs/
│   ├── roadmap-v1.md
│   ├── technologie.md
│   ├── prompty-v1.md
│   ├── testy-v1.md
│   ├── architektura-mvc.md  # Niniejsza mapa MVC
│   ├── prompty-mvc-v1.0.md  # Rejestr promptów i techniki inżynierii promptów
│   └── testy-v1.0.md       # Rzeczywiste wyniki testów wersji MVP 1.0
├── app.py                   # Plik startowy rejestrujący kontrolery (Blueprint)
├── db.py                    # Moduł połączenia z bazą SQLite i PRAGMA
├── init_db.py               # Inicjalizacja schematu bazy i użytkownika demo nr 1
├── README.md                # Dokumentacja główna i instrukcja uruchomienia v1.0.0
└── requirements.txt
