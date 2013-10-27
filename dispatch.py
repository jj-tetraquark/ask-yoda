from clockwork import clockwork
from ask_yoda import redisdb
 
api = clockwork.API('143f1e125a46cca4253316cb8600e1c0606b8217')

def deliver(text,number):
  message = clockwork.SMS(
      to = number,
      message = truncate_text(text),
      from_name = 'Yoda'
      )
  response = api.send(message)
  if response.success:
    try:
      redis_key = number
      print ("Delivered %(message)s to number %(number)s, response id: %(response)s" % {"message":text, "number": number, "response":response.id})
      redisdb.set(redis_key, text)
      redis_value = redisdb.get(redis_key)
      print ("Redis saved value: %(val)s" % {"val":redis_value})
    except Exception as e:
      print("Exception " + e.__class__.__name__)
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
