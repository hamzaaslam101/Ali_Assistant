from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    scans = relationship("Scan", back_populates="user")
    conversations = relationship("Conversation", back_populates="user")

class Scan(Base):
    __tablename__ = "scans"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    target = Column(String, nullable=False)
    scan_type = Column(String, nullable=False)
    status = Column(String, default="pending")
    started_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    results = Column(JSON, nullable=True)
    error_message = Column(Text, nullable=True)
    
    user = relationship("User", back_populates="scans")
    vulnerabilities = relationship("Vulnerability", back_populates="scan")

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    
    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scans.id"))
    name = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    recommendation = Column(Text, nullable=True)
    discovered_at = Column(DateTime, nullable=False)
    
    scan = relationship("Scan", back_populates="vulnerabilities")

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=Tru
