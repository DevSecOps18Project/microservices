"""
User controller functions for the User Service API
"""
import logging
from connexion import NoContent
from sqlalchemy.exc import IntegrityError

import exceptions
from controllers import tools
from database import db_session
from models.user import User

LOG = logging


def get_user_by_id(id_: int):
    """Get user by ID or raise an NotFound."""
    user = User.get_by_id(id_)
    if not user:
        LOG.error('User %s was not found', id_)
        raise exceptions.UserNotFound(user_id=id_)
    return user


def health_status():
    """Get health status."""
    return {'status': 'ok'}


def user_get_all():
    """Get all users."""
    users = User.get_all()
    return [user.to_dict() for user in users]


@tools.expected_errors(404)
def user_get_by_id(id_: int):
    """Get user by ID."""
    user = get_user_by_id(id_)
    return user.to_dict()


@tools.normal_response(201)
@tools.expected_errors(400)
def user_create(body: dict):
    """Create a new user."""
    user = User(body)
    try:
        # Create new user
        user.create()
        LOG.info('User %s was created successfully!', user.id)
        return user.to_dict()

    except IntegrityError:
        db_session.rollback()
        LOG.error('User with email %s already exists.', user.email)
        raise exceptions.UserEmailAlreadyExist(user.email)  # pylint: disable=W0707


@tools.expected_errors(400, 404)
def user_update(id_: int, body):
    """Update an existing user."""
    user = get_user_by_id(id_)
    try:
        user.update(body)
        LOG.info('User %s was updated successfully!', user.id)
        return user.to_dict()

    except IntegrityError:
        db_session.rollback()
        LOG.info('User with email %s already exists.', user.email)
        raise exceptions.UserEmailAlreadyExist(user.email)  # pylint: disable=W0707


@tools.normal_response(204)
@tools.expected_errors(404)
def user_delete(id_: int):
    """Delete user."""
    user = get_user_by_id(id_)
    user.delete()
    LOG.info('User %s was deleted successfully!', user.id)
    return NoContent
