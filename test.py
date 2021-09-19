import csv
import pandas as pd
from datetime import date

data = pd.DataFrame({
    'url':['test','test'],
    'name':['test','test'],
    'destino':['test','test'],
    'length':['test','test']
}
)

filename = (f'./database/dataset_{date.today()}.csv')

data.to_csv(filename,index=False)