from clockwork import clockwork
 
api = clockwork.API('143f1e125a46cca4253316cb8600e1c0606b8217')

def deliver(text,number):
  message = clockwork.SMS(
      to = number,
      message = text
      from_name = 'Yoda'
      )
  response = api.send(message)
  if response.success:
    print ("Delivered to number %(number)s, response id: %(response)s" % {"number": number, "response":response.id})
  else:
    print (response.error_code)
    print (response.error_description)