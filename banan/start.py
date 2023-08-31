import time

from binance.client import Client
import keys
import pandas as pd
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

client = Client(keys.api_key, keys.api_secret)
# futures_exchange_info = client.futures_exchange_info()
# trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols'] if info['symbol'][-4:] == "USDT"]
trading_pairs = ['BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT',
                 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT',
                 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT',
                 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT',
                 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT',
                 'SUSHIUSDT', 'SRMUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT',
                 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT',
                 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT',
                 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'CHZUSDT', 'SANDUSDT',
                 'ANKRUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT',
                 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT',
                 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT',
                 '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'IOTXUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT',
                 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT',
                 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT',
                 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'WOOUSDT', 'FTTUSDT', 'JASMYUSDT', 'DARUSDT',
                 'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT', 'FOOTBALLUSDT', 'SPELLUSDT', 'LDOUSDT', 'CVXUSDT',
                 'ICPUSDT', 'APTUSDT', 'QNTUSDT', 'BLUEBIRDUSDT', 'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT',
                 'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT',
                 'COCOSUSDT', 'BNXUSDT', 'ACHUSDT', 'SSVUSDT', 'CKBUSDT', 'PERPUSDT', 'TRUUSDT', 'LQTYUSDT', 'USDCUSDT',
                 'IDUSDT', 'ARBUSDT', 'JOEUSDT', 'TLMUSDT', 'AMBUSDT', 'LEVERUSDT', 'RDNTUSDT', 'HFTUSDT', 'XVSUSDT',
                 'BLURUSDT', 'EDUUSDT', 'IDEXUSDT', 'SUIUSDT', 'UMAUSDT', 'RADUSDT', 'KEYUSDT', 'COMBOUSDT', 'NMRUSDT',
                 'MAVUSDT', 'MDTUSDT', 'XVGUSDT']


