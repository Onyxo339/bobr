import json
import random

with open('bobr.json') as user_file:
    bobr_data = json.load(user_file)

with open('nora.json') as user_file:
    nora_data = json.load(user_file)


class Loc:
    def __init__(self, jmeno, nazev):
        self.jmeno = jmeno
        self.nazev = nazev
    
    def __str__(self):
        return f"{self.jmeno}({self.nazev})"

bobr_names = [entry['name'] for entry in bobr_data['bobr']]
nora_names = [entry['name'] for entry in nora_data['nora']]

random.shuffle(nora_names)
random.shuffle(bobr_names)

locs = [Loc(bobr_name, nora_name) for bobr_name, nora_name in zip(bobr_names, nora_names)]

for loc_obj in locs:
    print(loc_obj)