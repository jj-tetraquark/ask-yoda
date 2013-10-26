import re

class Question(object):
  def __init__(self, message, number):
    self.message = message
    self.number = number

  def message_for_yahoo(self):
    sanitized_message = re.sub(r'?', '', self.message)
    return sanitized_message