def top_coin(btc_differ):
    for i in trading_pairs:
        try:
            # print(i)
            # print(last_data(i, "3m", "300"))
            data_token = last_data(i, "3m", "1440")

            prices_token = data_token[0][300:]
            volumes_token = data_token[1][300:]
            price_change_in_9min = 100 - (prices_token[-3] / prices_token[-1]) * 100

            price_change_percent_24h = 100 - ((data_token[0][0] / data_token[0][-7]) * 100)

            # if price_change_percent_24h > 100:
            #     price_change_percent_24h = round(price_change_percent_24h - 100, 2)
            # elif price_change_percent_24h < 100:
            #     price_change_percent_24h = round(100 - price_change_percent_24h, 2)
            # else:
            #     price_change_percent_24h = 0
            print(i)
            if price_change_in_9min > 2.7 \
                    and prices_token[-3:] == sorted(prices_token[-3:]) \
                    and sum(volumes_token[:-3]) / len(volumes_token[:-3]) * 9.5 < volumes_token[-2] \
                    and prices_token[-1] > sum(prices_token[:-3]) / len(prices_token[:-3]) \
                    and btc_differ \
                    and price_change_percent_24h < 7:

                telebot.TeleBot(telega_token).send_message(-695765690, f"RABOTAEM - {i}")

                buy_qty = round(11 / prices_token[-1], 1)
                order_buy = client.create_order(symbol=i, side='BUY', type='MARKET', quantity=buy_qty)
                buyprice = float(order_buy["fills"][0]["price"])
                all_orders = pd.DataFrame(client.get_all_orders(symbol=i), columns=["orderId", "type", "side", "price", "status"])
                open_position = True
                start_time = time.time()
                balance = client.get_asset_balance(asset=i[:-4])
                sell_qty = round(float(balance["free"]), 2)
                while open_position:
                    if sell_qty > 0.5:
                        try:
                            order_sell = client.order_limit_sell(symbol=i, quantity=sell_qty, price=(buyprice / 100) * 101)
                        except Exception as e:
                            time.sleep(30)
                            telebot.TeleBot(telega_token).send_message(-695765690, f"PIZDA OSHIBKA SELL: {e}")
                            order_sell = client.order_limit_sell(symbol=i, quantity=sell_qty, price=(buyprice / 100) * 101)
                    else:
                        open_position = False

                        chat_id = -695765690
                        bot = telebot.TeleBot(telega_token)
                        message = f"ALARM - {i}\n" \
                                  f"{prices_token[-3:], volumes_token[-3:]}\n" \
                                  f"РОСТ ЦЕНЫ НА {round(price_change_in_9min, 2)}%\n" \
                                  f"СРЕДНИЙ ОБЪЕМ ТОРГОВ - {int(sum(volumes_token[:-3]) / len(volumes_token[:-3]))}\n" \
                                  f"СРЕДНЯЯ ЦЕНА ЗА ПРОШЛЫЕ 9 ЧАСОВ - {sum(prices_token[:-3]) / len(prices_token[:-3])}\n" \
                                  f"https://www.binance.com/ru/trade/{i[:-4]}_USDT?_from=markets&theme=dark&type=grid\n" \
                                  f"order_buy - {order_buy}\n" \
                                  f"order_sell - {order_sell}"
                        bot.send_message(chat_id, message)

                    last_time = time.time()
                    if int(last_time-start_time) > 4000:
                        data_token = last_data(i, "1m", "2")
                        order_jopa = client.create_order(symbol=i, side='SELL', type='MARKET', quantity=sell_qty)
                        telebot.TeleBot(telega_token).send_message(-695765690,
                                                                   f"Продажа в минус, за {data_token[0][-1]}\n"
                                                                   f"Покупал за {buyprice}")
                    time.sleep(5)


                trading_pairs.pop(trading_pairs.index(i))



            # if price_change_in_9min > 2.7 \
            #         and prices_token[-1] > sum(prices_token[80:-3])/len(prices_token[80:-3]) \
            #         and btc_differ == True:
            #     chat_id = -695765690
            #     bot = telebot.TeleBot(telega_token)
            #     message = f"PUMP {i}\n" \
            #               f"{prices_token[-3:], volumes_token[-3:]}\n" \
            #               f"РОСТ ЦЕНЫ НА {round(100-(prices_token[-3]/prices_token[-1])*100, 2)}%\n" \
            #               f"СРЕДНИЙ ОБЪЕМ ТОРГОВ - {int(sum(volumes_token[:-3])/len(volumes_token[:-3]))}\n" \
            #               f"СРЕДНЯЯ ЦЕНА ЗА ПРОШЛЫЕ 9 ЧАСОВ - {sum(prices_token[:-3])/len(prices_token[:-3])}"
            #     bot.send_message(chat_id, message)
        except:
            pass

    # top_coin = work[int(work.priceChangePercent.values[0]) > 8]
    # top_coin = top_coin.symbol.values[0]
    # return bebra


# print(top_coin())

def last_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    # frame.to_csv('file1.csv')
    # print(frame["Volume"].sum())
    return [i.Open for i in frame.itertuples()], [i.Volume for i in frame.itertuples()]


def btc_anal(data):
    if round(data[0][-1] / (sum(data[0][:-1]) / len(data[0][:-1])) - 1, 3) > 0.5:
        chat_id = -695765690
        bot = telebot.TeleBot(telega_token)
        message = f"БИТОК РАСТЕТ НА {round((sum(data[0][:-1]) / len(data[0][:-1])) / data[0][-1] - 1, 3)}%"
        bot.send_message(chat_id, message)
        return True
    elif round(data[0][-1] / (sum(data[0][:-1]) / len(data[0][:-1])) - 1, 3) < -0.5:
        chat_id = -695765690
        bot = telebot.TeleBot(telega_token)
        message = f"БИТОК ПАДАЕТ НА {abs(round((sum(data[0][:-1]) / len(data[0][:-1])) / data[0][-1] - 1, 3))}%"
        bot.send_message(chat_id, message)
        return False
    # print(data)
    # print(sum(data[0][:-1])/len(data[0][:-1]))
    # print(data[0][-1])
    return True


while True:
    btc_differ = btc_anal(last_data('BTCUSDT', "15m", "300"))

    top_coin(btc_differ)
