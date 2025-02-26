from flask import Flask, jsonify
from routes.user_routes import user_bp
from routes.listing_routes import listing_bp
from routes.chat_routes import chat_bp
from routes.transaction_routes import transaction_bp
from flask_cors import CORS  

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5173"}},supports_credentials=True)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Shamrock Market API!"}), 200

@app.route("/api/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "iPhone 14 Pro", "price": 1200.00},
        {"id": 2, "name": "MacBook Pro", "price": 2500.00}
    ]
    return jsonify(products)


# Router Register
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(listing_bp, url_prefix="/listings")
app.register_blueprint(chat_bp, url_prefix="/chats")
app.register_blueprint(transaction_bp, url_prefix="/transactions")

if __name__ == "__main__":
    app.run(debug=True, port=5000)