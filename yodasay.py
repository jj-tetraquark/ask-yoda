from requests_futures.sessions import FuturesSession
from chatterbot import cleverbot_ponder
from dispatch import deliver
import datetime

api = "https://yoda.p.mashape.com/yoda"
key = "OsmmBOCm2pwcc3497yJf4sv7XHTzZImH"

def yoda_handler(sess,resp,question):
  print "%(response)s delivered at %(time)s" % {"response":resp.text, "time":str(datetime.datetime.now())}
  deliver(resp.text,question.number)

def yoda_say(question):
  cb_message = cleverbot_ponder(question.message)
  session = FuturesSession()
  parameters = {"sentence":cb_message}
  heads = {'X-Mashape-Authorization':key}
  call = session.get(api, params=parameters, headers=heads, background_callback=yoda_handler)

#yoda_say("Where is the secret Rebel Base?")