import requests
import json

# API DO IPMA
# Previsão do risco de incêndio — RCM
URL_RCM_D0 = "https://api.ipma.pt/open-data/forecast/meteorology/rcm/rcm-d0.json"     # hoje
URL_RCM_D1 = "https://api.ipma.pt/open-data/forecast/meteorology/rcm/rcm-d1.json"     # amanhã

def _risco_incendio_d0():
    '''Puxar o identificador único de concelho (DICO) e o risco de incêndio respectivo.
    Retorna um dicionário. A chave é o código DICO do concelho e o valor é o risco de incêndio.'''
    
    try:
        dados = requests.get(URL_RCM_D0, timeout=10).json()['local']
        return {info['dico']: info['data']['rcm'] for info in dados.values()}
    except Exception as e:
        print(f"Erro ao obter a informação de risco de incêndio: {e}")
        return {}

# chamar a função para obter os dados da API
risco_incendio = _risco_incendio_d0()

# ficheiro com a relação codigo concelho distrito
with open('static/data/codigos-concelho.json', 'r', encoding='utf-8') as f:
    concelhos_dados = json.load(f)

# associar o codigo DICO aos concelhos e distritos
mapa_concelhos = {dado['DICO']: {'CONCELHO': dado['CONCELHO'], 'DISTRITO': dado['DISTRITO']} for dado in concelhos_dados}

mapa_dados = {}

for dico, risco in risco_incendio.items():
    if dico in mapa_concelhos:
        distrito = mapa_concelhos[dico]['DISTRITO']
        concelho = mapa_concelhos[dico]['CONCELHO']

        # para o caso do distrito ainda não estar no mapa_dados abre um dicionário para esse distrito
        if distrito not in mapa_dados:
            mapa_dados[distrito] = {}
        
        mapa_dados[distrito][concelho] = {
            'dico': dico,
            'rcm': risco
        }