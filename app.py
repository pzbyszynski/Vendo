import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'vendo_secret_key_dev'
DEMO_USER_ID = 1

def get_db_connection():
    conn = sqlite3.connect('vendo.db')
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# W01: Widok Listy Produktów (Magazyn) - F04
@app.route('/')
def w01_magazyn():
    status_filter = request.args.get('status', 'Wszystkie')
    conn = get_db_connection()
    
    if status_filter == 'Wszystkie':
        query = '''
            SELECT p.*, z.url_zdjecia 
            FROM produkt p 
            LEFT JOIN zdjecie_produktu z ON p.id = z.produkt_id AND z.czy_glowne = 1
            WHERE p.uzytkownik_id = ?
            ORDER BY p.created_at DESC
        '''
        produkty = conn.execute(query, (DEMO_USER_ID,)).fetchall()
    else:
        query = '''
            SELECT p.*, z.url_zdjecia 
            FROM produkt p 
            LEFT JOIN zdjecie_produktu z ON p.id = z.produkt_id AND z.czy_glowne = 1
            WHERE p.uzytkownik_id = ? AND p.status = ?
            ORDER BY p.created_at DESC
        '''
        produkty = conn.execute(query, (DEMO_USER_ID, status_filter)).fetchall()
        
    conn.close()
    return render_template('w01_magazyn.html', produkty=produkty, wybrane_status=status_filter)

# W02: Widok Formularza AI (Nowy Przedmiot) - F01 & F02
@app.route('/nowy', methods=['GET', 'POST'])
def w02_nowy_ai():
    if request.method == 'POST':
        slowo_kluczowe = request.form.get('slowo_kluczowe', '').strip()
        kod_kreskowy = request.form.get('kod_kreskowy', '').strip()
        url_zdjecia = request.form.get('url_zdjecia', '').strip()
        
        # F01: Walidacja danych wejściowych
        if not slowo_kluczowe and not kod_kreskowy and not url_zdjecia:
            flash("Wprowadź słowo kluczowe, kod kreskowy lub adres zdjęcia!", "error")
            return render_template('w02_nowy_ai.html')
        
        # F02: Symulacja generowania treści przez AI na podstawie wprowadzonych danych
        prompt_ref = slowo_kluczowe or kod_kreskowy or "Przedmiot Vintage"
        ai_tytul = f"[AI] {prompt_ref.capitalize()} - Stan Bardzo Dobry"
        ai_opis = f"Automatycznie wygenerowany opis dla przedmiotu '{prompt_ref}'. Świetny stan, brak śladów użytkowania. Idealny do kolekcji."
        ai_cena = 99.00
        
        if not url_zdjecia:
            url_zdjecia = "https://via.placeholder.com/150?text=Produkt+AI"

        # Zapis początkowy (Szkic)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produkt (uzytkownik_id, kod_kreskowy, slowo_kluczowe, ai_tytul, ai_opis, ai_cena, ostateczny_tytul, ostateczny_opis, ostateczna_cena, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Szkic')
        ''', (DEMO_USER_ID, kod_kreskowy, slowo_kluczowe, ai_tytul, ai_opis, ai_cena, ai_tytul, ai_opis, ai_cena))
        
        produkt_id = cursor.lastrowid
        cursor.execute('''
            INSERT INTO zdjecie_produktu (produkt_id, url_zdjecia, czy_glowne)
            VALUES (?, ?, 1)
        ''', (produkt_id, url_zdjecia))
        
        conn.commit()
        conn.close()
        
        flash("AI pomyślnie wygenerowało propozycję oferty! Dostosuj dane i zatwierdź.", "success")
        return redirect(url_url := url_for('w03_edycja', id=produkt_id))
        
    return render_template('w02_nowy_ai.html')

# W03: Widok Edycji i Szczegółów Przedmiotu - F03 & F04
@app.route('/edycja/<int:id>', methods=['GET', 'POST'])
def w03_edycja(id):
    conn = get_db_connection()
    produkt = conn.execute('SELECT * FROM produkt WHERE id = ? AND uzytkownik_id = ?', (id, DEMO_USER_ID)).fetchone()
    
    if not produkt:
        conn.close()
        flash("Brak uprawnień lub produkt nie istnieje.", "error")
        return redirect(url_for('w01_magazyn'))
        
    zdjecie = conn.execute('SELECT url_zdjecia FROM zdjecie_produktu WHERE produkt_id = ? AND czy_glowne = 1', (id,)).fetchone()
    
    if request.method == 'POST':
        ostateczny_tytul = request.form.get('ostateczny_tytul', '').strip()
        ostateczny_opis = request.form.get('ostateczny_opis', '').strip()
        cena_raw = request.form.get('ostateczna_cena', '0')
        status = request.form.get('status', 'Szkic')
        
        # F03: Walidacja po stronie serwera
        try:
            ostateczna_cena = float(cena_raw)
        except ValueError:
            ostateczna_cena = -1.0
            
        if not ostateczny_tytul or not ostateczny_opis:
            flash("Tytuł i opis nie mogą być puste!", "error")
            conn.close()
            return render_template('w03_edycja.html', produkt=produkt, zdjecie=zdjecie)
            
        if ostateczna_cena <= 0:
            flash("Cena musi być wartością wyższą niż 0 PLN!", "error")
            conn.close()
            return render_template('w03_edycja.html', produkt=produkt, zdjecie=zdjecie)
            
        # Zapis po edycji
        conn.execute('''
            UPDATE produkt 
            SET ostateczny_tytul = ?, ostateczny_opis = ?, ostateczna_cena = ?, status = ?
            WHERE id = ? AND uzytkownik_id = ?
        ''', (ostateczny_tytul, ostateczny_opis, ostateczna_cena, status, id, DEMO_USER_ID))
        
        conn.commit()
        conn.close()
        flash("Zapisano pomyślnie zmiany w produkcie.", "success")
        return redirect(url_for('w01_magazyn'))

    conn.close()
    return render_template('w03_edycja.html', produkt=produkt, zdjecie=zdjecie)

# Usuwanie produktu (F04)
@app.route('/usun/<int:id>', methods=['POST'])
def usun_produkt(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM produkt WHERE id = ? AND uzytkownik_id = ?', (id, DEMO_USER_ID))
    conn.commit()
    conn.close()
    flash("Produkt został usunięty.", "success")
    return redirect(url_for('w01_magazyn'))

if __name__ == '__main__':
    app.run(debug=True)
