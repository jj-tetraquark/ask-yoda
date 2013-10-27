import os
import re
import redis
from question import Question
from flask import Flask
from flask import request

app = Flask(__name__)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

@app.route('/')
def index():
  hello = ("<!DOCTYPE html><html style='background:#333;'><body style='font-family:courier, sans-serif;color:#FDFDFD;'><h1 style='font-size:2em;width:80%;margin:0 auto;text-align:center;'>Welcome to Ask Yoda. Seem to be using a browser you are. Text us, you must.</h1><h2 style='font-size:1.4em;text-align:center;border-bottom:1px solid #FDFDFD;width:72.5%;margin:0 auto;padding-bottom:10px;margin-bottom:10px;'>&rarr; &plus;44 7860 033 028</h2>"
          "<p style='font-size:4.8px;margin:0 auto;text-align:center;'>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "....................................................................................................................:=++??++:,..................................................................................................................................................................................................<br>"
          "....................................................................................................................=+????+??+=~=++~............................................................................................................................................................................................<br>"
          "...................................................................................................................,++++++??????+++???~.........................................................................................................................................................................................<br>"
          "..................................................................................................................=+++++?????????????+?+=,......................................................................................................................................................................................<br>"
          "................................................................................................................,~++++???++??????????++++=~~,...................................................................................................................................................................................<br>"
          "...........................................................................................................,~=???++==~~=+++++++++++++??+++++++==:...............................................................................................................................................................................<br>"
          "........................................................................................................~??????+++==~~~~=+??+?+++++=++???++??????+:.............................................................................................................................................................................<br>"
          "........................................................................................................~+????++==========+??++=++?+=???????????+:..............................................................................................................................................................................<br>"
          "........................................................................................................=????++++=~~~=~=~+++??++=+=+++???????????=,.............................................................................................................................................................................<br>"
          ".......................................................................................................~???+======:~~~=====++++===+==+??????II?+??=:............................................................................................................................................................................<br>"
          "......................................................................................................,=??++=====~~=~~==~=~==?+=+=+==++?+???????????~...........................................................................................................................................................................<br>"
          "......................................................................................................=???++==~===~~::~~==~~=++++====+??+??+??I??++++=,................~+=?+....................................................................................................................................................<br>"
          "..........................................................................~++=++++=++~,..............:???+==~~~~~~~~~:~~~~=~~=??+==+=?????+?++????++??++=~:,........:===~:~~,...................................................................................................................................................<br>"
          ".........................................................................,:~::,,,:=~==++=~,.........:???+=====~~~~~~~~:~=~~~~~+++=~~~+??=+??++????????+++==~......:~~=::~:......................................................................................................................................................<br>"
          "............................................................................,,,,,.,,:~=+====~:......+???+===~~~~~~=~~~~~~~~~=~====~=~=+?+++???I????????++=+==~..:~~=~:::~.......................................................................................................................................................<br>"
          "...............................................................................,,,,,,,,:===+=+==++++??+?+===~~~~~~~~===~:~==~~=??+===+?+???+++??????+??+++=+=~=====~,,:==~~:,,,:++~~=+????+?==:.........~?I?....................................................................................................................<br>"
          "................,................................................................,,,,,,,,,~~~~~==+=++=+====~=~~~:~=~~~======~==+???==+?????????????I???????++=+==+~:,:=+++====+++?++++?I??+++??+~::~+=~==++:....................................................................................................................<br>"
          "................~...................................................................,,,,,,,.,:===~~==+++=+==~~~::~~~~=====~==~=+?+++==?+??+++??+???II?????????+?=~~::~+++===++====++===+++++++++++++===~~:,.....................................................................................................................<br>"
          "................~:...................................................................,,.,.,..,.,~~=+=+=++=+=~:::::~~~~~~=+=~~~~~===+++?++=++????+???I???????++=:::::~=+?+==++===~=++=====++++++=====~:,.........................................................................................................................<br>"
          "................~~..............................................................:=??++=,,.,,,,...,:~++======:~:,::~~~~~=+=~===++++=++?????+++++?????+???++??=:~~::::===+++======:~=+========++====~,,:..........................................................................................................................<br>"
          "................=~..............................................................+??????+~..,,,,.,..,~=+=~~~~:~:::~~~~~===++===++??==+?????=+??????+?+????+=~~::::,~=:~+=++======::~=======+++===~==:,,..........................................................................................................................<br>"
          "...............,=~,..................................................,==,:=+,..,+??++++III.,,,,,,,,.,:~=~~:~:::::~~~~~~==+++=~=+??+=++???+=????+?++?++??======:::~===~+~======~~:,:~++========~:::=++=..........................................................................................................................<br>"
          "...............,==:.................................................~~==?+====,,+?+++=++?I7=,.,,,,,...,:=~:,,::::~::::~~~==+==~=+?+==+??+=++??++++++++?==+==+=~:==~==+=~====~~~~::~~++======~:,:,,~~+?+.........................................................................................................................<br>"
          "..............,:=~~........................................:+?+????+===~+?===+=:+?+++==?I?I?I~,,,,..,,:,:~~,,,,,::::,::~~=====~~+++~=+??=++=+++++=++++?+====~~~=+~,:=+=~==~~~~~~:~~~=====~~~,,.....,:=+=........................................................................................................................<br>"
          ".............,,~===,....................................~++++?????++++===+++==~~+?++=~=?II+I??:,,,,,,:,,,,::,,,,,::::,,,:~~~~~~~===~~=++==+=+=+===++++??+====+++=:,:~+~~=~=~~~:~~~~===~~~~,,,...................................................................................................................................<br>"
          "............,,,~===,.................................,=++++??????+++++====+?=~:~++++=~=III?I?=~~::~::,,,,::,,,,,,,:::~~~::,,:::::~~:~~=~=~~~~=+?++==++?+==~=~=,:?:::=~~~==~~:::~~=====~=:,,,....................................................................................................................................<br>"
          "............,,,~==~:...............................:===+=+??++++++++++====+++=~~~+++=~=??++++=~:::::,,..,,,,,,,,,,,:::::~:,,,,,,,,:,::::,:::~=+=+??+?+?=~=:~++.:+=:~=~~~~~::::~~=====~~,,,,.....................................................................................................................................<br>"
          "...........,,,,~=~=~.............................:=~======++======++++++====++~~:=++==~:::::~~~:,,,......,,,,,,,,,,~:,,,==,,.,,,::~~::,,:::,.:=+:+?+?+=,,~~=++,.==~~=~:~~::~~~~~::~=:,,,,.......................................................................................................................................<br>"
          "...........,,,,:===~....................:~+=+~.,~~~=========++======+++++=====+++?+==:,,,,...,,,,,,......,,:::,,,,::~=====:,,,,::~=+=~~:::~==+++++++??~~~:,:~~==?=~=:~~~~:~~~:,,,~,,,,,,........................................................................................................................................<br>"
          "..........,,,,,,====.................,~=====+++++======~~~~=========+?+++++++?+++=~:::,,,,.....,,,.,......,,::::,:,,,,:::~~~:,::~~++++~~:::::::~++++??~====~~~~:~==?~~~:~::..,,::,,,,,..........................................................................................................................................<br>"
          "..........,,,,,,====~:~=++??:......~========++===++?+=++=~~~=======+=========+++===,:,,,,,.....,,,..,.....,::~~~::,::~~~==~~::~~~=+????+~~:~~~~~~==+++~===~~~===~~:~=+:,..,:::::,,,:,...........................................................................................................................................<br>"
          "..........,,,,,,:===++++++++++??+++++===========~~~===+====~~~===~~~++=~~~~~====~=~~~:~~==:~,,,..,,.,,.....,:::~~~::::::::~:,,::::~~+===+=====~~====~.,:=+~:,::~~~~::~=+,,:~~~:,::,.............................................................................................................................................<br>"
          "..........,,,,,,,:+++===++++++===++???++==~~~~~~~=~~~~========~~::++?+==~:~~~~++~~~==+:,::~~~:.,..,,.,,.....,,::::::::::~~::::::,::~==++++=~=~===~~=~~.,=+~::::,,,:~~:::=+=~:::,................................................................................................................................................<br>"
          "............,,,,,,:+++=~=====+++++==++??+=====~~===~~~==~~::::::==++++++~:~~:===+=~=++++:,,:~~,.,,,,,,,.......,,,,:,,:::::::~~~~~==+++=+++==~~~~~~=~=~,,==+~:::::::,,:::~~++++..................................................................................................................................................<br>"
          "..............,,,,,:+++=~~=~====++??++++=+++++=======~=~:::~:~++??++====++==~~===+~~==+===~::=~,,,,,,.:,,.....,,,,,,:::,,:::~:~~~====+==++++~:~~~~==~,,,~==~:,,,,:,,..,,,.......................................................................................................................................................<br>"
          "................,,,,:=++=~~=========++++++++++++=====+==:~~==++++?????========~=+=~~~=====~:,~=:.,.,,,.~.......,,,,,,::,,:::~:::::~~=+=++?++=~~~~====,,:~~::::,,..............................................................................................................................,,.,..............................<br>"
          "..................,,,,:++?~~============+??++++???++++++++++++++++????=+==~========~~~====~~:,=~,,,,,,.~~,..,,..,,,,,,,,,,:,,,,,::::~~::,~+~=~~=====+,,:......................................................................................................................,,::~==+??II7777777777~...........................<br>"
          "....................,,,,~+??=~~==+=========+++???++???+=+=++++=+===+++=+=+=========~~~======~:~=:,,,,,,~~:,,,,,,..,,,,,,,:::::::::~~=~=??+~,,,~~===++:.....................................................................................................,,,::~==++??II777777777777777777777777777~...........................<br>"
          "......................,,:,~++?=~~::~~~~~~=~====++???=+========+=====++?+====~~======~~======~:~=~,,,,,,~~~:,,,,,,,,,,.,:::::::::::::::~~~::,,:=======....................................................................................,,:::~==++??II77777777777777777777777777777777777II??++=~:,............................<br>"
          "..........................,,~=+++~~~~~~==~~~~::~========~~==++++=====++??===~=============~=~::~~:,,,,,~~=~:,,,,,,,,,,,,,,::::::::::~~==:::::========...................................................................,,::~~=+++?III7777777777777777777777  777777777777II??++=~~:,,..........................................<br>"
          ".............................,:~+++++=:~,:::,:~::~====~~==++???I?I+++++??II+========~~======~~:~:,,,,,,=====::,,,,,,,,,,:::,::::::::~~::::~~======++,..................................................,::~~==++??II777777777777 77  7   7  7777777777777III??+==~:,,,..........................................................<br>"
          ".................................,~=:,:,::::::::~:::~:~~~==+????????????II?I========~==~==~~~~:~,,,,,,:+=+=+~~~:,,::::::,:~~~~:::~~~~~~~========++++.................................,,:~~==++??III77777777777777777777777777777777777777III??++==~:,,..........................................................................<br>"
          "..................................:,,::,,,,,,:,:,,+++?=::,~=?+??????+???????+==========~=~~~~:::::::::==++++====::::::::::::~~=========+=======++++~...............,,,:~==++??III777777777777777 7777777777777777777777777II??+==~::,...........................................................................................<br>"
          "..................................,::,.......,..~~=+++++~:~===+????+??I?I?????======~====~~~~:::::::::+++++++==~~~~~~~~~~~~~~~~=++++=+=+++++++?????=~~==++??III777777777777777777777777777777777777777777777II++=~::,...........................................................................................................<br>"
          ".................................:,.,,....,,..,:::~====~=~~===++++++=:=????????++===~====~~~~::::::~~=++++++=+=~~~~~=========++++???IIIII777777777777777777777777777777777777777777777777777IIII+=~::,,,,.......................................................................................................................<br>"
          "................................,,,,.....,,,,.,,::~===::~====+?+=++++=,~=???++++++=======~~~~~~~~~~~+??+????+?===+++?????IIII777777777777777777777777    7777777  777777777777777I?+=~~:,,,,....................................................................................................................................<br>"
          "...............................,,,..........,,,,,:~~~~:,:~~~~=++++=+=+?:,:??+++++++=============++??IIII77777777777777 7777 77  77  777777777777777777777777777I?++==~:,,,,,....................................................................................................................................................<br>"
          "...............................,.,........,...,.:~~===::,::~~~~=++=~:::~~~~~~~~~:~,:~?7III7777777777777777777777777777 7777 777777 7777777777777IIII??????????=.................................................................................................................................................................<br>"
          "...............................,,,.............,::~===~:,,:::~==++~:::~~+?IIII++.,,:+I777777777777777777777777777777777777777777IIII???????++++=~~==========++++:...............................................................................................................................................................<br>"
          "..............................,,:::,::::~~~::,,,:~~=~~~:,:~===~++=::::~~~:~~~~~~::==~=+?77777777777777777777777IIII?????++++++++++=====+++====~~~~==~~~~=~====+++?,.............................................................................................................................................................<br>"
          ".............................,:~:...............::~::~=~,.:=++I:=~,,::::::=~~:~~~~~~~~~=?7777777III???++++=============================~~====~::~=~~~~~~~~=====++++~............................................................................................................................................................<br>"
          ".............................:~?......,,:~=+???=,,,,::::,.:~+??~?~,,:,,:,,,:::::,,=~~~~=+?++++==~~~~~~~~~~~~~~~~~~~~~~~~~~~~=======~~~~~=~~~~:::~~~:::~~~~=~======++~...........................................................................................................................................................<br>"
          ".............................,=:777777777777II=~:::::~:::~:,+??:,,,=+?I77II?????=~=?++==+=,..=~~~~::::~~~~::::::~~~~~~~~~~~~~~~~~~~:~~~~~~~~:::~~~::::~~~~~~~=====++++,.........................................................................................................................................................<br>"
          ".............................::I=~,,,,,,,,,,,,,,:~~.:~~:....:~=+====~~~==+=,.,,,,::,.......,::::::::::::::::::~~~~~~~~~~~~~~~~~~:~~~~~~~~~::,:~~::,::::::~~~~~~~~~==++?~........................................................................................................................................................<br>"
          ".............................,:::~+?II??+=~:,,,,,.+~..,:????++==++++=~~:~==:,,::::.........,,,,,,:::::::,,::::::::~~~~~~~~~~:::~~~~~~~~~:::,:~::,,::::::::::::::::~~==++,.......................................................................................................................................................<br>"
          "..............................:~7I:,:~::................=?II??I?==+=++==~=+:::::,.........,,,,,,,,,,::::::::::::::~::~:::::::~~~~~~~~~~:,,,,:::,,,:::::::,::::::::::~~=++,......................................................................................................................................................<br>"
          ".................................,:,::,,..................=+????+==~=+====::,............,,,,,,,,,,,,,,:::::::::::::::::::~~~~~~~::::::,,,:,,,,,,:::,,,,,,,,,,,,,,,:::~~===,....................................................................................................................................................<br>"
          ".....................................,,,,,..................,,::::::~=~~=~..............,,,,::::,,,,,,,,::::::::::::::::::::::::::::,::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::::~~==+=~,................................................................................................................................................<br>"
          "......................................,,,................,.,,,,,,,,:~~~=,..............,,,,::::::::::,,,..,::,,:::,:,:::::::::::,,:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::~~~=+++++=:............................................................................................................................................<br>"
          "........................................,,,,........,,,,,,,,,,,:~~~~~~,...............,,,,:::::::::::::,,.....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:::~~===+++=+=:.........................................................................................................................................<br>"
          "...........................................,,,,,,,,,,,,,,,,,,,~~~=~~,.................,,,,,:::::::::::::::::,,.....,,,,,,,,:,,,,,,,......,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:,:~~~==++====~........................................................................................................................................<br>"
          "..............................................,,,,,,,,,,,.,,::~~:,....................,,,,::::::::::::::::::::,,,,,,,,,,,,,,....................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:~~======~.........................................................................................................................................<br>"
          "..................................................,,,,,,,,,::.........................,,,,:::~:::::::~~~~~::::::,:,,:::,..,........................,,,,,,,,,,,,,,,,,,,,,,,,,,,,:~~====::........................................................................................................................................<br>"
          "........................................................,,,............................,,,::::~~~~~:~~::~~:~~~~~::::,.,,..,.............................,,,,,,,,,,,,,,,,,,,,,,,,:~===~~~:,......................................................................................................................................<br>"
          "........................................................................................,,,,::::~~~~~~~~~~::,,,,,,,::::,..,................................,,,,,,,,,,,,,,,,,,,,,::~~~~~~~~,.....................................................................................................................................<br>"
          "........................................................................................,,,,,::::::::::::::::::~:::,::....,..................................,,,,,,,,,,,,,,,,,,,,::::~==++=:=:..................................................................................................................................<br>"
          ".........................................................................................,,,,,,:::::::~~~~~~~::,,:::::,,,.,...................................,,,,,,,,,,,,,,,,,,,:~:~~==++~~===:................................................................................................................................<br>"
          "..........................................................................................,,,,,,,,,,,,,,,,,:::::::::::::::......................................,,,,,,,,,,,,,,,:==+==+=+++=~~=~~=:..............................................................................................................................<br>"
          ".............................................................................................,:::::::::::::::::~::~~~~~~::,........................................,,,,,,,,,,:::~~=+++=+++~::~:~=+..............................................................................................................................<br>"
          "..................................................................................................:,,,,,,,,:::::~~::~:~:~:,..........................................,,,,,,,:::::~===~====~,....................................................................................................................................<br>"
          "..................................................................................................,,,....,,,,,,:::::~:::~::...........................................,,,,,,,,:::::~~~=====~....................................................................................................................................<br>"
          "...........................................................................................................,,,,::::~,,:::::.............................................,,,,,::::,:::::~~~==+~..................................................................................................................................<br>"
          "..........................................................................................................,,,,.,::,..,,:~~,..............................................,,,.,:~::::::,:~===++=.................................................................................................................................<br>"
          ".........................................................................................................,,,:,::::....,,::................................................,,,,~~~~::::,,:~====++................................................................................................................................<br>"
          "........................................................................................................,,::~~::,.....,,~~..................................................,,~~~~::::::,,,~==+==,..............................................................................................................................<br>"
          "........................................................................................................,:::~::,.......,~~.................................................,,,:~~~::,,:::,,,,:==++..............................................................................................................................<br>"
          "........................................................................................................,:::::..........:...................................................,,::~~~:,,,,,,::::::==~.............................................................................................................................<br>"
          ".........................................................................................................,:::,..............................................................,,:~=~~,.......,,,,,,~=,............................................................................................................................<br>"
          ".........................................................................................................,::.................................................................,::~~~.............,,=+............................................................................................................................<br>"
          ".........................................................................................................,:...................................................................,,~~~.............................................................................................................................................<br>"
          "...............................................................................................................................................................................,:~~~............................................................................................................................................<br>"
          "................................................................................................................................................................................,:+?............................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................<br>"
          "................................................................................................................................................................................................................................................................................................................................</p>"
          "<p style='text-align:center;'>Made by @jonnyjdark &amp; @hipsters_unite in Manchester, UK.<br><br><audio loop='loop' autoplay='false' controls='controls'><source src=\"http://cprouvost.free.fr/fun/generiques/--%20Film%20--/Film%20-%20Star%20Wars%20Episode%201%20%28Duel%20Of%20The%20Fates%29.mp3\" /></audio></p>"
          "</body></html>")
  return hello

@app.route('/receive-sms')
def accept_input():
  content = request.args.get('content', '')
  number = request.args.get('from', '')
  question = Question(content,number)
  question.ask()

  # debug statements below
  print("%(content)s from %(number)s." % {"content": question.message, "number": question.number})
  return "%(content)s from %(number)s." % {"content": question.message, "number": question.number} 

if __name__ == '__main__':
    app.run(port=8080, debug=True)
