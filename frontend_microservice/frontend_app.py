from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact')
def add_contact():
    return render_template('add_contact.html')

@app.route('/edit_contact')
def edit_contact():
    return render_template('edit_contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)