from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

with app.app_context():
    db.create_all()

# List all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    contacts_list = [{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in contacts]
    return jsonify(contacts_list)

# Add a new contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contact added successfully!'})

# Edit a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    data = request.json
    contact.name = data.get('name', contact.name)
    contact.email = data.get('email', contact.email)
    contact.phone = data.get('phone', contact.phone)
    db.session.commit()
    return jsonify({'message': 'Contact updated successfully!'})

# Delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)