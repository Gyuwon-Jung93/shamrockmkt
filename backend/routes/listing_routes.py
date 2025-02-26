from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database import get_db
from models import Listing

listing_bp = Blueprint("listing", __name__)

# product register API
@listing_bp.route("/", methods=["POST"])
def create_listing():
    db: Session = next(get_db())
    data = request.json

    new_listing = Listing(
        title=data["title"],
        description=data["description"],
        price=data["price"],
        category=data["category"],
        image_url=data.get("image_url"),
        location=data["location"],
        owner_id=data["owner_id"]
    )
    
    db.add(new_listing)
    db.commit()
    return jsonify({"message": "Listing created successfully"}), 201

# product Listing API
@listing_bp.route("/", methods=["GET"])
def get_listings():
    db: Session = next(get_db())
    listings = db.query(Listing).all()
    
    return jsonify([{
        "id": listing.id,
        "title": listing.title,
        "price": listing.price,
        "location": listing.location,
        "image_url": listing.image_url
    } for listing in listings])