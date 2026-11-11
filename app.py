from flask import Flask
from controllers.produkty import produkty_bp

app = Flask(__name__)
app.secret_key = 'vendo_secret_key_mvc_v1_0'

# Rejestracja kontrolera
app.register_blueprint(produkty_bp)

if __name__ == '__main__':
    app.run(debug=True)
