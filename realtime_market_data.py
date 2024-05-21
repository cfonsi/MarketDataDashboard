import asyncio
import websockets
import json

BINANCE_WS_URL = f"wss://stream.binance.com:9443/ws/btcusdt@trade"

async def fetch_market_data():
    async with websockets.connect(BINANCE_WS_URL) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                print(f"Price of BTC: {data['p']}")
            except Exception as e:
                print(f"Error: {e}")
                break

def main():
    asyncio.run(fetch_market_data())

if __name__ == "__main__":
    main()
