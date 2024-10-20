from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Add contact page route
@app.route('/add_contact')
def add_contact_page():
    return render_template('add_contact.html')

# Edit contact page route
@app.route('/edit_contact/<int:id>')
def edit_contact_page(id):
    return render_template('edit_contact.html', contact_id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)