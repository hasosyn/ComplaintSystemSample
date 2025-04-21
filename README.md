# MefRecipes Backend

This is the backend service for the MefRecipes application, built with FastAPI and MongoDB.

## Features

- User authentication and authorization
- Recipe management (CRUD operations)
- Inventory tracking
- Shopping list management
- Image upload and storage
- API documentation with Swagger UI

## Prerequisites

- Python 3.8+
- MongoDB
- pip (Python package manager)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with the following variables:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=mefrecipes
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:19006
```

5. Initialize the database:
```bash
python -m database.init_db
```

## Running the Server

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── schemas.py
│   └── utils/
├── database/
│   ├── __init__.py
│   └── init_db.py
├── .env
├── requirements.txt
└── README.md
```

## API Endpoints

### Authentication

#### Register a new user
```http
POST /api/auth/register
Content-Type: application/json

{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
}

Response (201 Created):
{
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "username": "johndoe",
    "first_name": "John",
    "last_name": "Doe",
    "created_at": "2024-01-01T12:00:00Z"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
    "username": "johndoe",
    "password": "securepassword123"
}

Response (200 OK):
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 1800
}
```

#### Get current user info
```http
GET /api/auth/me
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response (200 OK):
{
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "username": "johndoe",
    "first_name": "John",
    "last_name": "Doe",
    "created_at": "2024-01-01T12:00:00Z"
}
```

### Recipes

#### Create a new recipe
```http
POST /api/recipes/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Spaghetti Carbonara",
    "description": "Classic Italian pasta dish",
    "category": "Pasta",
    "prep_time": 15,
    "cook_time": 15,
    "servings": 4,
    "difficulty": "medium",
    "ingredients": [
        {
            "name": "spaghetti",
            "amount": 400,
            "unit": "g"
        },
        {
            "name": "eggs",
            "amount": 4,
            "unit": "pcs"
        }
    ],
    "steps": [
        {
            "step_number": 1,
            "instructions": "Cook pasta according to package instructions"
        }
    ],
    "tags": ["italian", "pasta", "quick"]
}

Response (201 Created):
{
    "id": "507f1f77bcf86cd799439012",
    "title": "Spaghetti Carbonara",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

#### Get all recipes
```http
GET /api/recipes/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response (200 OK):
{
    "recipes": [
        {
            "id": "507f1f77bcf86cd799439012",
            "title": "Spaghetti Carbonara",
            "description": "Classic Italian pasta dish",
            "category": "Pasta",
            "prep_time": 15,
            "cook_time": 15,
            "servings": 4,
            "difficulty": "medium",
            "created_at": "2024-01-01T12:00:00Z"
        }
    ],
    "total": 1,
    "page": 1,
    "per_page": 10
}
```

#### Get a specific recipe
```http
GET /api/recipes/507f1f77bcf86cd799439012
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response (200 OK):
{
    "id": "507f1f77bcf86cd799439012",
    "title": "Spaghetti Carbonara",
    "description": "Classic Italian pasta dish",
    "category": "Pasta",
    "prep_time": 15,
    "cook_time": 15,
    "servings": 4,
    "difficulty": "medium",
    "ingredients": [
        {
            "name": "spaghetti",
            "amount": 400,
            "unit": "g"
        },
        {
            "name": "eggs",
            "amount": 4,
            "unit": "pcs"
        }
    ],
    "steps": [
        {
            "step_number": 1,
            "instructions": "Cook pasta according to package instructions"
        }
    ],
    "tags": ["italian", "pasta", "quick"],
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

### Inventory

#### Add an inventory item
```http
POST /api/inventory/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "name": "Pasta",
    "category": "Pantry",
    "quantity": 2,
    "unit": "kg",
    "expiration_date": "2024-12-31",
    "location": "Kitchen cabinet"
}

Response (201 Created):
{
    "id": "507f1f77bcf86cd799439013",
    "name": "Pasta",
    "category": "Pantry",
    "quantity": 2,
    "unit": "kg",
    "expiration_date": "2024-12-31",
    "location": "Kitchen cabinet",
    "created_at": "2024-01-01T12:00:00Z"
}
```

#### Get all inventory items
```http
GET /api/inventory/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response (200 OK):
{
    "items": [
        {
            "id": "507f1f77bcf86cd799439013",
            "name": "Pasta",
            "category": "Pantry",
            "quantity": 2,
            "unit": "kg",
            "expiration_date": "2024-12-31",
            "location": "Kitchen cabinet"
        }
    ],
    "total": 1,
    "page": 1,
    "per_page": 10
}
```

### Shopping Lists

#### Create a shopping list
```http
POST /api/shopping-lists/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "name": "Weekly Groceries",
    "items": [
        {
            "name": "Milk",
            "quantity": 2,
            "unit": "L",
            "category": "Dairy",
            "priority": "high"
        }
    ],
    "is_shared": false
}

Response (201 Created):
{
    "id": "507f1f77bcf86cd799439014",
    "name": "Weekly Groceries",
    "items": [
        {
            "name": "Milk",
            "quantity": 2,
            "unit": "L",
            "category": "Dairy",
            "priority": "high",
            "is_checked": false
        }
    ],
    "is_shared": false,
    "created_at": "2024-01-01T12:00:00Z"
}
```

#### Get all shopping lists
```http
GET /api/shopping-lists/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response (200 OK):
{
    "lists": [
        {
            "id": "507f1f77bcf86cd799439014",
            "name": "Weekly Groceries",
            "items_count": 1,
            "is_shared": false,
            "created_at": "2024-01-01T12:00:00Z"
        }
    ],
    "total": 1,
    "page": 1,
    "per_page": 10
}
```

## Testing

To run the tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
