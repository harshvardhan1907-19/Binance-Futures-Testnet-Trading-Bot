# Binance Futures Testnet Trading Bot

A Python-based command-line application that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**.

This project was developed as part of a Python Developer application task.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports both **BUY** and **SELL**
- Command Line Interface (CLI) using `argparse`
- Input validation
- Logging of API requests, responses, and errors
- Exception handling
- Clean and modular project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Requirements

- Python 3.10 or above
- Binance Futures Testnet Account
- Binance Testnet API Key
- Binance Testnet Secret Key

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd trading_bot
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## Usage

### Place a MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Place a LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

### Place a LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

---

## Logging

Application logs are stored in:

```
logs/trading_bot.log
```

The log file contains:

- Order Requests
- Order Responses
- API Errors

---

## Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing price for LIMIT orders
- Binance API errors
- Network/API exceptions

---

## Assumptions

- Orders are placed on the Binance USDT-M Futures Testnet.
- Valid API credentials are configured in the `.env` file.
- Internet connection is available.
- The user has sufficient Testnet balance.

---

## Technologies Used

- Python
- python-binance
- argparse
- python-dotenv
- logging

---

## Author

Harshvardhan Sagar