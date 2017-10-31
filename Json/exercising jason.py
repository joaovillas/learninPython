import json

placas = open('sness.json','r')
placas_obj = json.load(placas)

for placas in placas_obj :
    print(placas['Nome'])

