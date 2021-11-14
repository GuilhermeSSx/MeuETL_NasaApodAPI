import requests
import csv

# https://api.nasa.gov/

NASA_API_KEY = 'oONPThyXOgkfrFhRR9SqGChI0DF2wr7MrSS5Rngp'
url = 'https://api.nasa.gov/planetary/apod?api_key='

start_date = '&start_date=2021-11-01'
end_date = '&end_date=2021-11-14'

r = requests.get(url + NASA_API_KEY + start_date + end_date)
dados_json = r.json()

status = r.status_code
print(f'status code da API: {status}')

lista_registros = []

# Processa os dados
for registro in dados_json:
    titulo = registro.get('title')
    data = registro.get('date')
    if registro.get('media_type') == 'video':
        link = registro.get('url') # link video youtube
    else:
        link = registro.get('hdurl') # link imagem
    explicacao = registro.get('explanation')
    lista_registros.append([titulo, data, link, explicacao])
    
# Cria o arquivo CSV / com os dados da lista    
with open(r'C:\Users\Administrador\Desktop\Napp_Academy\MeuETL_NasaApod\NasaDados.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';', lineterminator='\r' )
    writer.writerow(["titulo", "data", "link_imagem_video", "explicacao"])
    for dados_processados in lista_registros:
        writer.writerow(dados_processados)


