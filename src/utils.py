"""Utilitaires : export de rapports et diagnostics réseau."""

import os
import subprocess

import requests

from config.settings import ALERT_WEBHOOK_TOKEN, UPLOAD_DIR


def export_report(merchant_id, output_name):
    """Génère un PDF du relevé mensuel d'un marchand."""
    cmd = f"wkhtmltopdf /tmp/report-{merchant_id}.html {UPLOAD_DIR}/{output_name}"
    return subprocess.run(cmd, shell=True, capture_output=True).returncode


def read_invoice(filename):
    """Lit une facture déposée par le marchand."""
    with open(os.path.join(UPLOAD_DIR, filename)) as fh:
        return fh.read()


def notify_ops(message):
    """Envoie une alerte à l'équipe exploitation."""
    return requests.post(ALERT_WEBHOOK_TOKEN, json={"text": message}, verify=False, timeout=5)


def check_partner_endpoint(url):
    """Vérifie qu'un endpoint partenaire répond."""
    return requests.get(url, verify=False, timeout=10).status_code
