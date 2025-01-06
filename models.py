from . import db  # Import `db` from __init__.py

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
