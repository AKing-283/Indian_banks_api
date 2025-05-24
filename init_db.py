import csv
from app import app, db
from app.models import Bank, Branch
import os

def init_db():
    with app.app_context():
        # Check if database already has data
        if Bank.query.first() is not None:
            print("Database already exists and has data. Skipping initialization.")
            return

        # Create tables if they don't exist
        db.create_all()
        
        # Read CSV file
        with open('bank_branches.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            
            # Dictionary to store bank names and their IDs
            bank_dict = {}
            
            # Process each row
            for row in csv_reader:
                try:
                    # Add bank if not exists
                    if row['bank_name'] not in bank_dict:
                        bank = Bank(name=row['bank_name'])
                        db.session.add(bank)
                        db.session.flush()  # This will get us the bank.id
                        bank_dict[row['bank_name']] = bank.id
                    
                    # Add branch
                    branch = Branch(
                        ifsc=row['ifsc'],
                        bank_id=bank_dict[row['bank_name']],
                        branch=row['branch'],
                        address=row['address'],
                        city=row['city'],
                        district=row['district'],
                        state=row['state']
                    )
                    db.session.add(branch)
                    
                    # Commit every 1000 records to avoid memory issues
                    if len(bank_dict) % 1000 == 0:
                        db.session.commit()
                        print(f"Processed {len(bank_dict)} banks...")
                
                except Exception as e:
                    print(f"Error processing row: {row}")
                    print(f"Error: {str(e)}")
                    db.session.rollback()
                    continue
            
            # Final commit
            db.session.commit()
            print("Database initialized successfully!")

if __name__ == '__main__':
    # Check if database file exists
    db_path = os.path.join(os.path.dirname(__file__), 'app', 'indian_banks.db')
    if not os.path.exists(db_path):
        print("Database file not found. Creating new database...")
        init_db()
    else:
        print("Database file exists. Checking if initialization is needed...")
        init_db() 