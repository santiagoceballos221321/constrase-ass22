from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    include_uppercase = 'include_uppercase' in request.form
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    characters += string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
