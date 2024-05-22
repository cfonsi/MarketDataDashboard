import asyncio
import websockets
import json
import requests
from datetime import datetime, timedelta

async def fetch_market_data(currency,refresh_interval,historical_date):
    
    BINANCE_WS_URL = f"wss://stream.binance.com:9443/ws/{currency}usdt@trade"

    async with websockets.connect(BINANCE_WS_URL) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                price_change = get_price_change(currency,data['p'],historical_date)
                print(f"Price of {currency.upper()}: {data['p']} | Change from {historical_date} ago: {price_change:.2f}%")
                await asyncio.sleep(refresh_interval)
            except websockets.ConnectionClosed:
                print("Connection closed, retrying...")
                await asyncio.sleep(1)
                continue
            except Exception as e:
                print(f"Error: {e}")
                break

def get_price_change(currency,current_price,historical_date):

    historical_price = fetch_historical_price(currency,historical_date)
    current_price = float(current_price)
    price_change=((current_price - historical_price) / historical_price) * 100
    
    return price_change

def fetch_historical_price(currency, time_interval):
    
    request_body = {
        'symbol': f'{currency.upper()}USDT',
        'interval': time_interval,
        'limit': 1
    }

    response = requests.get('https://api.binance.com/api/v3/klines', params=request_body)
    data = response.json()

    if data:
        # Kline data structure - [Open time, Open, High, Low, Close, Volume, Close time, ...]
        # The open price for the current time period = the close price for the previous period which we'll use to compare 
        close_price = float(data[0][1])
        return close_price
    else:
        return None

def main():
    currency = 'pyr'
    refresh_rate = 5
    time_interval = '1d'
    asyncio.run(fetch_market_data(currency,refresh_rate,time_interval))

if __name__ == "__main__":
    main()
