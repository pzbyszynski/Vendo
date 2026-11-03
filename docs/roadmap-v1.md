#Plan i Architektura Projektu Vendo – Iteracja v1 (MVP)
## 1. Cel i granice wersji v1

* Tytuł projektu: Vendo – Polski asystent resellingu i zarządzania multi-listingiem.  
* Główny odbiorca: Drobni sprzedawcy internetowi, osoby handlujące odzieżą używaną oraz prywatni użytkownicy wyprzedający rzeczy z własnej szafy.  
* Najważniejszy cel v1: Stworzenie funkcjonalnego MVP umożliwiającego dodanie przedmiotu na podstawie zdjęcia/kodu kreskowego, automatyczną generację treści przez AI oraz zarządzanie lokalnym magazynem produktów.  
* Opis efektu dla użytkownika: W wersji v1 użytkownik może błyskawicznie wprowadzić nowy przedmiot do systemu, uzyskując automatyczne propozycje tytułu, opisu oraz wyceny rynkowej przygotowane przez model AI. Sprzedawca ma możliwość swobodnego dostosowania tych danych, ustalenia ostatecznej ceny i zapisania produktu w centralnym magazynie ze wskazanym statusem. System eliminuję potrzebę ręcznego wymyślania opisów od zera, skracając czas przygotowania oferty do kilkunastu sekund.  

* Funkcje wybrane do MVP (v1): 
   * F01 – Wprowadzanie danych przedmiotu (zdjęcie, słowo kluczowe, kod kreskowy).  
   * F02 – AI-Asystent: generowanie sugerowanego tytułu, opisu i ceny.  
   * F03 – Edycja i zatwierdzanie ostatecznych danych produktu przez użytkownika.  
   * F04 – Zarządzanie bazą produktów (dodawanie, edycja, zmiana statusu: Szkic, Aktywny, Sprzedany).  
* Funkcje odłożone do iteracji v2: 
   * F05 – Generowanie etykiet wysyłkowych.  
   * F06 – Zamawianie i organizacja odbiorów kurierskich.  
   * F07 – Analityka zysków ze sprzedaży. 
Tworzy folder docs/ i dodaje plik roadmap-v1.md z sekcjami: 1. Cel i granice, 2. Projekt widoków, 5. Tabela Mapy Prac v1.

# Projekt widoków (UI / UX)
## Zestawienie widoków v1
| ID | Nazwa Widoku | Użytkownik | Cel i Przeznaczenie |
| :--- | :--- | :--- | :--- |
| **W01** | Lista produktów (Magazyn) | Sprzedawca | Przeglądanie zapisanych produktów, filtrowanie po statusie (*Szkic*, *Aktywny*, *Sprzedany*) oraz nawigacja do dodawania nowego przedmiotu. |
| **W02** | Formularz AI (Nowy przedmiot) | Sprzedawca | Wgrywanie zdjęcia, wpisywanie kodu/słowa kluczowego, wywołanie AI i podgląd wygenerowanych sugestii. |
| **W03** | Edycja i Szczegóły przedmiotu | Sprzedawca | Modyfikacja ostatecznego tytułu, opisu, ceny, edycja statusu oraz usuwanie produktu. |

## Opis i układ widoków
## W01: Lista produktów (Magazyn)
* Odbiorca: Zalogowany użytkownik.  
* Elementy UI: Nagłówek aplikacji, przycisk nawigacyjny + Dodaj przedmiot, pasek wyszukiwania, filtry statusów (Wszystkie, Szkic, Aktywny, Sprzedany), siatka/lista kart produktów (miniaturka zdjęcia, ostateczny tytuł, cena, badge statusu).  
* Prezentowane dane: Miniaturka (url_zdjecia), ostateczny_tytul, ostateczna_cena, status.
* Komunikaty: 
   *Sukces: Wyświetlenie listy załadowanych produktów.  
   *Brak danych: "Brak produktów w magazynie. Kliknij + Dodaj przedmiot, aby stworzyć pierwsze ogłoszenie."  
