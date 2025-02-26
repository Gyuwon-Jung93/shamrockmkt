from flask import Flask, jsonify
from routes.user_routes import user_bp
from routes.listing_routes import listing_bp
from routes.chat_routes import chat_bp
from routes.transaction_routes import transaction_bp

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Shamrock Market API!"}), 200

# Router Register
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(listing_bp, url_prefix="/listings")
app.register_blueprint(chat_bp, url_prefix="/chats")
app.register_blueprint(transaction_bp, url_prefix="/transactions")

if __name__ == "__main__":
    app.run(debug=True)