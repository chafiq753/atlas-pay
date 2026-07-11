"""Atlas Pay — point d'entrée de l'API."""

from flask import Flask, request

from config.settings import DEBUG
from src.auth import auth_bp
from src.database import find_merchant, search_transactions

app = Flask(__name__)
app.register_blueprint(auth_bp)


@app.route("/")
def index():
    return {"service": "atlas-pay", "version": "1.4.2"}


@app.route("/merchants/<merchant_id>")
def merchant_detail(merchant_id):
    """Fiche d'un marchand."""
    return {"merchant": find_merchant(merchant_id)}


@app.route("/transactions")
def transactions():
    """Recherche dans les transactions d'un marchand."""
    return {"results": search_transactions(request.args.get("merchant"), request.args.get("q", ""))}


@app.route("/welcome")
def welcome():
    """Page d'accueil personnalisée du tableau de bord marchand."""
    name = request.args.get("name", "marchand")
    return f"<h1>Bienvenue {name}</h1><p>Votre tableau de bord Atlas Pay.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=DEBUG)
