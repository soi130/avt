#%% import
import pandas as pd
import get_api_key
import requests
import asyncio
import aiohttp
import datetime as datetime
#%% var
symbol = pd.read_parquet('symbol.parquet')
avt_api = get_api_key.get_api_key_avt()

start_year = 2020

focus = symbol.loc[symbol['mic'].isin(['XNYS','XMCM'])] #nyse and nasdaq only
symbol_ls = [i.split('.')[0] for i in focus['displaySymbol'].unique()]
symbol_ls = sorted(symbol_ls)


#%% def
def create_date_str(start_year):
    start = datetime.datetime(start_year,1,1)
    end = datetime.datetime.today()
    bus_date_range = pd.bdate_range(start,end,freq='B',normalize = True) #bdate_range return only business day (also freq = 'B')
    return bus_date_range

def create_url_list():
    bus_date_range = create_date_str(start_year)
    date_strs = [d.strftime("%Y-%m-%d") for d in bus_date_range]
    
    ls = []
    for s,d in zip(symbol_ls,date_strs):
        ls.append(f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={s}&date={d}&apikey={avt_api}')
    return ls
#%% collect data

async def fetch_data(session,url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = create_url_list()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_data(session,url))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
    return result

#%% run

data = main()
    

    



# %%
