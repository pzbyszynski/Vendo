import sqlite3

def init_db():
    conn = sqlite3.connect('vendo.db')
    cursor = conn.cursor()
    
    # Włączenie sprawdzania kluczy obcych
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Tabela: Uzytkownik
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uzytkownik (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            haslo_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    
    # Tabela: Produkt
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produkt (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uzytkownik_id INTEGER NOT NULL,
            kod_kreskowy TEXT,
            slowo_kluczowe TEXT,
            ai_tytul TEXT,
            ai_opis TEXT,
            ai_cena REAL,
            ostateczny_tytul TEXT NOT NULL,
            ostateczny_opis TEXT NOT NULL,
            ostateczna_cena REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Szkic',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik (id) ON DELETE CASCADE
        );
    ''')
    
    # Tabela: Zdjecie_Produktu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS zdjecie_produktu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produkt_id INTEGER NOT NULL,
            url_zdjecia TEXT NOT NULL,
            czy_glowne INTEGER DEFAULT 0,
            FOREIGN KEY (produkt_id) REFERENCES produkt (id) ON DELETE CASCADE
        );
    ''')
    
    # Utworzenie konta demo nr 1 (jeśli nie istnieje)
    cursor.execute("SELECT id FROM uzytkownik WHERE id = 1;")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO uzytkownik (id, email, haslo_hash) VALUES (1, 'jan.demo@vendo.pl', 'demo_hash_123');"
        )
        print("Utworzona użytkownika demo o ID = 1.")
        
        # Przykładowe dane startowe dla demo
        cursor.execute('''
            INSERT INTO produkt (uzytkownik_id, kod_kreskowy, slowo_kluczowe, ai_tytul, ai_opis, ai_cena, ostateczny_tytul, ostateczny_opis, ostateczna_cena, status)
            VALUES (1, '5901234567890', 'Kurtka Nike', 'Kurtka sportowa Nike Vintage M', 'Czarna kurtka wiatrówka w stanie idealnym.', 149.99, 'Kurtka sportowa Nike Vintage M', 'Czarna kurtka wiatrówka w stanie idealnym.', 149.99, 'Aktywny');
        ''')
        prod_id = cursor.lastrowid
        cursor.execute('''
            INSERT INTO zdjecie_produktu (produkt_id, url_zdjecia, czy_glowne)
            VALUES (?, 'https://via.placeholder.com/150?text=Kurtka+Nike', 1);
        ''', (prod_id,))
    
    conn.commit()
    conn.close()
    print("Baza danych vendo.db została pomyślnie zinicjalizowana.")

if __name__ == '__main__':
    init_db()
