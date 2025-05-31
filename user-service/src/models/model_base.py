"""
SQLAlchemy models for the Base Model
"""
import logging
from sqlalchemy import Column, Integer
from sqlalchemy.exc import IntegrityError
from database import db_session


class BaseModel:
    """Base model."""

    id = Column(Integer, primary_key=True)

    def to_dict(self):
        raise NotImplementedError(f'Please implement fhe function for {self.__class__.__name__}')

    def create(self, commit=True) -> bool:
        try:
            db_session.add(self)
            if commit:
                db_session.commit()
            return True
        except IntegrityError:
            db_session.rollback()
            return False
        except Exception as e:  # pylint: disable=W0718
            logging.exception(f'create : unexpected exception : {e}')
            db_session.rollback()
            raise e

    def update(self, _: dict, commit=True) -> bool:
        try:
            if commit:
                db_session.commit()
            return True
        except IntegrityError:
            db_session.rollback()
            return False
        except Exception as e:  # pylint: disable=W0718
            logging.exception(f'update : unexpected exception : {e}')
            db_session.rollback()
            raise e

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
