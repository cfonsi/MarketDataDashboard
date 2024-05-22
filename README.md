# Real-Time Cryptocurrency Price Tracker

This project is a real-time cryptocurrency price tracker that fetches live market data from Binance using WebSockets and displays the current price along with the percentage change from specified intervals (e.g., 1 hour, 1 day, 1 week).

## Features

- Fetches real-time market data for a specified cryptocurrency using WebSockets.
- Displays the current price and calculates the percentage change from historical prices.
- Supports configurable time intervals for comparison (e.g., 1 hour, 1 day, 1 week).
- Allows for an adjustable refresh rate

## Installation

### Prerequisites

- Python 3.6 or higher

### Installing Required Libraries

```bash
pip install -r requirements.txt

### Example Output

```bash
Price of PYR: 4.61700000 | Change from 1d ago: -4.41%
Price of PYR: 4.62000000 | Change from 1d ago: -4.35%
Price of PYR: 4.62100000 | Change from 1d ago: -4.33%
Price of PYR: 4.62300000 | Change from 1d ago: -4.29%


