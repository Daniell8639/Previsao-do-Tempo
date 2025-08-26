import requests
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    city_name = input('Qual e o nome da cidade: ')
    if city_name.strip().lower() == 'sair':
        print('Saindo...')
        break

    url = f'https://wttr.in/{city_name}?format=j1&lang=pt'
    
    link = requests.get(url)
    dados = link.json()

    if link.status_code == 200:
        temperatura = dados['current_condition'][0]['temp_C']
        sensacao_termica = dados['current_condition'][0]['FeelsLikeC']
        humidade = dados['current_condition'][0]['humidity']
        descricao = dados['current_condition'][0]['lang_pt'][0]['value']
        print(f'Clima em {city_name}:')
        print(f'Temperatura: {temperatura}°C')
        print(f'Sensacao Termica: {sensacao_termica}°C')
        print(f'Humidade: {humidade}%')
        print(f'Descriçao: {descricao}')
    else:
        print('Erro na conexão dos dados')
    
    input("\nPressione Enter para consultar outra cidade ou digite Ctrl+C para sair...")
