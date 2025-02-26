from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database import get_db
from models import Message

chat_bp = Blueprint("chat", __name__)

# Chating msg send API
@chat_bp.route("/send", methods=["POST"])
def send_message():
    db: Session = next(get_db())
    data = request.json

    new_message = Message(
        sender_id=data["sender_id"],
        receiver_id=data["receiver_id"],
        listing_id=data["listing_id"],
        message_text=data["message_text"]
    )

    db.add(new_message)
    db.commit()
    return jsonify({"message": "Message sent successfully"}), 201

# Chating msg Listing API
@chat_bp.route("/<int:listing_id>", methods=["GET"])
def get_messages(listing_id):
    db: Session = next(get_db())
    messages = db.query(Message).filter(Message.listing_id == listing_id).all()

    return jsonify([{
        "sender_id": msg.sender_id,
        "receiver_id": msg.receiver_id,
        "text": msg.message_text,
        "timestamp": msg.timestamp
    } for msg in messages])