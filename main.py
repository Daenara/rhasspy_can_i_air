import configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import HermesApp, EndSession, TopicData

config = configparser.ConfigParser()
config.read('config.ini')
client = config["mqtt"]["client"]
server = config["mqtt"]["server"]
port = config["mqtt"].getint("port")
user = config["mqtt"]["user"]
password = config["mqtt"]["password"]

app = HermesApp(client, host=server, port=port, username=user, password=password)

temperatures = {}


@app.on_topic("weather/+/{position}/temperature_*C")
async def on_temperature_update(data: TopicData, payload: bytes):
    temperatures[data.data['position']] = float(payload.decode('UTF-8'))


@app.on_intent("CanIAir")
async def can_i_air(intent: NluIntent):
    """Can I open the window to air"""
    slots = intent.to_dict()["slots"]
    if len(slots) == 0:
        value = config["rhasspy_can_i_air"]["default"]
    else:
        value = slots[0]["value"]["value"]
    if value in temperatures.keys():
        delta = max(temperatures["front"], temperatures["back"]) - temperatures[value]
        if delta <= 0:
            return EndSession("Ja")
        elif delta <= 2:
            return EndSession("Wenn es sein muss")
        else:
            return EndSession("Nein")
    return EndSession("Keine Ahnung")

app.run()


