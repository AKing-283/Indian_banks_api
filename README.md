# Indian Banks API

A Flask-based REST and GraphQL API for Indian bank branch information.

## Solution Approach

### Time Taken
- Total time: ~4-5 hours
  - Initial setup and dependency resolution: 1 hour
  - Database modeling and implementation: 1 hour
  - API implementation (REST + GraphQL): 1.5 hours
  - Testing and debugging: 1 hour
  - Deployment and documentation: 30 minutes

### Implementation Strategy

1. **Technology Stack Selection**
   - Flask as the web framework for its simplicity and flexibility
   - SQLAlchemy for ORM to handle database operations
   - GraphQL for flexible data querying
   - Gunicorn as the production server
   - Render for deployment

2. **Database Design**
   - Two main models: Bank and Branch
   - Bank model with auto-incrementing IDs
   - Branch model with IFSC as primary key
   - Proper relationships between models
   - Timestamp fields for tracking creation and updates

3. **API Implementation**
   - REST API endpoints for basic CRUD operations
   - GraphQL endpoint for flexible querying
   - Proper error handling and data validation
   - Support for time-based queries

4. **Testing Strategy**
   - Unit tests for all API endpoints
   - Test fixtures for database setup
   - Coverage reporting
   - Both REST and GraphQL endpoint testing

5. **Deployment Strategy**
   - Containerized deployment using Gunicorn
   - Environment-based configuration
   - Database migration handling
   - Automatic test data seeding

## Live Demo

The API is deployed at: [https://indian-banks-api-u5d0.onrender.com](https://indian-banks-api-u5d0.onrender.com)

## API Endpoints

### REST API

1. Get all banks:
```
GET https://indian-banks-api-u5d0.onrender.com/api/banks
```

2. Get branches for a specific bank:
```
GET https://indian-banks-api-u5d0.onrender.com/api/banks/{bank_id}/branches
```

3. Get a specific branch by IFSC:
```
GET https://indian-banks-api-u5d0.onrender.com/api/branches/{ifsc}
```

### GraphQL API

GraphQL endpoint: `https://indian-banks-api-u5d0.onrender.com/gql`

Example queries:

1. Get all branches with bank information:
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

2. Get all banks:
```graphql
query {
  banks {
    edges {
      node {
        id
        name
      }
    }
  }
}
```

## Testing the API

### Using Postman

1. REST API Testing:
   - Set request method to GET
   - Use the endpoints listed above
   - No authentication required

2. GraphQL Testing:
   - Set request method to POST
   - URL: `https://indian-banks-api-u5d0.onrender.com/gql`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
   ```json
   {
       "query": "query { branches { edges { node { branch bank { name } ifsc } } } }"
   }
   ```

### Using Browser

1. For GraphQL testing:
   - Visit `https://indian-banks-api-u5d0.onrender.com/gql`
   - Use the GraphiQL interface to write and test queries

2. For REST API testing:
   - Simply paste the REST endpoints in your browser
   - Example: `https://indian-banks-api-u5d0.onrender.com/api/banks`

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/AKing-283/Indian_banks_api.git
cd Indian_banks_api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Database Initialization

### Issue and Solution

Previously, the database initialization script (`init_db.py`) would recreate the database every time it was run, causing data loss. This has been fixed with the following improvements:

1. **Smart Initialization**
   - Database is only created if it doesn't exist
   - Existing data is preserved between runs
   - Initialization is skipped if data is already present

2. **How to Use**
   ```bash
   # First time setup or if database is missing
   python init_db.py
   
   # Subsequent runs will preserve existing data
   python init_db.py
   ```

3. **Benefits**
   - No accidental data loss
   - Faster subsequent runs
   - Safe to run multiple times
   - Preserves existing data

## Technologies Used

- Flask
- SQLAlchemy
- GraphQL
- Gunicorn
- Render (Deployment)

## Future Improvements

1. Add pagination for large result sets
2. Implement caching for better performance
3. Add more comprehensive error handling
4. Add API documentation using Swagger/OpenAPI
5. Add rate limiting
6. Implement user authentication
7. Add more advanced GraphQL features (mutations, subscriptions)
