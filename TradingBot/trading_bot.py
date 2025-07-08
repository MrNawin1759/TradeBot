import os
import logging
from datetime import datetime
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.exceptions import BinanceAPIException, BinanceOrderException

base_dir = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(base_dir, "Application_logs")
os.makedirs(log_folder, exist_ok=True)
# Set up logging
today_str = datetime.now().strftime("%Y-%m-%d")
log_file =os.path.join(log_folder, f"Log_file_{today_str}.txt")
logging.basicConfig(filename=log_file,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    """
    A simplified trading bot for the Binance Futures Testnet.
    """
    def __init__(self, api_key, api_secret, testnet=True):
        """ 
        Initializes the bot with API credentials.
        """
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'

    def place_market_order(self, symbol, side, quantity):
        """
        Places a market order.
        """
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info("Market order placed successfully,with order details: %s",order)
            print(order)
            return order
        except BinanceAPIException as e:
            logging.error(f"API Error placing market order: {e}")
        except BinanceOrderException as e:
            logging.error(f"Order Error placing market order: {e}")
        return None

    def place_limit_order(self, symbol, side, quantity, price):
        """
        Places a limit order.
        """
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_LIMIT,
                timeInForce=Client.TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info("Limit order placed successfully with order details: %s", order)
            print(order)
            return order
        except BinanceAPIException as e:
            logging.error(f"API Error placing limit order: {e}")
        except BinanceOrderException as e:
            logging.error(f"Order Error placing limit order: {e}")
        return None


    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """
        Places a stop-limit order.
        """
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.FUTURE_ORDER_TYPE_STOP,  # or just "STOP"
                timeInForce=Client.TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,           # Limit price
                stopPrice=stop_price,  # Trigger price
                workingType="MARK_PRICE",  # Optional: "MARK_PRICE" or "CONTRACT_PRICE"
            )
            logging.info("Stop-limit order placed successfully with order details: %s", order)
            print(order)
            return order
        except BinanceAPIException as e:
            logging.error(f"API Error placing stop-limit order: {e}")
        except BinanceOrderException as e:
            logging.error(f"Order Error placing stop-limit order: {e}")
        return None

def main():
    """
    Main function to run the trading bot CLI.
    """
    api_key ='ca08bf97b4c54bfc61f36c05046d1e174be2caf70baf7bccf8a22bcfd3bc0bc3'
    api_secret = '2a18eee0cd7395718bdbd2253e06201983851d2711f724c2b19d3e31b74c13e0'

    if not api_key or not api_secret:
        print("Please set the BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET environment variables.")
        return

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n--- Simplified Trading Bot ---")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter side (BUY or SELL): ").upper()
            quantity = float(input("Enter quantity: "))
            bot.place_market_order(symbol, side, quantity)

        elif choice == '2':
            symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter side (BUY or SELL): ").upper()
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter price: "))
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':
            symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter side (BUY or SELL): ").upper()
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter limit price: "))
            stop_price = float(input("Enter stop price: "))
            bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()