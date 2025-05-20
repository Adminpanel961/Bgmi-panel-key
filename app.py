from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Function to generate random key
def generate_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_key')
def generate_key_route():
    key = generate_key()
    return jsonify({"key": key})

if __name__ == '__main__':
    app.run(debug=True)
