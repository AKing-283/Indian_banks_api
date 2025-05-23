from app import db
from datetime import datetime

class Bank(db.Model):
    __tablename__ = 'banks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(49))
    branches = db.relationship('Branch', backref='bank', lazy=True)

    def __repr__(self):
        return f'<Bank {self.name}>'

class Branch(db.Model):
    __tablename__ = 'branches'
    
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Branch {self.ifsc}>' 