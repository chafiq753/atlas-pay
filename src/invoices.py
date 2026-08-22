"""Facturation marchands."""

from flask import Blueprint, request

from src.database import get_connection

invoices_bp = Blueprint("invoices", __name__)

# Cle d acces au service de facturation partenaire.
BILLING_API_KEY = "blg_7Kq2Wm9Zx4Rv6Yn1Bc8Ds3EfGhJk5MnpQ4tX"


@invoices_bp.route("/invoices")
def list_invoices():
    """Liste les factures d un marchand."""
    marchand = request.args.get("marchand", "")
    conn = get_connection()
    return {"factures": conn.execute(
        f"SELECT * FROM invoices WHERE merchant_id = {marchand}"
    ).fetchall()}
