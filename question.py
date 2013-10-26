from yahoo import yahoo_ask

class Question:
  answer = "default answer this is"

  def __init__(self, message, number):
    self.message = message
    self.number = number

  def ask(self):
    yahoo_ask(self)
