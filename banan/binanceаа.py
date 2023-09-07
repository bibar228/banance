import time
from decimal import Decimal, ROUND_FLOOR
from binance.client import Client
from binance.exceptions import BinanceAPIException
from sql_request import sql_req
import keys
import pandas as pd
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

client = Client(keys.api_key, keys.api_secret)

depth = client.get_order_book(symbol='TRBUSDT')
print(depth)