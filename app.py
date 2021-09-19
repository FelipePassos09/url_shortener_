import requests as rq
import csv
from datetime import date
import pandas as pd

api_key = 'your-key'
url_api = 'https://kutt.it/api/v2/links'
csv_file = 'database/dados.csv'
link_expiration = '999months'

def header():
    """Making header to request.
    """
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


# Making the request and generating links..
with open(csv_file) as database:
    list_archives = csv.reader(database,delimiter=',')
    line_count = 0
    
    
    # Create target dataframe:
    filename = (f'./database/dataset_{date.today()}.csv')
    dataset = {
    'url':[],
    'name':[],
    'destino':[],
    'length':[]
}
    df = pd.DataFrame(dataset)
    
    
    # Reading file an making package of the requisition:
    
    for row in list_archives:
        call_shortener = {
  "target": row[0],
  "description": "",
  "expire_in": link_expiration,
  "password": "",
  "customurl": "",
  "reuse": 'false',
  "domain": ""
}
    # Request and record responses:
        response = req(call_shortener)
        if 'error' in response:
            newRow = {'url': response['error'], 'name':response['error'], 'destino':response['error'], 'length': response['error']}
            df = df.append(newRow, ignore_index=True)
        else:
            newRow = {'url':response['link'],
                      'name':'null',
                      'destino':response['target'],
            }
            df = df.append(newRow, ignore_index=True)
    
    
    # Exporting results:
    
    df.to_csv(filename)