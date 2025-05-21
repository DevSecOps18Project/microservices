# User Service API

A RESTful API for managing user accounts, built with Flask, Connexion, and SQLAlchemy.

## Project Structure

```
user_service/
│
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── models.py               # SQLAlchemy models
├── controllers/
│   ├── __init__.py
│   └── users.py            # User controller functions
├── database.py             # Database connection handling
├── exceptions.py           # Custom exceptions
├── requirements.txt        # Project dependencies
├── user-service.yaml       # OpenAPI specification file
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── deploy.sh               # Deployment script for Docker
└── docker-compose-util.sh  # Utility script for Docker Compose
```

## Setup and Installation

### Local Development

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the PostgreSQL database:

```bash
# Create a database named user_service
# Or set DATABASE_URL environment variable to your PostgreSQL connection string
```

4. Run the application:

```bash
python app.py
```

The API will be available at http://localhost:8080, and the Swagger UI documentation will be available at http://localhost:8080/ui.

### Docker Deployment

#### Option 1: Using the deployment script

Make the script executable and run it:

```bash
chmod +x deploy.sh
./deploy.sh
```

#### Option 2: Using Docker Compose

Make the utility script executable:

```bash
chmod +x docker-compose-util.sh
```

Start the services:

```bash
./docker-compose-util.sh start
```

Additional commands:

```bash
./docker-compose-util.sh stop     # Stop the services
./docker-compose-util.sh restart  # Restart the services
./docker-compose-util.sh logs     # View logs
./docker-compose-util.sh status   # Check status
./docker-compose-util.sh clean    # Clean up (remove containers, networks, volumes)
```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string (default: postgresql://postgres:postgres@localhost:5432/user_service)
- `DEBUG`: Enable debug mode (default: False)
- `SECRET_KEY`: Application secret key (default: super-secret-key)
- `PORT`: Port to run the application on (default: 8080)

## API Endpoints

- `GET /`: Health status
- `GET /api/users`: Get all users
- `POST /api/users`: Create a new user
- `GET /api/users/{id}`: Get user by ID
- `PUT /api/users/{id}`: Update user
- `DELETE /api/users/{id}`: Delete user

## Dependencies

- Connexion: OpenAPI/Swagger framework for Flask
- SQLAlchemy: SQL toolkit and ORM
- Flask-CORS: Cross-Origin Resource Sharing support
- PostgreSQL: Database
