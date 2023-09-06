import time
import pymysql
from binance.client import Client
import telebot
import keys

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

client = Client(keys.api_key, keys.api_secret)
#i = "SNXUSDT"

def sql_req(i):
    try:
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
    except Exception as e:
        telebot.TeleBot(telega_token).send_message(-695765690, f"SQL OSHIBKA: {e}\n")

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

    except Exception as e:
        telebot.TeleBot(telega_token).send_message(-695765690, f"SQL OSHIBKA: {e}\n")