from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database import get_db
from models import Transaction

transaction_bp = Blueprint("transaction", __name__)

# TransAction Creation API
@transaction_bp.route("/", methods=["POST"])
def create_transaction():
    db: Session = next(get_db())
    data = request.json

    new_transaction = Transaction(
        listing_id=data["listing_id"],
        buyer_id=data["buyer_id"],
        seller_id=data["seller_id"],
        status="pending"
    )

    db.add(new_transaction)
    db.commit()
    return jsonify({"message": "Transaction created successfully"}), 201

# TransAction State change API
@transaction_bp.route("/<int:transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    db: Session = next(get_db())
    data = request.json

    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        return jsonify({"message": "Transaction not found"}), 404

    transaction.status = data["status"]
    db.commit()
    return jsonify({"message": "Transaction updated successfully"})