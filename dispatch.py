from clockwork import clockwork
from jinja2 import utils
import redis, os

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)
 
api = clockwork.API('143f1e125a46cca4253316cb8600e1c0606b8217')

def deliver(question):
  text = question.answer
  number = question.number
  message = clockwork.SMS(
      to = number,
      message = truncate_text(text),
      from_name = 'Yoda'
      )
  response = api.send(message)
  if response.success:
    try:
      redis_key = response.id
      print ("Delivered %(message)s to number %(number)s, response id: %(response)s" % {"message":text, "number": number, "response":response.id})
      xss_safe_question = str(utils.escape(question.message))
      q_and_a = "Q: %(question)s <br>Yoda: %(answer)s" % {"question": xss_safe_question, "answer": text}
      # write to database
      redis.set(redis_key, q_and_a)
      redis_value = redis.get(redis_key)
      print ("Redis saved value: %(val)s" % {"val":redis_value})
    except Exception as e:
      print("Exception " + e.__class__.__name__)
      print(e.args)
  else:
    print (response.error_code)
    print (response.error_description)

def truncate_text(text):
  #459 is the max text length
  max = 459
  if len(text) > max:
    text = text[:max]
    last_full_stop = text.rfind(".") 
    if(last_full_stop > 0):
      text = text[:last_full_stop+1]
  return text
