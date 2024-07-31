import finnhub
from datetime import datetime
import json
import boto3

#%% vars
print('START')

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
d = td.day

td_string = f'year={y}/month={m}/'

# %%
def lambda_handler(event,context):
    s3 = boto3.client('s3')

    finnhub_client = finnhub.Client(api_key=finhub_api)
    symbol_json = finnhub_client.stock_symbols('US')
    
    name = symbol_bronze_name
    filename = td_string+'symbol.json'
    to_s3 = bytes(json.dumps(symbol_json),
                  encoding='UTF-8')

    s3.put_object(Bucket=symbol_bronze_name,
                  Key = filename,
                  Body = to_s3
                  )
    return {"statusCode":200,
            "log":'Symbol JSON Put to S3 Complete'
        
    }