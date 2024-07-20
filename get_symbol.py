import finnhub
from get_api_key import *
import pandas as pd 
from datetime import datetime
import boto3
#%% vars
finhub_api = get_api_key_finhub()
symbol_s3 = get_symbol_bucket()
symbol_bronze_name = symbol_s3['bronze'][1]['name']
 
td  = datetime.today()
y = td.year
m = td.month
d = td.day

td_string = f'year={y}/month={m}/'

# %%
def lambda_handler(event,context):
    s3 = boto3.client('s3')

    finnhub_client = finnhub.Client(api_key=finhub_api)
    symbol_json = pd.DataFrame(finnhub_client.stock_symbols('US')).to_json()
    name = symbol_bronze_name
    filename = td_string+'symbol.json'
    to_s3 = bytes(json.dumps(symbol_json),
                  encoding='UTF-8')

    s3.put_object(bucket=symbol_bronze_name,
                  key = filename,
                  body = to_s3
                  )
    
    print('Symbol JSON Put to S3 Complete')