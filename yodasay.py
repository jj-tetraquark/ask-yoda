from requests_futures.sessions import FuturesSession
from dispatch import deliver
from requests_futures_ext import AsyncSession
import datetime
import re

mashape_api = "https://yoda.p.mashape.com/yoda"
mashape_key = "OsmmBOCm2pwcc3497yJf4sv7XHTzZImH"

def yoda_handler(sess,resp):
  question = sess.obj
  question.answer = re.sub(r'(?i)cleverbot', r"Yoda", resp.text)
  print "%(response)s delivered at %(time)s" % {"response":question.answer, "time":str(datetime.datetime.now())}
  deliver(question)

def yoda_say(question):
  session = AsyncSession()
  session.obj = question
  answer = correct_textspeak(question.answer)
  answer = add_fullstop(answer)
  parameters = {"sentence":answer}
  heads = {'X-Mashape-Authorization':mashape_key}
  call = session.get(mashape_api, params=parameters, headers=heads, background_callback=yoda_handler)

def correct_textspeak(text):
  text = re.sub(r'(?i)(?:\bdont)', r"don't", text)
  text = re.sub(r'(?i)(?:\bhasnt)', r"hasn't", text)
  text = re.sub(r'(?i)(?:\byoure)', r"you're", text)
  text = re.sub(r'(?i)(?:\bhavent)', r"haven't", text)
  text = re.sub(r'(?i)(?:\bur)', r"your", text)
  text = re.sub(r'(?i)(?:\bu)', r"you", text)  
  return text

def add_fullstop(text):
  if text[-1] != "." and text[-1] != '?' and text[-1] != '!':
    text = text + "."
  return text

#yoda_say("Where is the secret Rebel Base?")