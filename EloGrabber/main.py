from urllib.request import urlopen as uReq
import json

def pegaurl(nome):
    urlid = 'https://br1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+nome+'?api_key=RGAPI-8c9b531b-2997-4f48-b4d7-858a832ae015'
    pagina = uReq(urlid)
    pagina_response = pagina.read()
    pagina.close()

    pagina_json = json.loads(pagina_response)

    id = str(pagina_json['id'])
    return id

def pegaelo(id):
    urltier = 'https://br1.api.riotgames.com/lol/league/v3/positions/by-summoner/'+id+'?api_key=RGAPI-8c9b531b-2997-4f48-b4d7-858a832ae015'

    pagina = uReq(urltier)
    pagina_response = pagina.read()
    pagina.close()


    return pagina_response

nick =str( input('Nick:'))
nick = nick.replace(' ','_')
id = pegaurl(nick)
id = str(id)
pagina = pegaelo(id)
pagina_json = json.loads(pagina)
i=0
while (i<3):
    try:
        if (pagina_json[i]['queueType'] == 'RANKED_FLEX_SR'):
            print('Tipo da fila: Flex')
        elif (pagina_json[i]['queueType'] == 'RANKED_FLEX_TT'):
            print('Tipo da fila: Twisted Tree Line')
        elif (pagina_json[i]['queueType'] == 'RANKED_SOLO_5x5'):
            print('Tipo de fila: Solo Duo')

        print('Nome da Liga:' + pagina_json[i]['leagueName'])
        print('Elo:'+pagina_json[i]['tier']+' '+pagina_json[i]['rank'])
        i+=1
        print('----------------------------------------------------------')
    except (IndexError):
        print('Dado Não Encontrado')
        i+=1