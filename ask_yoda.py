import os
import re
from question import Question
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Ask Yoda. Seem to be using a browser you are. Text us, you must.'

@app.route('/receive-sms')
def accept_input():
  content = request.args.get('content', '')
  number = request.args.get('from', '')
  question = Question(content,number)
  # debug statements below
  print("%(content)s from %(number)s." % {"content": question.message, "number": question.number})
  return "%(content)s from %(number)s." % {"content": question.message, "number": question.number} 

if __name__ == '__main__':
    app.run(port=8080)