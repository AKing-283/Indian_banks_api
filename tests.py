import pytest
from app import app, db
from app.models import Bank, Branch
from app.graphql import schema
from flask_graphql import GraphQLView
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Add test data
            bank = Bank(name='Test Bank')
            db.session.add(bank)
            db.session.flush()
            
            branch = Branch(
                ifsc='TEST0000001',
                bank_id=bank.id,
                branch='Test Branch',
                address='Test Address',
                city='Test City',
                district='Test District',
                state='Test State'
            )
            db.session.add(branch)
            db.session.commit()
            
            yield client
            
            db.session.remove()
            db.drop_all()

def test_get_banks(client):
    """Test getting all banks"""
    response = client.get('/api/banks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert data[0]['name'] == 'Test Bank'

def test_get_bank_branches(client):
    """Test getting branches for a specific bank"""
    response = client.get('/api/banks/1/branches')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert data[0]['ifsc'] == 'TEST0000001'
    assert data[0]['branch'] == 'Test Branch'

def test_get_branch(client):
    """Test getting a specific branch by IFSC"""
    response = client.get('/api/branches/TEST0000001')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['ifsc'] == 'TEST0000001'
    assert data['branch'] == 'Test Branch'
    assert data['bank']['name'] == 'Test Bank'

def test_get_nonexistent_branch(client):
    """Test getting a non-existent branch"""
    response = client.get('/api/branches/NONEXISTENT')
    assert response.status_code == 404

def test_graphql_branches_query(client):
    """Test GraphQL branches query"""
    query = """
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
    """
    response = client.post('/gql', json={'query': query})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert 'branches' in data['data']
    assert len(data['data']['branches']['edges']) > 0
    assert data['data']['branches']['edges'][0]['node']['ifsc'] == 'TEST0000001'

def test_graphql_banks_query(client):
    """Test GraphQL banks query"""
    query = """
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
    """
    response = client.post('/gql', json={'query': query})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    assert 'banks' in data['data']
    assert len(data['data']['banks']['edges']) > 0
    assert data['data']['banks']['edges'][0]['node']['name'] == 'Test Bank'

def test_invalid_graphql_query(client):
    """Test invalid GraphQL query"""
    query = """
    query {
        invalid {
            field
        }
    }
    """
    response = client.post('/gql', json={'query': query})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'errors' in data 