from yahoo import yahoo_ask

class Question:
  def __init__(self, message, number):
    self.message = message
    self.number = number
    self.answer = None

  def ask(self):
    yahoo_ask(self)

  def ask_cleverbot(self):
    cleverbot_complete(self)
