from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database import get_db
from models import User
import bcrypt

user_bp = Blueprint("user", __name__)

# Signup API
@user_bp.route("/register", methods=["POST"])
def register():
    db: Session = next(get_db())
    data = request.json
    hashed_pw = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())

    new_user = User(username=data["username"], email=data["email"], password_hash=hashed_pw.decode("utf-8"))
    db.add(new_user)
    db.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# SignIn API
@user_bp.route("/login", methods=["POST"])
def login():
    db: Session = next(get_db())
    data = request.json
    user = db.query(User).filter(User.email == data["email"]).first()
    
    if user and bcrypt.checkpw(data["password"].encode("utf-8"), user.password_hash.encode("utf-8")):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid email or password"}), 401