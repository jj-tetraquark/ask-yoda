from requests_futures.sessions import FuturesSession
from dispatch import deliver
from requests_futures_ext import AsyncSession
import datetime

mashape_api = "https://yoda.p.mashape.com/yoda"
mashape_key = "OsmmBOCm2pwcc3497yJf4sv7XHTzZImH"

def yoda_handler(sess,resp):
  question = sess.obj
  print "%(response)s delivered at %(time)s" % {"response":resp.text, "time":str(datetime.datetime.now())}
  deliver(resp.text,question.number)

def yoda_say(question):
  session = AsyncSession()
  session.obj = question
  # covers cases of timeout or no response from Yahoo Answers
  parameters = {"sentence":question.answer}
  heads = {'X-Mashape-Authorization':mashape_key}
  call = session.get(mashape_api, params=parameters, headers=heads, background_callback=yoda_handler)

#yoda_say("Where is the secret Rebel Base?")
