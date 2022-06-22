# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:44:21 2022

@author: SergioOliveira
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5741d03f-db7b-4efd-8304-7a06542e534b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
##understanding the type of data we are dealing with

#print(type(data))

##normalizing the data

df = pd.json_normalize(data['data'])

#exporting to a csv file

df.to_csv(r'C:\Users\SergioOliveira\Projects\API\cryptodata.csv', index = False)