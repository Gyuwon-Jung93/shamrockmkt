import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Listing, Message, Transaction
import datetime

# Database configuration
DATABASE_URL = f"postgresql://jacob@localhost/shamrock_market"

# Create database engine
engine = create_engine(DATABASE_URL)

# Configure database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables have been created.")

    # Create session
    db = SessionLocal()

    # ✅ Insert initial dummy data
    try:
        # 1️⃣ Add user data
        user1 = User(username="john_doe", email="john@example.com", password_hash="hashedpassword1")
        user2 = User(username="jane_doe", email="jane@example.com", password_hash="hashedpassword2")

        db.add(user1)
        db.add(user2)
        db.commit()

        # 2️⃣ Add listing data
        listing1 = Listing(
            title="iPhone 14 Pro Max",
            description="Like new condition.",
            price=1200.00,
            category="Electronics",
            image_url="https://example.com/iphone.jpg",
            location="Dublin, Ireland",
            owner_id=user1.id,
            created_at=datetime.datetime.utcnow()
        )

        listing2 = Listing(
            title="MacBook Pro 16-inch",
            description="M1 chip, 16GB RAM, almost like new.",
            price=2500.00,
            category="Electronics",
            image_url="https://example.com/macbook.jpg",
            location="Dublin, Ireland",
            owner_id=user2.id,
            created_at=datetime.datetime.utcnow()
        )

        db.add(listing1)
        db.add(listing2)
        db.commit()

        # 3️⃣ Add transaction data
        transaction1 = Transaction(
            listing_id=listing1.id,
            buyer_id=user2.id,
            seller_id=user1.id,
            status="completed",
            timestamp=datetime.datetime.utcnow()
        )

        db.add(transaction1)
        db.commit()

        # 4️⃣ Add chat message
        message1 = Message(
            sender_id=user2.id,
            receiver_id=user1.id,
            listing_id=listing1.id,
            message_text="Is this still available?",
            timestamp=datetime.datetime.utcnow()
        )

        db.add(message1)
        db.commit()

        print("✅ Initial dummy data has been added.")

    except Exception as e:
        db.rollback()
        print(f"⚠️ Error occurred while inserting data: {e}")

    finally:
        db.close()

# Execute
if __name__ == "__main__":
    init_db()