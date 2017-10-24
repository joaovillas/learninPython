import json

placas = open('sness.json','r')
placas_obj = json.load(placas)

print(placas['Nome'])