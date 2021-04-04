import json
import os
from pprint import pprint

DIRECTORY = "data"

dir = os.fsencode(DIRECTORY)

def convertMillis(millis):
    seconds = (millis / 1000) % 60
    minutes = (millis // (1000 * 60)) % 60
    hours = (millis // (1000 * 60 * 60)) % 24
    days = (millis // (1000 * 60 * 60 * 24))
    return (seconds, minutes, hours, days)

data = []

for file in os.listdir(dir):
    filename = os.fsdecode(file)

    with open(f"{DIRECTORY}/{filename}", "r") as f:
        for obj in json.loads(f.read()):
            data.append(obj)


total_ms = 0

for obj in data:
    total_ms += obj["msPlayed"]

seconds, minutes, hours, days = convertMillis(total_ms)
print(f"{days}d {hours}h {minutes}m {round(seconds, 3)}s")
