import os
import re
import question
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Ask Yoda. Seem to be using a browser you are. Text us, you must.'

@app.route('/receive-sms')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
    app.run(port=80)