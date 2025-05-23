from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'indian_banks.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after db initialization to avoid circular imports
from app import routes, models, graphql

# Create database tables
with app.app_context():
    db.create_all()
    
    # Add some test data if the database is empty
    from app.models import Bank, Branch
    if Bank.query.count() == 0:
        test_bank = Bank(name='Test Bank')
        db.session.add(test_bank)
        db.session.flush()
        
        test_branch = Branch(
            ifsc='TEST0000001',
            bank_id=test_bank.id,
            branch='Test Branch',
            address='Test Address',
            city='Test City',
            district='Test District',
            state='Test State'
        )
        db.session.add(test_branch)
        db.session.commit()

# Register GraphQL endpoint
app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=graphql.schema,
        graphiql=True  # Enable GraphiQL interface
    )
) 