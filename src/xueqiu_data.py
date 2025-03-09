# %%
import requests
import pandas as pd
from datetime import datetime
import pytz

import requests

# Extract headers
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

# Extract cookies
cookies = { 
    "cookiesu": "501716971730603",
    "device_id": "b466cc5fe5c41c2cf5113e1dc9758e94",
    "s": "br1biz2pdb",
    "bid": "3f1caaa1da9c9048cf5319e6a0c33666_lwsmxccn",
    "xq_is_login": "1",
    "u": "2110750062",
    "xq_a_token": "9c122216cb6f84ba4120b71e9cbfd32c77ef6487",
    "xqat": "9c122216cb6f84ba4120b71e9cbfd32c77ef6487",
    "xq_r_token": "f1e36d5474b04438b870677381f462a49040683e",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjIxMTA3NTAwNjIsImlzcyI6InVjIiwiZXhwIjoxNzQzOTIzMTI2LCJjdG0iOjE3NDEzMzExMjY1NjEsImNpZCI6ImQ5ZDBuNEFadXAifQ.BOtmado9nrsKHetVkPMOcrjS3jZv1wU1OOBydAhOtHPVMAwHgsNV0PIWp0PR1pqX-PbaiOnL9tIUKeb1ePdlYGbcTg5tcv4kAfDyrD-pH1cxuJqyEhb0paIaCRfNJ2uAyibRZUM8Ss24AGSVocA5og6lkmbph1rKL0aSTP7OUV_LH5bwvG0riK73sP6CbC7vv-q-rnIXycluAbI96xztg3fEjUt4hEM6RqCtoDr5l_CtC4XFKwtfNJwYyZ9yQInoMQejch4SeG8kTu4owJdoAEhem790HKmcpQLI1i2O089_I7F316DU7-aQZcWQVtDq2OQhiezo9AUSwBmCycJMzw",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1741297738,1741305010,1741326639,1741332357",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1741332357",
    "HMACCOUNT": "90AC0DA1311E6AC3",
}

def get_current_newyork_time():
    # Get current UTC time
    utc_now = datetime.now(pytz.utc)
    # Convert UTC time to New York time
    newyork_tz = pytz.timezone('America/New_York')
    newyork_now = utc_now.astimezone(newyork_tz)
    # Convert New York time to milliseconds timestamp
    milliseconds = int(newyork_now.timestamp() * 1000)
    return milliseconds

def calculate_date_difference(date_str, timezone_str):
    # Convert string to date object and specify timezone
    date = pd.to_datetime(date_str).tz_localize(timezone_str)
    
    # Get current time and specify timezone
    current_date = datetime.now(pytz.timezone(timezone_str))
    
    # Calculate date difference
    date_diff = current_date - date
    
    # Output date difference (in days)
    return date_diff.days

def getUSStockHistoryByDate(symbol, start_date = '2025-01-01', end_date = '9999-12-31'):

    timezone = 'America/New_York'
    begin = get_current_newyork_time()

    days = calculate_date_difference(start_date, timezone) + 120
    
    url = f'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol={symbol}&begin={begin}&period=day&type=before&count=-{days}'

    response = requests.get(url, headers=headers, cookies=cookies)
    response_json = response.json()
    
    # Extract column names and data items
    columns = response_json['data']['column']
    items = response_json['data']['item']

    # Convert data items to DataFrame and set column names
    df = pd.DataFrame(items, columns=columns)

    # Calculate 60-day moving average (MA60)
    df['MA60'] = df['close'].rolling(window=60).mean()
    # Calculate 120-day moving average (MA120)
    df['MA120'] = df['close'].rolling(window=120).mean()
    
    # Convert timestamp to pandas datetime object and filter
    df['Timestamp_str'] = pd.to_datetime(df['timestamp'], unit='ms', utc=True).dt.tz_convert(timezone)
    df = df[df['Timestamp_str'] >= start_date]
    df = df[df['Timestamp_str'] <= end_date]

    # Convert filtered timestamp to string format
    df['Timestamp_str'] = df['Timestamp_str'].dt.strftime('%Y-%m-%d')
    
    df['percent'] = df['percent'].div(100)
    df['turnoverrate'] = df['turnoverrate'].div(100)
    # Add Ticker column
    df['Ticker'] = symbol

    return df

if __name__ == "__main__":
    df = getUSStockHistoryByDate('AAPL')
# %%
