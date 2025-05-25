"""
SQLAlchemy models for the Base Model
"""
from sqlalchemy import Column, Integer
from database import db_session


class BaseModel:
    """User model."""

    id = Column(Integer, primary_key=True)

    def __init__(self):
        pass

    def to_dict(self):
        raise NotImplementedError('')

    def delete(self, commit=True):
        db_session.delete(self)
        if commit:
            db_session.commit()

    @classmethod
    def get_by_id(cls, id_: int):
        user = cls.query.filter(cls.id == id_).first()  # pylint: disable=E1101
        return user

    @classmethod
    def get_all(cls) -> list:
        user_list = cls.query.all()  # pylint: disable=E1101
        return user_list