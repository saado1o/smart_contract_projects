from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from blockchain import Blockchain  # Import your Blockchain class

# Initialize Flask app and extensions
app = Flask(__name__, static_folder='static', static_url_path='/assets')
blockchain = Blockchain()  # Instantiate Blockchain object
app.secret_key = 'your_secure_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Linkin.1234@127.0.0.1/smart_contract_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from blockchain import Blockchain

# Define Models
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, nullable=False)
    target_id = db.Column(db.Integer, nullable=False)
    relationship_type = db.Column(db.String(255), nullable=False)
    source_type = db.Column(db.String(255), nullable=False)
    target_type = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/view_blockchain', methods=['GET'])
def view_blockchain():
    chain = blockchain.get_chain()  # Fetch blockchain data
    return render_template('view_blockchain.html', blockchain=chain)


@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain = blockchain.get_chain()
    return jsonify(chain)

@app.route('/view_supply_chain', methods=['GET'])
def view_supply_chain():
    relationships = Relationship.query.all()
    return render_template('view_supply_chain.html', relationships=relationships)

@app.route('/add_suppliers', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return render_template('add_suppliers.html', suppliers=suppliers)

@app.route('/add_suppliers', methods=['POST'])
def add_suppliers():
    supplier_name = request.form.get('supplier_name')
    if supplier_name:
        try:
            supplier = Supplier(name=supplier_name)
            db.session.add(supplier)
            db.session.commit()
            flash("Supplier added successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
    else:
        flash("Supplier name cannot be empty!", "warning")
    return redirect(url_for('get_suppliers'))

@app.route('/add_manufacturers', methods=['GET'])
def get_manufacturers():
    manufacturers = Manufacturer.query.all()
    return render_template('add_manufacturers.html', manufacturers=manufacturers)

@app.route('/add_manufacturers', methods=['POST'])
def add_manufacturers():
    manufacturer_name = request.form.get('manufacturers_name')
    if manufacturer_name:
        try:
            manufacturer = Manufacturer(name=manufacturer_name)
            db.session.add(manufacturer)
            db.session.commit()
            flash("Manufacturer added successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
    else:
        flash("Manufacturer name cannot be empty!", "warning")
    return redirect(url_for('get_manufacturers'))

@app.route('/add_buyers', methods=['GET'])
def get_buyers():
    buyers = Buyer.query.all()
    return render_template('add_buyers.html', buyers=buyers)

@app.route('/add_buyers', methods=['POST'])
def add_buyers():
    buyer_name = request.form.get('buyer_name')
    if buyer_name:
        try:
            buyer = Buyer(name=buyer_name)
            db.session.add(buyer)
            db.session.commit()
            flash("Buyer added successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
    else:
        flash("Buyer name cannot be empty!", "warning")
    return redirect(url_for('get_buyers'))

@app.route('/add_relationship', methods=['GET'])
def get_relationship_form():
    suppliers = Supplier.query.all()
    manufacturers = Manufacturer.query.all()
    buyers = Buyer.query.all()
    return render_template(
        'add_relationship.html',
        suppliers=suppliers,
        manufacturers=manufacturers,
        buyers=buyers
    )

@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    source_id = request.form['source_id']
    target_id = request.form['target_id']
    relationship_type = request.form['relationship_type']
    source_type = request.form['source_type']
    target_type = request.form['target_type']
    
    new_relationship = Relationship(
        source_id=source_id,
        target_id=target_id,
        relationship_type=relationship_type,
        source_type=source_type,
        target_type=target_type
    )
    try:
        db.session.add(new_relationship)
        db.session.commit()
        flash("Relationship added successfully!", "success")
    except Exception as e:
        flash(f"An error occurred: {e}", "danger")
    return redirect(url_for('get_relationship_form'))

@app.route('/fetch_relationships', methods=['GET'])
def fetch_relationships():
    relationships = Relationship.query.all()
    relationship_list = []
    for relationship in relationships:
        source_name, target_name = None, None
        if relationship.source_type == 'Supplier':
            source_name = Supplier.query.get(relationship.source_id).name
        elif relationship.source_type == 'Manufacturer':
            source_name = Manufacturer.query.get(relationship.source_id).name
        elif relationship.source_type == 'Buyer':
            source_name = Buyer.query.get(relationship.source_id).name
        
        if relationship.target_type == 'Supplier':
            target_name = Supplier.query.get(relationship.target_id).name
        elif relationship.target_type == 'Manufacturer':
            target_name = Manufacturer.query.get(relationship.target_id).name
        elif relationship.target_type == 'Buyer':
            target_name = Buyer.query.get(relationship.target_id).name
        
        relationship_list.append({
            'id': relationship.id,
            'source_name': source_name,
            'target_name': target_name,
            'relationship_type': relationship.relationship_type
        })
    
    return jsonify(relationship_list)


@app.route('/fetch_sub_categories', methods=['GET'])
def fetch_sub_categories():
    category = request.args.get('category')
    result = []
    if category == 'Supplier':
        members = Supplier.query.all()
        result = [{'id': member.id, 'name': member.name, 'type': 'Supplier'} for member in members]
    elif category == 'Manufacturer':
        members = Manufacturer.query.all()
        result = [{'id': member.id, 'name': member.name, 'type': 'Manufacturer'} for member in members]
    elif category == 'Buyer':
        members = Buyer.query.all()
        result = [{'id': member.id, 'name': member.name, 'type': 'Buyer'} for member in members]
    return jsonify(result)

@app.route('/add_transaction', methods=['GET'])
def get_add_transaction_form():
    relationships = Relationship.query.all()
    return render_template('add_transaction.html', relationships=relationships)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.form
    relationship_id = data.get('relationship_id')
    amount = data.get('amount')
    remarks = data.get('remarks')

    if not relationship_id or not amount or not remarks:
        return jsonify({"error": "Missing transaction details"}), 400

    # Fetch relationship details from Relationship table
    relationship = Relationship.query.get(relationship_id)

    if not relationship:
        return jsonify({"error": "Invalid relationship"}), 400

    sender_id = relationship.source_id
    receiver_id = relationship.target_id

    try:
        transaction = blockchain.add_transaction(sender_id, receiver_id, amount, remarks)
        return jsonify({"message": "Transaction added successfully", "transaction": transaction}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to add transaction: {str(e)}"}), 500


# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't already exist
    app.run(debug=True)
