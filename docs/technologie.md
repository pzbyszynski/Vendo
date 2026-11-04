# Wybór i rola technologii w projekcie Vendo (v1)

## Opis wybranego stosu technologicznego
Dla pierwszej wersji aplikacji Vendo (MVP) wybrano zestaw technologii oparty na języku Python 3, mikroframeworku Flask oraz relacyjnej bazie danych SQLite. Warstwa prezentacji (widoki W01-W03) została zrealizowana przy użyciu HTML5, czystego arkusza stylów CSS oraz silnika szablonów Jinja2. Logika serwerowa opiera się na Flasku, co pozwala na szybką obsługę tras HTTP, walidację danych formularzy i komunikację z bazą. Jako trwały magazyn danych wykorzystano wbudowany w Pythona moduł `sqlite3`, który zapisuje dane w lokalnym pliku `vendo.db`. Wybór ten gwarantuje natychmiastowe uruchomienie aplikacji na dowolnym systemie (Windows/macOS/Linux) bez konieczności instalowania zewnętrznych serwerów bazodanowych czy płatnych usług w chmurze. 

## Zestawienie ról i wersji narzędzi

| Obszar | Wybrane narzędzie / technologia | Wersja | Rola w projekcie Vendo |
| :--- | :--- | :--- | :--- |
| **Widoki (Frontend)** | HTML5, CSS3, Jinja2 | HTML5 / Standard | Wyświetlanie listy produktów, formularza AI oraz widoku edycji ze spójnym układem wizualnym. |
| **Serwer (Backend)** | Python 3 + Flask | Python 3.10+, Flask 3.0+ | Obsługa żądań HTTP, logika biznesowa generowania sugestii AI (mock/API) oraz walidacja. |
| **Baza danych** | SQLite (moduł `sqlite3`) | SQLite 3 | Trwałe przechowywanie użytkowników, produktów i zdjęć w lokalnym pliku `vendo.db`. |
| **Praca zespołu** | VS Code, Git, GitHub | Aktualne | Edycja kodu, kontrola wersji i rejestracja historii zmian przez obu członków zespołu. |

## Uzasadnienie wyboru
Zestaw Python + Flask + SQLite zapewnia optymalny stosunek prostoty implementacji do możliwości spełnienia wszystkich wymogów funkcjonalnych MVP (F01–F04). Pozwala uniknąć skomplikowanej konfiguracji środowiska, skupiając się na przejrzystym podziale na widoki, logikę serwerową oraz bazę danych. SQLite idealnie wpisuje się w wymóg trwałości danych po restarcie serwera przy zerowym koszcie utrzymania.
