import finnhub
from datetime import datetime
import json
import boto3

import awswrangler as wr
import pandas as pd

#%% vars
ssm_client = boto3.client('ssm')
finhub_api_response = ssm_client.get_parameter(
    Name='finnhub_api',
    WithDecryption=True
    )
    
finhub_api = finhub_api_response['Parameter']['Value']
symbol_bronze_name = "avt-symbol-bronze"
 
td  = datetime.today()
y = td.year
m = td.month

td_string = f'year={y}/month={m}'

def lambda_handler(event,context):
    s3 = boto3.client('s3')

    finnhub_client = finnhub.Client(api_key=finhub_api)
    symbol_json = finnhub_client.stock_symbols('US')
    print('symbol collected')
    df = pd.DataFrame(symbol_json)
    
    wr.s3.to_parquet(df=df,
        path=f's3://{symbol_bronze_name}/{td_string}/symbol.parquet',
        index = False,
        compression = 'snappy',
        
    )
    
    return {"statusCode":200,
            "log":'Symbol put to S3 Complete'
        
    }