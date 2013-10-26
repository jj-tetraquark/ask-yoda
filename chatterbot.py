from chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()

yodabot = factory.create(ChatterBotType.CLEVERBOT)
yodabot_session = yodabot.create_session()

def cleverbot_ponder(message):
  response = yodabot_session.think(message)
  return response

def cleverbot_ask(text_message):
  text_message.answer = cleverbot_ponder(text_message.message)
  


#we could also use pandorabots
#luke = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
#lukesession = luke.create_session()
