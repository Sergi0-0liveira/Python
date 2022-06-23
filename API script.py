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

## most of the provide code is available at the API website. However I like to explain it to better understand how it functions

##STEP 1 - store the API in a variable that we can work with.

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 

##STEP 2- Define parameters and headers
## PARAMETERS - 
## HEADERS -this is usefull and it provides information about the request we are doing, in this case we are defininf the start, limit and currency we want to request.

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5741d03f-db7b-4efd-8304-7a06542e534b',
}

##STEP3 - This is not necessary for every API we connect with however since this is to show how I would handle. It makes sense to create a session object. 
# A session object has the purpose of improve the speed of our requests. Instead of connecting to the API/server each time we do a request... 
# we create a session and this we leave the connection open and we can use it to send multiple request. 
# This will increase performance.
# for this we only need to create a variable named session and store the session in it

session = Session()
session.headers.update(headers)

#STEP 4 - Getting the data
# in this case We are TRY to get the info and store it data by loading the json file.
# we are also looking at if we fail to get the data we will handle and understand the error we are getting.

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
##STEP 5 - understanding the type of data we are dealing with
print(data)
type(data)

##STEP 6 - normalizing the data

df = pd.json_normalize(data['data'])

#STEP 7 - exporting to a csv file

df.to_csv(r'C:\Users\SergioOliveira\Projects\API\cryptodata.csv', index = False)
