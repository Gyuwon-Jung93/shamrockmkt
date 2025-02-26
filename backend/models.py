from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base
import datetime

# User Table
# Table for managing user accounts
# Includes columns such as username, email, password_hash, and created_at
# Establishes relationships with the listings (products) and messages (chats) tables
# 사용자 테이블
# 사용자 계정을 관리하는 테이블
# username, email, password_hash, created_at 등의 컬럼 포함
# 사용자가 등록한 상품(listings), 채팅(messages)과 관계 설정

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    listings = relationship("Listing", back_populates="owner")
    messages = relationship("Message", back_populates="sender")

# Listing Table
# Stores information about products listed for sale by users
# Includes columns such as title, description, price, image_url, and location
# Links owner_id to the User table
# 상품 테이블
# 사용자가 판매하는 상품 정보를 저장
# title (제목), description (설명), price (가격), image_url (이미지), location (위치) 등의 컬럼 포함
# owner_id(상품 소유자)와 User 테이블과 연결
class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    image_url = Column(String)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship("User", back_populates="listings")

# Message Table (Chat Feature)
# Stores chat messages exchanged between users regarding a listing
# Connects sender_id (sender), receiver_id (receiver), and listing_id (product)
# 메시지 테이블 (채팅 기능)
# 사용자가 상품에 대해 주고받은 채팅 메시지 저장
# sender_id (보낸 사람), receiver_id (받는 사람), listing_id (상품)와 연결

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    listing_id = Column(Integer, ForeignKey('listings.id'))
    message_text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    sender = relationship("User", foreign_keys=[sender_id], back_populates="messages")
    receiver = relationship("User", foreign_keys=[receiver_id])
    listing = relationship("Listing")

# Transaction Table (Purchase Requests & Transaction Status)
# Stores transaction history when a user purchases a product
# Includes buyer_id (buyer), seller_id (seller), and status (transaction status)
# 거래 테이블 (구매 요청 및 거래 상태)
# 사용자가 상품을 구매하는 경우 거래 내역을 저장
# buyer_id (구매자), seller_id (판매자), status (거래 상태) 포함
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey('listings.id'))
    buyer_id = Column(Integer, ForeignKey('users.id'))
    seller_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String, default='pending')  # pending, completed, cancelled
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    listing = relationship("Listing")
    buyer = relationship("User", foreign_keys=[buyer_id])
    seller = relationship("User", foreign_keys=[seller_id])
