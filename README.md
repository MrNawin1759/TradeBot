# 📊 Binance Futures Trading Bot

A command-line based trading bot that interacts with Binance Futures Testnet API.  
Supports market, limit, and stop-limit orders with daily logging.  
Ideal for learning, testing strategies, and prototyping trading automation.

📁 Project Structure

TradingBot/
├── main.py # Bot logic and command-line interface
├── application logs/ # Daily log files (auto-generated, not tracked by Git)
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation

## ⚙️ Features

- ✅ Place **Market Orders**
- ✅ Place **Limit Orders**
- ✅ Place **Stop-Limit Orders**
- ✅ Generate daily log files in `application logs/`
- ✅ Fully testable using Binance **Futures Testnet**

## 🚀 Getting Started

### 1. Clone the repository

bash

git clone https://github.com/MrNawin1759/TradingBot.git

cd TradingBot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set your Binance API credentials
Open main.py and replace the placeholders:

api_key = 'your_api_key_here'

api_secret = 'your_api_secret_here'

▶️ How to Run the Bot

    python main.py
    
You'll see a menu like:
1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order
4. Exit
Follow the prompts to place a trade on Binance Futures Testnet.

🧾 Logging

Log files are saved automatically under the application logs/ folder.

Each file is named by date:

  Log_file_2025-07-08.txt
  
📄 Requirements
  
  Python 3.8+
  
  python-binance

You can install dependencies with:

   pip install -r requirements.txt

🌐 Binance Testnet

Use Binance’s official Futures Testnet for simulation and testing:
  👉 https://testnet.binancefuture.com/

⚠️ Make sure to enable Futures on the testnet and generate separate API keys.

🚧 To-Do / Future Improvements

 Add Take-Profit and Stop-Market support
 
 Add leverage and margin selection
 
 Add price polling or websocket live ticker
 
 Integrate Telegram/Slack alerts
 
 Streamlit GUI for easier interaction
 
 Add backtesting or strategy modules
