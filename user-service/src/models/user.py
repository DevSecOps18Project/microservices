"""
SQLAlchemy models for the User Service API
"""
from sqlalchemy import Column, String
from database import Base

from models.model_base import BaseModel


class User(BaseModel, Base):
    """User model."""

    __tablename__ = 'users'

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)

    def __init__(self, name, email, phone=None):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }
