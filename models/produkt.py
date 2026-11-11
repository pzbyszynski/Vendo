from db import get_db_connection

def pobierz_produkty(uzytkownik_id=1, status_filter='Wszystkie'):
    """Pobiera listę produktów użytkownika wraz ze zdjęciem głównym."""
    conn = get_db_connection()
    if status_filter == 'Wszystkie':
        query = '''
            SELECT p.*, z.url_zdjecia 
            FROM produkt p 
            LEFT JOIN zdjecie_produktu z ON p.id = z.produkt_id AND z.czy_glowne = 1
            WHERE p.uzytkownik_id = ?
            ORDER BY p.created_at DESC
        '''
        produkty = conn.execute(query, (uzytkownik_id,)).fetchall()
    else:
        query = '''
            SELECT p.*, z.url_zdjecia 
            FROM produkt p 
            LEFT JOIN zdjecie_produktu z ON p.id = z.produkt_id AND z.czy_glowne = 1
            WHERE p.uzytkownik_id = ? AND p.status = ?
            ORDER BY p.created_at DESC
        '''
        produkty = conn.execute(query, (uzytkownik_id, status_filter)).fetchall()
    conn.close()
    return produkty

def pobierz_produkt_po_id(produkt_id, uzytkownik_id=1):
    """Pobiera pojedynczy produkt oraz jego zdjęcie główne."""
    conn = get_db_connection()
    produkt = conn.execute('SELECT * FROM produkt WHERE id = ? AND uzytkownik_id = ?', (produkt_id, uzytkownik_id)).fetchone()
    zdjecie = None
    if produkt:
        zdjecie = conn.execute('SELECT url_zdjecia FROM zdjecie_produktu WHERE produkt_id = ? AND czy_glowne = 1', (produkt_id,)).fetchone()
    conn.close()
    return produkt, zdjecie

def utworz_produkt_szkic_ai(uzytkownik_id, slowo_kluczowe, kod_kreskowy, url_zdjecia):
    """Generuje propozycję AI i zapisuje przedmiot jako Szkic w bazie danych (F01, F02)."""
    prompt_ref = slowo_kluczowe or kod_kreskowy or "Przedmiot Vintage"
    ai_tytul = f"[AI] {prompt_ref.capitalize()} - Stan Bardzo Dobry"
    ai_opis = f"Automatycznie wygenerowany opis dla przedmiotu '{prompt_ref}'. Stan idealny, brak śladów użytkowania."
    ai_cena = 99.00
    
    if not url_zdjecia:
        url_zdjecia = "https://via.placeholder.com/150?text=Produkt+AI"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produkt (uzytkownik_id, kod_kreskowy, slowo_kluczowe, ai_tytul, ai_opis, ai_cena, ostateczny_tytul, ostateczny_opis, ostateczna_cena, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Szkic')
    ''', (uzytkownik_id, kod_kreskowy, slowo_kluczowe, ai_tytul, ai_opis, ai_cena, ai_tytul, ai_opis, ai_cena))
    
    produkt_id = cursor.lastrowid
    cursor.execute('''
        INSERT INTO zdjecie_produktu (produkt_id, url_zdjecia, czy_glowne)
        VALUES (?, ?, 1)
    ''', (produkt_id, url_zdjecia))
    
    conn.commit()
    conn.close()
    return produkt_id

def zaktualizuj_produkt(produkt_id, uzytkownik_id, ostateczny_tytul, ostateczny_opis, ostateczna_cena, status):
    """Waliduje dane biznesowe i aktualizuje produkt w bazie (F03)."""
    if not ostateczny_tytul or not ostateczny_opis:
        return False, "Tytuł i opis nie mogą być puste!"
        
    try:
        cena_val = float(ostateczna_cena)
    except (ValueError, TypeError):
        return False, "Cena musi być poprawną liczbą!"

    if cena_val <= 0:
        return False, "Cena musi być wartością wyższą niż 0 PLN!"

    conn = get_db_connection()
    conn.execute('''
        UPDATE produkt 
        SET ostateczny_tytul = ?, ostateczny_opis = ?, ostateczna_cena = ?, status = ?
        WHERE id = ? AND uzytkownik_id = ?
    ''', (ostateczny_tytul, ostateczny_opis, cena_val, status, produkt_id, uzytkownik_id))
    conn.commit()
    conn.close()
    return True, "Zapisano pomyślnie zmiany w produkcie."

def usun_produkt(produkt_id, uzytkownik_id=1):
    """Usuwa produkt z bazy danych (F04)."""
    conn = get_db_connection()
    conn.execute('DELETE FROM produkt WHERE id = ? AND uzytkownik_id = ?', (produkt_id, uzytkownik_id))
    conn.commit()
    conn.close()
    return True
