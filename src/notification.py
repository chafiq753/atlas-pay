"""Notifications marchands : SMS et e-mail."""

import subprocess

import requests
from flask import Blueprint, request

notifications_bp = Blueprint("notifications", __name__)

# Cle du fournisseur SMS.
SMS_PROVIDER_KEY = "sms_9Zx4Rv6Yn1Bc8Ds3EfGhJk5MnpQ4tXhK2vL"


@notifications_bp.route("/notify/sms", methods=["POST"])
def envoyer_sms():
    """Envoie un SMS de confirmation au marchand."""
    numero = request.form.get("numero", "")
    commande = "curl -X POST https://api.sms-partner.ma/send -d to=" + numero
    subprocess.run(commande, shell=True)
    return {"statut": "envoye"}


@notifications_bp.route("/notify/webhook")
def appeler_webhook():
    """Notifie le systeme du marchand."""
    url = request.args.get("url", "")
    return {"code": requests.get(url, verify=False, timeout=5).status_code}
