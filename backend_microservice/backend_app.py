from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline';"
    return response

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('instance/contacts.db')
    return conn

# Get all contacts
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return jsonify(contacts)

# Add a new contact
@app.route('/api/add_contact', methods=['POST'])
def add_contact():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                   (data['name'], data['phone'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact added successfully!"})

# Edit an existing contact
@app.route('/api/edit_contact/<int:contact_id>', methods=['PUT'])
def edit_contact(contact_id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
                   (data['name'], data['phone'], data['email'], contact_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact updated successfully!"})

# Delete a contact
@app.route('/api/delete_contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact deleted successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)