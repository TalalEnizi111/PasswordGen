from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def generate_password(length=14):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "!@#$%^&*()-_=+<>?/[]{}"
    all_chars = lower + upper + number + symbols

    password = (
        random.choice(lower) +
        random.choice(upper) +
        random.choice(number) +
        random.choice(symbols) +
        ''.join(random.choices(all_chars, k=length - 4))
    )
    return ''.join(random.sample(password, len(password)))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify({'password': generate_password()})

if __name__ == '__main__':
    app.run(debug=True)
