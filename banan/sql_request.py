import time
from datetime import datetime

import pymysql
from binance.client import Client
from binance.exceptions import BinanceAPIException

api_key = "rxe9zm8PLaF4MT1ZshEcVC0559883oH8LCVTbjOhY5U8TXoDbsbnNfhVBQDZ37xf"
api_secret = "f41uNN5J8TIeL4lWYCM3n9n4do4e5I1T8YQ5JNiheljyyiKLLAFpEqMSwC3Tsoa3"

client = Client(api_key, api_secret)
i = "SNXUSDT"
orders = client.get_all_orders(symbol=i, limit=1)
times = time.localtime(int((str(orders[0]["time"]))[:-3]))
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", times)
name_cript = orders[0]["symbol"][:-4]
if orders[0]["side"] == "SELL":
    side = "Продать"
elif orders[0]["side"] == "BUY":
    side = "Купить"
price = float(orders[0]["price"])
count = float(orders[0]["origQty"])
all_cost = float(orders[0]['cummulativeQuoteQty'])
link_cript = f"https://www.binance.com/ru/trade/{i[:-4]}_USDT?_from=markets&theme=dark&type=grid"


values = (formatted_time, name_cript, side, price, count, all_cost, link_cript)

try:
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='banan_user', password='warlight123',
                                         database='banan',
                                         cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `vision_orders` (time, name_cript, side, price, count, all_cost, link_cript) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (values))
            connection.commit()
    finally:
        connection.close()

except Exception as ex:
    print(ex)