#!/usr/bin/env python3
"""
Main application entry point for User Service API
"""
import os
import connexion
from flask_cors import CORS

from database import db_session, init_db

# Create Connexion application instance
connex_app = connexion.FlaskApp(__name__, specification_dir='./')

# Add API definition
connex_app.add_api('./user-service.yaml', validate_responses=True, pythonic_params=True, jsonifier=...)

# Get Flask application instance
app = connex_app.app

# Configure the application
app.config.from_object('config.Config')

# Enable CORS
CORS(app)


# Register DB session cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Initialize the database
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    connex_app.run(host='0.0.0.0', port=port)
