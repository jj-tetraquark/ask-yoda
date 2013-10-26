from yahoo import yahoo_ask

class Question:
  answer = None

  def __init__(self, message, number):
    self.message = message
    self.number = number

  def ask(self):
    yahoo_ask(self)

  def ask_cleverbot(self):
    cleverbot_complete(self)
