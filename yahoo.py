import re
from requests_futures.sessions import FuturesSession
from pprint import pprint # remove this later

yahoo_api_key = "dj0yJmk9SGRNZ3NLVWFNN0hWJmQ9WVdrOVdqWm9ka2RoTXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Mw--"
yahoo_question_url = "http://answers.yahooapis.com/AnswersService/V1/questionSearch"

def yahoo_question_callback(sess, resp):
  response_data = resp.json()
  print("answer: ")
  #need to deal with the response being empty
  pprint(sess)
  pprint(response_data["all"]["questions"][0]["ChosenAnswer"])
  
def yahoo_ask(message):
  yahoo_session = FuturesSession()
  question = sanitize_question(message) 
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
