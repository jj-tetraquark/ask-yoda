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
  answer = correct_textspeak(question.answer)
  answer = add_fullstop(answer)
  parameters = {"sentence":answer}
  heads = {'X-Mashape-Authorization':mashape_key}
  call = session.get(mashape_api, params=parameters, headers=heads, background_callback=yoda_handler)

def correct_textspeak(text):
  text = re.sub(r'(?i)(?:dont\s)|(?:\sdont\s)|(?:\sdont)', r" don't ", text)
  text = re.sub(r'(?i)(?:hasnt\s)|(?:\shasnt\s)|(?:\shasnt)', r" hasn't ", text)
  text = re.sub(r'(?i)(?:youre\s)|(?:\syoure\s)|(?:\syoure)', r" you're ", text)
  text = re.sub(r'(?i)(?:havent\s)|(?:\shavent\s)|(?:\shavent)', r" haven't ", text)
  text = re.sub(r'(?i)(?:ur\s)(?:\sur\s)|(?:\sur)', r" your ", text)
  text = re.sub(r'(?i)(?:u\s)(?:\su\s)|(?:\su)', r" you ", text)  
  return text

def add_fullstop(text):
  if text[:-1] != ".":
    text = text + "."
  return text

#yoda_say("Where is the secret Rebel Base?")