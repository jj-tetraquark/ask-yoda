import re
from requests_futures_ext import AsyncSession
from pprint import pprint # remove this later

yahoo_api_key = "dj0yJmk9SGRNZ3NLVWFNN0hWJmQ9WVdrOVdqWm9ka2RoTXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Mw--"
yahoo_question_url = "http://answers.yahooapis.com/AnswersService/V1/questionSearch"

def yahoo_question_callback(sess, resp):
  response_data = resp.json()
  print("answer: ")
  #need to deal with the response being empty
  sess.obj.answer = response_data["all"]["questions"][0]["ChosenAnswer"]
  print(sess.obj.answer)
  
def yahoo_ask(text_message):
  AsyncSession.obj = text_message
  yahoo_session = AsyncSession()
  question = sanitize_question(text_message) 
  parameters = {"query":question, 
      "search_in":"question",
      "appid":yahoo_api_key, 
      "output":"json",
      "type":"resolved"}
  yahoo_session.get(yahoo_question_url, params=parameters, background_callback=yahoo_question_callback) 

def sanitize_question(message):
  sanitized_message = re.sub(r'\?', '', message.message)
  sanitized_message = sanitized_message.replace(' ', '+')
  return sanitized_message
