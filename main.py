from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/connect')
def connect():
    return render_template('connect.html')
@app.route('/memories')
def memories():
    return render_template('memories.html')
@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)