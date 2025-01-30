# Django REST API Project

## Overview
This Django REST API project provides a backend service implementing basic CRUD (Create, Read, Update, Delete) operations. The API is built using Django REST Framework.

## Technologies
- Python 3.8+
- Django 4.2+
- Django REST Framework
- PostgreSQL

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)
- PostgreSQL

### Local Development Setup
1. Clone the repository:
```bash
git clone git@github.com:Indi-o-e-Hacking/ih-ps-backend.git
cd ih-ps-backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

### Base URL
`http://localhost:8000/api/v1/`

### Authentication
- Token-based authentication
- Include token in Authorization header: `Authorization: Token <your-token>`

### Endpoints

#### Users Resource

- **Register User**
  - POST `/api/v1/users/register`
  - Creates a new user account
  - Required fields:
    - `username`: string
    - `password`: string
    - `email`: string
    - `first_name`: string
    - `last_name`: string

- **List Users**
  - GET `/api/v1/users`
  - Returns a list of all users
  - Response includes:
    - `id`: number
    - `username`: string
    - `email`: string
    - `first_name`: string
    - `last_name`: string

### Response Format
```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "Example Item",
        "description": "Description here",
        "price": "29.99",
        "created_at": "2023-01-01T00:00:00Z"
    }
}
```

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use black for code formatting
- Run flake8 for linting

### Testing
Run tests using:
```bash
pytest
```

### Making Contributions
1. Create a new branch for each feature
2. Write tests for new features
3. Ensure all tests pass before submitting PR
4. Follow the PR template guidelines

## License
This project is licensed under the MIT License - see the LICENSE file for details.

