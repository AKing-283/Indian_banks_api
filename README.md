# Indian Banks API

A Flask-based API service for Indian Banks data with both REST and GraphQL endpoints.

## Solution Overview

### Time Taken
- Total time: ~2 hours
  - Setup and dependency resolution: 30 minutes
  - Database modeling and initialization: 30 minutes
  - API implementation: 45 minutes
  - Testing and debugging: 15 minutes

### Approach
1. **Technology Stack Selection**
   - Flask for the web framework
   - SQLite for database (simpler setup than PostgreSQL)
   - Flask-SQLAlchemy for ORM
   - Flask-GraphQL for GraphQL support

2. **Database Design**
   - Two main models: Bank and Branch
   - Bank model with auto-incrementing IDs
   - Branch model with IFSC as primary key
   - Proper relationships between models

3. **API Implementation**
   - REST API endpoints for basic CRUD operations
   - GraphQL endpoint for flexible querying
   - Proper error handling and data validation

4. **Data Migration**
   - CSV to SQLite conversion
   - Batch processing for large datasets
   - Error handling during data import

## Project Structure
```
.
├── app/
│   ├── __init__.py      # Flask app initialization
│   ├── models.py        # Database models
│   ├── routes.py        # REST API endpoints
│   └── graphql.py       # GraphQL schema
├── init_db.py           # Database initialization script
├── requirements.txt     # Project dependencies
├── run.py              # Application entry point
└── bank_branches.csv   # Source data
```

## API Endpoints

### REST API
1. Get All Banks
   ```
   GET /api/banks
   ```

2. Get Bank Branches
   ```
   GET /api/banks/{bank_id}/branches
   ```

3. Get Branch Details
   ```
   GET /api/branches/{ifsc}
   ```

### GraphQL
```
POST /gql
```

Example Query:
```graphql
query {
  branches {
    edges {
      node {
        branch
        bank {
          name
        }
        ifsc
      }
    }
  }
}
```

## Setup Instructions

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize database:
   ```bash
   python init_db.py
   ```

4. Run the application:
   ```bash
   python run.py
   ```

## Testing
- Use Postman for REST API testing
- Use GraphiQL interface at http://localhost:5000/gql for GraphQL testing

## Future Improvements
1. Add pagination for large result sets
2. Implement caching for better performance
3. Add more comprehensive error handling
4. Add unit tests
5. Add API documentation using Swagger/OpenAPI
