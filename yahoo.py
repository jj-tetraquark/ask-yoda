from pprint import pprint # remove this later
from requests_futures.sessions import FuturesSession

yahoo_session = FuturesSession()
yahoo_api_key = "dj0yJmk9SGRNZ3NLVWFNN0hWJmQ9WVdrOVdqWm9ka2RoTXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD00Mw--"
yahoo_question_url = "http://answers.yahooapis.com/AnswersService/V1/questionSearch"



def yahoo_question_callback(sess, resp):
  response_data = resp.json()
  print("answer: ")
  pprint(response_data["all"]["questions"][0]["ChosenAnswer"])
  
def yahoo_ask(question):
  parameters = {"query":question, 
      "search_in":"question",
      "appid":yahoo_api_key, 
      "output":"json",
      "type":"resolved"}
  yahoo_session.get(yahoo_question_url, params=parameters, background_callback=yahoo_question_callback)

