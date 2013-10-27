import re
from requests_futures_ext import AsyncSession
from pprint import pprint # remove this later
from yodasay import yoda_say
from chatterbot import cleverbot_ask


yahoo_api_key = "dj0yJmk9SGRNZ3NLVWFNN0hWJmQ9WVdrOVdqWm9ka2RoTXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Mw--"
yahoo_question_url = "http://answers.yahooapis.com/AnswersService/V1/questionSearch"

def yahoo_question_callback(sess, resp):
  response_data = resp.json()
  print('recieved')
  try:
    sess.obj.answer = response_data["all"]["questions"][0]["ChosenAnswer"]
    print(sess.obj.answer)
    yoda_say(sess.obj)
  except: #Gotta catch them all!
    print('Yahoo, you have failed me for the last time. Cleverbot, I choose you!')
    cleverbot_ask(sess.obj)


  
def yahoo_ask(text_message):
  yahoo_session = AsyncSession()
  yahoo_session.obj = text_message
  question = sanitize_question(text_message) 
  parameters = {"query":question, 
      "search_in":"question",
      "appid":yahoo_api_key, 
      "output":"json",
      "type":"resolved"}
  yahoo_session.get(yahoo_question_url, params=parameters, background_callback=yahoo_question_callback) 

def sanitize_question(message):
  sanitized_message = re.sub(r'\?', '', message.message)
  sanitized_message = re.sub(r"\"|\'", '', sanitized_message)
  sanitized_message = correct_textspeak(sanitized_message)
  sanitized_message = sanitized_message.replace(' ', '+')
  sanitized_message = add_fullstop(sanitized_message)
  return sanitized_message

def correct_textspeak(text):
  text = re.sub(r'(?i)(?:dont\s)|(?:\sdont\s)|(?:\sdont)', r" don't ", text)
  text = re.sub(r'(?i)(?:hasnt\s)|(?:\shasnt\s)|(?:\shasnt)', r" hasn't ", text)
  text = re.sub(r'(?i)(?:youre\s)|(?:\syoure\s)|(?:\syoure)', r" you're ", text)
  text = re.sub(r'(?i)(?:havent\s)|(?:\shavent\s)|(?:\shavent)', r" haven't ", text)
  text = re.sub(r'(?i)(?:ur\s)(?:\sur\s)|(?:\sur)', r" your ", text)
  text = re.sub(r'(?i)(?:u\s)(?:\su\s)|(?:\su)', r" you ", text)  
  return text

def add_fullstop(text):
  if text[-1] != ".":
    text = text + "."
  return text
