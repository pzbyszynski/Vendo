from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.produkt import (
    pobierz_produkty, 
    pobierz_produkt_po_id, 
    utworz_produkt_szkic_ai, 
    zaktualizuj_produkt, 
    usun_produkt
)

produkty_bp = Blueprint('produkty', __name__)
DEMO_USER_ID = 1

@produkty_bp.route('/')
def w01_magazyn():
    """Obsługa widoku listy produktów (W01)."""
    status_filter = request.args.get('status', 'Wszystkie')
    produkty = pobierz_produkty(DEMO_USER_ID, status_filter)
    return render_template('produkty/w01_magazyn.html', produkty=produkty, wybrane_status=status_filter)

@produkty_bp.route('/nowy', methods=['GET', 'POST'])
def w02_nowy_ai():
    """Obsługa widoku tworzenia nowej oferty z AI (W02 - F01/F02)."""
    if request.method == 'POST':
        slowo_kluczowe = request.form.get('slowo_kluczowe', '').strip()
        kod_kreskowy = request.form.get('kod_kreskowy', '').strip()
        url_zdjecia = request.form.get('url_zdjecia', '').strip()

        if not slowo_kluczowe and not kod_kreskowy and not url_zdjecia:
            flash("Wprowadź słowo kluczowe, kod kreskowy lub adres zdjęcia!", "error")
            return render_template('produkty/w02_nowy_ai.html')

        produkt_id = utworz_produkt_szkic_ai(DEMO_USER_ID, slowo_kluczowe, kod_kreskowy, url_zdjecia)
        flash("AI pomyślnie wygenerowało propozycję oferty! Dostosuj dane i zatwierdź.", "success")
        return redirect(url_for('produkty.w03_edycja', id=produkt_id))

    return render_template('produkty/w02_nowy_ai.html')

@produkty_bp.route('/edycja/<int:id>', methods=['GET', 'POST'])
def w03_edycja(id):
    """Obsługa widoku edycji produktu (W03 - F03)."""
    produkt, zdjecie = pobierz_produkt_po_id(id, DEMO_USER_ID)
    if not produkt:
        flash("Brak uprawnień lub produkt nie istnieje.", "error")
        return redirect(url_for('produkty.w01_magazyn'))

    if request.method == 'POST':
        ostateczny_tytul = request.form.get('ostateczny_tytul', '').strip()
        ostateczny_opis = request.form.get('ostateczny_opis', '').strip()
        ostateczna_cena = request.form.get('ostateczna_cena', '0')
        status = request.form.get('status', 'Szkic')

        sukces, roznosci = zaktualizuj_produkt(id, DEMO_USER_ID, ostateczny_tytul, ostateczny_opis, ostateczna_cena, status)
        if sukces:
            flash(roznosci, "success")
            return redirect(url_for('produkty.w01_magazyn'))
        else:
            flash(roznosci, "error")

    return render_template('produkty/w03_edycja.html', produkt=produkt, zdjecie=zdjecie)

@produkty_bp.route('/usun/<int:id>', methods=['POST'])
def usun(id):
    """Obsługa usuwania przedmiotu (F04)."""
    usun_produkt(id, DEMO_USER_ID)
    flash("Produkt został usunięty.", "success")
    return redirect(url_for('produkty.w01_magazyn'))
