from yahoo import yahoo_ask
from chatterbot import cleverbot_ask

class Question:
  def __init__(self, message, number):
    self.message = message
    self.number = number
    self.answer = None

  def ask(self):
    if len(self.message) < 15:
      cleverbot_ask(self)
    else:
      yahoo_ask(self)

  def ask_cleverbot(self):
    cleverbot_complete(self)
