from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hi'


@app.route('/signup')
def signup():
    return 'hi'


@app.route('/signin')
def signin():
    return 'hi'
