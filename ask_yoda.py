import os
import re
import question
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Ask Yoda. Seem to be using a browser you are. Text us, you must.'

@app.route('/receive-sms')
def accept_input():
  question = Question.new(
    request.args.get('content', ''),
    request.args.get('from', '')
    )
  print question.message
  print question.number

if __name__ == '__main__':
    app.run(port=8080)