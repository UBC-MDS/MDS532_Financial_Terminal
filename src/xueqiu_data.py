# %%
import requests
import pandas as pd
from datetime import datetime
import pytz

import requests

# Extract headers
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,et;q=0.7',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# Extract cookies
cookies = {
    'cookiesu': '501716971730603',
    'device_id': 'b466cc5fe5c41c2cf5113e1dc9758e94',
    's': 'br1biz2pdb',
    'bid': '3f1caaa1da9c9048cf5319e6a0c33666_lwsmxccn',
    'xq_is_login': '1',
    'u': '2110750062',
    'xq_a_token': 'ad394ced1eb5707d9926b7342d2aae0c4c6d5762',
    'xqat': 'ad394ced1eb5707d9926b7342d2aae0c4c6d5762',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjIxMTA3NTAwNjIsImlzcyI6InVjIiwiZXhwIjoxNzQ1MzY2ODMwLCJjdG0iOjE3NDI3NzQ4MzA0MDUsImNpZCI6ImQ5ZDBuNEFadXAifQ.Z-mGI_SUS8ZLs-ULLPuS4e57ToxuJtvr_ACqW3H4vhru_chjYnmOeYPL_fq9vtRWZlPICumWoDSasmCK97PlgB4UaBSMJT5yiJYIKgsBH7aNC3mPU4iI9kiN-PzS78tLhtz4n6VAnZvmWust--LUWRVX3bNLnSVpMrmuEx2yPq23ism4d5-TirYoNxiZ8k7yhANciEuEx64k__VQfsCFvOqnnF387X38WASsT_phDJNpkT5aDaLXAlQsh4oKpdCt1tiy6IZMqSwLN3F4ci_o1XJKjFdGh-G6-GX87D8dT317bW1iYOmQSUSJEKITE_H4uQyrm2leyEjwoRPCC0QoPg',
    'xq_r_token': '3b737bccb2dc7fde2bd8bd9c1a3835a305eede31',
    'is_overseas': '1',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1742512425,1742534199,1742575630,1742774972',
    'HMACCOUNT': '90AC0DA1311E6AC3',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1742774975',
    'ssxmod_itna': 'eq0xuDRDyD0DgDjxhDh=CD8GtwRDewxq0dGMD3Mq7tDRDFqAPeDHAxfh1CixkhyExxQmi7T5D/K7eGzDiqKGhDBnAzQnxEh6xHbU02D1=WCQ4wmwNf0hwwvNXMrOowiQ40aDbqGkoKg5GGm4GwDGoD34DiDDPDb8NDAMeD7qDFblrovCrDm4GWbeGfDDoDY32xxit3DDUIRqG2WhrKDDNK0pxDaGD4D6nlbZe7hnGbg3rDjTPD/RKIOYrFk/OKUjWwgRuwKeGySKGuIleQyq9O7QT3ZjtQt4xbU4x4K2ImQAGQ70DYY+Dkn0K/vlQDKWD4K0qtGtK2a4uaDDWVrz=j3qD4w0khkCpMCwGzPg177DXMYiGD52Y1DxiGx9BmLEz+E53B5G2ph2KjEs5nK9hx4D',
    'ssxmod_itna2': 'eq0xuDRDyD0DgDjxhDh=CD8GtwRDewxq0dGMD3Mq7tDRDFqAPeDHAxfh1CixkhyExxQmi7keDAKr7GbQeDjRDeiH4GNKNh=BE4eapZeLuxsyfpLIRhw+hQ96el4u08qe/4oMFvs2eZo4QDh8tleKQlP13lmxtm7WY7Y+uPPW5FcFqGp=UZvxTIoWDp7hd2BG0Dh7d99H9jY4kcYENpyp8xp7TKLzn1MWSgy6qm5QFtE=Opl0D/m=7l7Ru4w0b/PWdNEpbtRWe0GtktGsKnxGel=Ik2ogIqh4wQ4BuN+rMnw4VBGIC3XVQ2eKYD'
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
