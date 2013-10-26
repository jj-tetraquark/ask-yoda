from requests_futures.sessions import FuturesSession
from chatterbot import cleverbot_ponder

api = "https://yoda.p.mashape.com/yoda"
key = "OsmmBOCm2pwcc3497yJf4sv7XHTzZImH"

def yoda_handler(sess, resp):
  print resp.text

def yoda_say(message):
  cb_message = cleverbot_ponder(message)
  session = FuturesSession()
  parameters = {"sentence":cb_message}
  heads = {'X-Mashape-Authorization':key}
  call = session.get(api, params=parameters, headers=heads, background_callback=yoda_handler)

#yoda_say("Where is the secret Rebel Base?")