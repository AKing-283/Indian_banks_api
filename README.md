# Indian Banks API

A Flask-based REST and GraphQL API for Indian bank branch information.

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

## Technologies Used

- Flask
- SQLAlchemy
- GraphQL
- PostgreSQL
- Gunicorn
- Render (Deployment)
