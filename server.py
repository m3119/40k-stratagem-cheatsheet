from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/antti')
def antti():
    return 'hodor'

@app.route('/antti')
def apinakontti():
    return 'däh'