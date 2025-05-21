"""
User controller functions for the User Service API
"""
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from database import db_session
from models.user import User


def health_status():
    """Get health status."""
    return jsonify({'status': 'ok'})


def user_get_all():
    """Get all users."""
    users = User.get_all()
    return jsonify([user.to_dict() for user in users])


def user_get_by_id(id_: int):
    """Get user by ID."""
    user = User.get_by_id(id_)
    if not user:
        return jsonify({'message': f'User with ID {id_} not found'}), 404
    return jsonify(user.to_dict())


def user_create(body):
    """Create a new user."""
    try:
        # Validate required fields
        if not body.get('name') or not body.get('email'):
            return jsonify({'message': 'Name and email are required'}), 400

        # Create new user
        user = User(
            name=body.get('name'),
            email=body.get('email'),
            phone=body.get('phone')
        )

        # Add user to database
        db_session.add(user)
        db_session.commit()

        return jsonify(user.to_dict()), 201

    except IntegrityError:
        db_session.rollback()
        return jsonify({'message': 'Email already exists'}), 400

    except Exception as e:
        db_session.rollback()
        return jsonify({'message': str(e)}), 400


def user_update(id_: int, body):
    """Update an existing user."""
    try:
        # Find user
        user = User.get_by_id(id_)
        if not user:
            return jsonify({'message': f'User with ID {id_} not found'}), 404

        # Update user fields if provided
        for key in ['name', 'email', 'phone']:
            if key in body:
                setattr(user, key, body[key])

        # Commit changes
        db_session.commit()

        return jsonify(user.to_dict())

    except IntegrityError:
        db_session.rollback()
        return jsonify({'message': 'Email already exists'}), 400

    except Exception as e:
        db_session.rollback()
        return jsonify({'message': str(e)}), 400


def user_delete(id_: int):
    """Delete user."""
    # Find user
    user = User.get_by_id(id_)
    if not user:
        return jsonify({'message': f'User with ID {id_} not found'}), 404

    # Delete user
    user.delete()

    return '', 204
