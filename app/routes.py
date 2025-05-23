from flask import jsonify
from app import app, db
from app.models import Bank, Branch

@app.route('/api/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify([{
        'id': bank.id,
        'name': bank.name
    } for bank in banks])

@app.route('/api/banks/<int:bank_id>/branches', methods=['GET'])
def get_bank_branches(bank_id):
    branches = Branch.query.filter_by(bank_id=bank_id).all()
    return jsonify([{
        'ifsc': branch.ifsc,
        'branch': branch.branch,
        'address': branch.address,
        'city': branch.city,
        'district': branch.district,
        'state': branch.state
    } for branch in branches])

@app.route('/api/branches/<ifsc>', methods=['GET'])
def get_branch(ifsc):
    branch = Branch.query.get_or_404(ifsc)
    return jsonify({
        'ifsc': branch.ifsc,
        'branch': branch.branch,
        'address': branch.address,
        'city': branch.city,
        'district': branch.district,
        'state': branch.state,
        'bank': {
            'id': branch.bank.id,
            'name': branch.bank.name
        }
    }) 