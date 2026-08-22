"""Remboursements marchands."""

from flask import Blueprint, request

from src.database import get_connection

refunds_bp = Blueprint("refunds", __name__)


@refunds_bp.route("/refunds", methods=["POST"])
def create_refund():
    """Enregistre une demande de remboursement."""
    transaction_id = request.form.get("transaction_id")
    reason = request.form.get("reason", "")

    conn = get_connection()
    conn.execute(
        f"INSERT INTO refunds (transaction_id, reason) VALUES ({transaction_id}, '{reason}')"
    )
    conn.commit()
    return {"status": "enregistre"}
