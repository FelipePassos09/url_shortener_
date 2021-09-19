import requests as rq
import csv
#import json
from datetime import date
import pandas as pd

api_key = 'MNwFlIG5wsrLDtx6mqCSeEiRLzO1CmgnsbgbkAGc'
url_api = 'https://kutt.it/api/v2/links'
csv_file = 'database/dados.csv'

def header():
    header = {
        "X-API-KEY":api_key,
    }
    
    return header


def req(method:dict):
    """Define a method and call API endpoint to GET method with parameters passed to function an return a response by endpoint called.

    Args:
        method (dict): a dict with json method by calling API endpoint.
    """
    req = rq.post(url_api,data=call_shortener,headers=header())
    result = req.json()
    
    return result


# Fazendo o request e gerando o link.
with open(csv_file) as database:
    list_archives = csv.reader(database,delimiter=',')
    line_count = 0
    
    
    # Criando DataFrame de destino:
    filename = (f'./database/dataset_{date.today()}.csv')
    dataset = {
    'url':[],
    'name':[],
    'destino':[],
    'length':[]
}
    df = pd.DataFrame(dataset)
    
    
    # Lendo o arquivo e montando o pacote da requisição:
    
    for row in list_archives:
        call_shortener = {
  "target": row[0],
  "description": "",
  "expire_in": "5minutes",
  "password": "",
  "customurl": "",
  "reuse": 'false',
  "domain": ""
}
    # Efetuando as requisições e gravando os resultados:
        response = req(call_shortener)
        if 'error' in response:
            #repo_post = pd.read_csv(filename, delimiter=',')
            newRow = {'url': response['error'], 'name':response['error'], 'destino':response['error'], 'length': response['error']}
            df = df.append(newRow, ignore_index=True)
        else:
            #repo_post = pd.read_csv(filename, delimiter=',')
            newRow = {'url':response['link'],
                      'name':'null',
                      'destino':response['target'],
            }
            df = df.append(newRow, ignore_index=True)
    
    
    # Exportando o resultado:
    
    df.to_csv(filename)