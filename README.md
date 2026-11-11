# Vendo (Polski asystent resellingu i zarządzania multi-listingiem)
Aplikacja, dzięki której użytkownik robi zdjęcie przedmiotu, który chce wystawić na sprzedarz.
Wystarczy zrobić zdjęcie przedmiotu, zeskanować kod kreskowy lub wpisać słowo kluczowe, a AI wygeneruje tytuł, opis oraz sugerowaną cenę.
Aplikacja sugeruje użytkownikowi cenę za wystawiany produkt, ale co do ceny - użytkownik wystawia ją ostatecznie samemu.
Narzędzia do tworzenia etykiet wysyłkowych oraz organizowania odbiorów.
## Wersja v1.0.0 (Architektura MVC)
Projekt został w pełni zrefaktoryzowany do wzorca **MVC (Model-View-Controller)** przy użyciu technologii Python 3, Flask (Blueprints) oraz relacyjnej bazy SQLite[cite: 12, 13].
# Zespół Vendo: 
Członek 1: Paweł Zbyszyński, nr indeksu: 180651, grupa: IO2 , GitHub: @pzbyszynski   
Członek 2: Maciej Wojciechowski, nr indeksu: 180647, grupa: IO2, GitHub: @ELLVO3
# Użytkownicy i scenariusz
## Główna grupa odbiorców: 
Drobni sprzedawcy internetowi, osoby handlujące odzieżą używaną/retro (resellerzy) oraz prywatni użytkownicy wyprzedający rzeczy z własnego domu.   
## Scenariusz użycia:
1. Użytkownik otwiera aplikację Vendo i robi zdjęcie używanej kurtki lub skanuje jej kod kreskowy z metki.   
2. Moduł AI analizuje zdjęcie/kod, sugerując tytuł: "Kurtka zimowa z kapturem M", opis z właściwościami materiału oraz sugerowaną cenę: 120 PLN.
3. Użytkownik weryfikuje dane, zmienia cenę na własną (130 PLN) i zatwierdza formularz.   
4. Przedmiot zostaje zapisany w centralnym magazynie Vendo ze stanem "Gotowy do wystawienia".
5. Po dokonaniu sprzedaży użytkownik przechodzi do zakładki przesyłek, generuje etykietę wysyłkową PDF i zamawia kuriera po odbiór paczki z domu.
# Zakres funkcjonalny:
| ID | Funkcjonalność | Zakres |
| :--- | :--- | :---: |
| **F01** | Użytkownik może wykonać zdjęcie przedmiotu, wprowadzić słowo kluczowe lub zeskanować kod kreskowy. | `MVP` |
| **F02** | Użytkownik może wygenerować za pomocą AI sugerowany tytuł, opis oraz proponowaną cenę przedmiotu. | `MVP` |
| **F03** | Użytkownik może edytować i zatwierdzić ostateczny tytuł, opis oraz cenę sprzedawanego produktu. | `MVP` |
| **F04** | Użytkownik może zarządzać bazą swoich produktów (dodawać, edytować, usuwać i zmieniać statusy: Szkic, Wystawiony, Sprzedany). | `MVP` |
| **F05** | Użytkownik może generować etykiety wysyłkowe dla sprzedanych przedmiotów. | `Rozszerzenie` |
| **F06** | Użytkownik może planować i organizować odbiór przesyłek przez kuriera. | `Rozszerzenie` |
| **F07** | Użytkownik może przeglądać podsumowanie i analitykę zysków ze sprzedaży w podziale na platformy. | `Rozszerzenie` |
# Poza zakresem pierwszej wersji
Bezpośrednia, automatyczna integracja przez oficjalne API serwisów Vinted/OLX (ze względu na ograniczenia prawne i brak publicznych interfejsów). 
Wbudowany moduł płatności elektronicznych pomiędzy kupującym a sprzedającym (aplikacja skupia się na zarządzaniu i logistyce).
# Organizacja współpracy 
## Podział zadań:
(Są w trakcie ustaleń)
## Kanal komunikacji: 
Discord / Messenger oraz wbudowany komunikator w serwisie LaboChat.com.   
## Zasady aktualizacji: 
Wszystkie kluczowe decyzje architektoniczne i zmiany w zakresie funkcjonalnym są odnotowywane w pliku README.md oraz w przestrzeni zespołu na LaboChat.com. Ogniwem kontroli zmian są pull requesty w repozytorium GitHub.   
# Odnośniki
### Repozytorium GitHub:
 https://github.com/pzbyszynski/Vendo
### Roadmapa v1:
 [Dokumentacja Road Map v1](docs/roadmap-v1.md)
## Uruchomienie lokalne aplikacji (Wersja v1)

### 1. Wymagania
* Python 3.10 lub nowszy [cite: 9].

### 2. Instalacja i start (Windows PowerShell) [cite: 9]
```powershell

# 1. Uruchom Windows PowerShell jako administrator i wpisz komendę
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Po wpisaniu zatwierdź zmianę, wpisując Y (lub T w polskiej wersji) i naciskając Enter. Następnie spróbuj aktywować środowisko:

# 2. Utwórz i aktywuj środowisko wirtualne
py -3 -m venv .venv
.\.venv\Scripts\activate

# 3. Wpisz komendę
cd ... (Ścieżka do folderu z aplikacją Vendo-main) 

# 4. Zainstaluj wymagane pakiety
pip install -r requirements.txt

# 5. Zinicjalizuj bazę danych (tworzy użytkownika demo nr 1)
python init_db.py

# 6. Uruchom serwer aplikacji
python app.py
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:5000 [cite: 9].