## W02: Formularz AI (Nowy przedmiot) 
* Odbiorca: Zalogowany użytkownik.  
* Elementy UI: Przycisk powrotu, sekcja uploadu pliku (zdjęcie), pole tekstowe Kod kreskowy / Słowo kluczowe, przycisk Generuj z AI, wskaźnik ładowania (loading spinner), podgląd sugestii AI.  
* Dane wprowadzane/wyświetlane:
   * Input: Plik zdjęcia, kod_kreskowy, slowo_kluczowe.  
   * Output: ai_tytul, ai_opis, ai_cena.  
* Komunikaty: 
   * Błąd: "Nie udało się przeanalizować zdjęcia. Upewnij się, że plik jest poprawny lub wpisz słowo kluczowe ręcznie."  
   * Sukces: "AI pomyślnie wygenerowało propozycję oferty!" -> automatyczne przejście do edycji w W03.  
## W03: Edycja i Szczegóły przedmiotu 
* Odbiorca: Zalogowany użytkownik.  
* Elementy UI: Formularz z polami edycyjnymi (Tytuł, Opis, Cena), rozwijana lista wyboru Status, sekcja zdjęć z oznaczeniem zdjęcia głównego, przycisk Zapisz w magazynie, przycisk Usuń.  
* Dane wprowadzane/wyświetlane: ostateczny_tytul, ostateczny_opis, ostateczna_cena, status.  
* Komunikaty: 
   * Błąd walidacji: "Cena musi być wartością dodatnią wyższą niż 0 PLN."  
   * Sukces: "Zmieniono dane produktu." -> powrót do W01 
## Mapa nawigacji i przepływu
```text
## Mapa nawigacji i przepływu

[ W01: Lista produktów ]
   │
   ├── (Kliknięcie "+ Dodaj przedmiot") ────> [ W02: Formularz AI ]
   │                                                 │
   │                                           (Przetworzenie przez AI)
   │                                                 │
   │                                                 ▼
   └── (Kliknięcie na produkt z listy) ─────> [ W03: Edycja i Szczegóły ]
                                                     │
                                           (Zapis zmian / Zmiana statusu)
                                                     │
                                                     ▼
                                            [ W01: Lista produktów ]
```

# Opis Funkcjonalności MVP (v1)
* F01: Wprowadzanie danych przedmiotu
    * Użytkownik: Zalogowany sprzedawca.
    * Oczekiwane działanie: Użytkownik w widoku `W02` załącza plik ze zdjęciem przedmiotu i opcjonalnie uzupełnia pole kodu kreskowego lub słowa kluczowego.
    * Powiązany widok: `W02`.
    * Potrzebne dane: Plik zdjęcia, `kod_kreskowy`, `slowo_kluczowe`.
    * Warunek poprawności: Dodano przynajmniej jeden plik graficzny LUB wpisano wartość w polu kodu/słowa kluczowego.
    * Sytuacja błędna: Brak załączonego zdjęcia oraz puste pole tekstowe. System blokuje wysłanie formularza i podświetla wymagane pola na czerwono.

* F02: Generowanie sugerowanych treści i wyceny przez AI
    * Użytkownik: Zalogowany sprzedawca.
    * Oczekiwane działanie: System przesyła wprowadzone dane z `W02` do zewnętrznego modelu AI, który generuje proponowany tytuł, wyczerpujący opis oraz sugerowaną cenę rynkową przedmiotu.
    * Powiązane widoki: `W02` -> `W03`.
    * Potrzebne dane: Zdjęcie/kod/słowo kluczowe z `F01`, odpowiedź z API (zapis do `ai_tytul`, `ai_opis`, `ai_cena`).
    * Warunek poprawności: Moduł AI zwraca komplet danych w formacie JSON, a aplikacja przekazuje wygenerowane propozycje do pól formularza edycji w `W03`.
    * Sytuacja błędna: Przekroczenie limitu czasu odpowiedzi API (timeout) lub brak możliwości sklasyfikowania zdjęcia przez AI. System wkleja opisy domyślne ("Do uzupełnienia") i informuje użytkownika komunikatem: "Nie udało się wygenerować opisu. Uzupełnij dane ręcznie."

