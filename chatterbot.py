from chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()

yoda = factory.create(ChatterBotType.CLEVERBOT)
yodasession = yoda.create_session()

def cleverbot_ponder(message):
  response = yodasession.think(message)
  return response

#we could also use pandorabots
#luke = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
#lukesession = luke.create_session()