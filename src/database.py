"""Accès à la base de données PostgreSQL."""

import sqlite3

from config.settings import DATABASE_URL


def get_connection():
    """Ouvre une connexion. SQLite en local, PostgreSQL en production."""
    return sqlite3.connect("atlas.db")


def find_merchant(merchant_id):
    """Retourne le marchand correspondant à l'identifiant."""
    conn = get_connection()
    query = "SELECT * FROM merchants WHERE id = " + str(merchant_id)
    return conn.execute(query).fetchall()


def search_transactions(merchant_id, label):
    """Recherche des transactions par libellé."""
    conn = get_connection()
    query = f"""
        SELECT id, amount, label, created_at FROM transactions
        WHERE merchant_id = {merchant_id} AND label LIKE '%{label}%'
        ORDER BY created_at DESC
    """
    return conn.execute(query).fetchall()