* F03: Edycja i zatwierdzenie finalnych danych produktu
    * Użytkownik: Zalogowany sprzedawca.
    * Oczekiwane działanie: W widoku `W03` użytkownik modyfikuje wygenerowany tytuł, opis i ustawia własną cenę ostateczną, a następnie zapisuje produkt.
    * Powiązany widok: `W03`.
    * Potrzebne dane: `ostateczny_tytul`, `ostateczny_opis`, `ostateczna_cena`, `status`.
    * Warunek poprawności: Zapisanie rekordu w tabeli `Produkt` oraz relacyjnych wpisów w `Zdjecie_Produktu`.
    * Sytuacja błędna: Użytkownik podaje ujemną cenę lub pozostawia puste pole ostatecznego tytułu. System odrzuca formularz z walidacją błędu.

* F04: Zarządzanie bazą produktów (Magazyn)
    * Użytkownik: Zalogowany sprzedawca.
    * Oczekiwane działanie: Przeglądanie listy produktów w W01, filtrowanie ich po statusie oraz zmiana stanu przedmiotu (np. z Aktywny na Sprzedany).
    * Powiązane widoki: `W01`, `W03`.
    * Potrzebne dane: Rekordy z tabeli `Produkt` powiązane z `kluczem uzytkownik_id`.
    * Warunek poprawności: Prawidłowa zmiana pola `status` w bazie danych oraz natychmiastowa zmiana oznaczenia wizualnego na karcie przedmiotu w `W01`.
    * Sytuacja błędna: Próba edycji lub usunięcia przedmiotu należącego do innego użytkownika (brak uprawnień) – system zwraca błąd dostępu.

# Tabela Mapy Prac v1
| Etap v1 | Zadanie | Odpowiedzialny | Zależność | Oczekiwany rezultat |
| :--- | :--- | :--- | :--- | :--- |
| **Cel i zakres** | Doprecyzowanie zakresu MVP i podziału ról | Paweł i Maciej | Lab 01 | Zatwierdzony cel v1 i usunięcie zbędnych funkcji z MVP. |
| **1. Widoki** | Przygotowanie szkiców makiety dla W01, W02, W03 | Paweł i Maciej | Cel i zakres | Pliki graficzne/szkice w folderze `docs/mockups/`. |
| **2. Struktura Bazy** | Utworzenie skryptu SQL / migracji bazy danych | Paweł i Maciej | Widoki | Działające tabele `Uzytkownik`, `Produkt`, `Zdjecie_Produktu`. |
| **3. Funkcjonalności** | Implementacja API i serwisu integracji z AI | Paweł i Maciej | Struktura Bazy | Działające wywołanie AI dla opisu i wyceny (F02). |
| **3. Funkcjonalności** | Budowa widoków frontendowych oraz formularza edycji | Paweł i Maciej| Widoki i Baza | Podpięty interfejs dla W01, W02 i W03 (F01, F03, F04). |
| **Sprawdzenie** | Testy integracyjne przepływu danych od zdjęcia do zapisu | Paweł i Maciej | Wszystkie etapy | Kompletne, przetestowane MVP v1 bez krytycznych błędów. |

# Kierunek kolejnej iteracji – v2

* Pomysł 1: Etykiety wysyłkowe (F05)
    * Uzasadnienie: Po sprzedaniu przedmiotu użytkownik chce szybko wygenerować etykietę kurierską z poziomu aplikacji bez konieczności przechodzenia na strony przewoźników.
    * Wpływ na Widoki: W widoku `W03` (oraz na liście w `W01`) przy produktach o statusie Sprzedany pojawi się przycisk `Generuj etykietę PDF`.
    * Wpływ na Baza danych: Utworzenie nowej tabeli Przesylka (`id`, `produkt_id`, `kurier`, `numer_nadania`, `etykieta_url`, `status`).
    * Wpływ na Funkcjonalności: Integracja z API przewoźnika (np. InPost/DPD API) i pobieranie pliku PDF etykiety.

* Pomysł 2: Organizacja odbioru przesyłek (F06)
    * Uzasadnienie: Umożliwienie zamówienia podjazdu kuriera po paczkę bezpośrednio z domu sprzedawcy.
    * Wpływ na Widoki: Dodanie nowego widoku `W04: Zamów kuriera` z wyborem daty i okna godzinowego odbioru paczek.
    * Wpływ na Baza danych: Rozbudowa tabeli Przesylka o pola `data_odbioru` oraz `uwagi_dla_kuriera`.
    * Wpływ na Funkcjonalności: Wysłanie zlecenia podjazdu kuriera przez API zewnętrznego brokera kurierskiego.
