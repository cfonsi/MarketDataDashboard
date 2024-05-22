import asyncio
import websockets
import json

async def fetch_market_data(currency,interval):
    
    BINANCE_WS_URL = f"wss://stream.binance.com:9443/ws/{currency}usdt@trade"

    async with websockets.connect(BINANCE_WS_URL) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                print(f"Price of {currency.upper()}: {data['p']}")
                await asyncio.sleep(interval)
            except websockets.ConnectionClosed:
                print("Connection closed, retrying...")
                await asyncio.sleep(1)
                continue
            except Exception as e:
                print(f"Error: {e}")
                break

def main():
    asyncio.run(fetch_market_data('pyr',5))

if __name__ == "__main__":
    main()
