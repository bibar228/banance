import time
from decimal import Decimal, ROUND_FLOOR
from binance.client import Client
from binance.exceptions import BinanceAPIException
import keys
import pandas as pd
import telebot
from sql_request import sql_req
from tradingview_ta import TA_Handler, Interval, Exchange

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"
chat_id = -695765690

client = Client(keys.api_key, keys.api_secret)
# futures_exchange_info = client.futures_exchange_info()
# trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols'] if info['symbol'][-4:] == "USDT"]
trading_pairs = ['1INCHUSDT', 'AAVEUSDT', 'ACAUSDT', 'ACHUSDT', 'ACMUSDT', 'ADAUSDT', 'ADXUSDT', 'AERGOUSDT', 'AGIXUSDT',
                 'AGLDUSDT', 'AKROUSDT', 'ALCXUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPACAUSDT', 'ALPHAUSDT', 'ALPINEUSDT',
                 'AMBUSDT', 'AMPUSDT', 'ANKRUSDT', 'ANTUSDT', 'APEUSDT', 'API3USDT', 'APTUSDT', 'ARBUSDT', 'ARDRUSDT',
                 'ARKMUSDT', 'ARPAUSDT', 'ARUSDT', 'ASRUSDT', 'ASTRUSDT', 'ASTUSDT', 'ATAUSDT', 'ATMUSDT', 'ATOMUSDT',
                 'AUCTIONUSDT', 'AUDIOUSDT', 'AVAUSDT', 'AVAXUSDT', 'AXSUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANDUSDT',
                 'BARUSDT', 'BATUSDT', 'BCHUSDT', 'BELUSDT', 'BETAUSDT', 'BETHUSDT', 'BICOUSDT', 'BIFIUSDT', 'BLZUSDT',
                 'BNTUSDT', 'BNXUSDT', 'BONDUSDT', 'BSWUSDT', 'BTSUSDT', 'BURGERUSDT', 'BUSDUSDT', 'C98USDT',
                 'CAKEUSDT', 'CELOUSDT', 'CELRUSDT', 'CFXUSDT', 'CHESSUSDT', 'CHRUSDT', 'CHZUSDT', 'CITYUSDT', 'CKBUSDT',
                 'CLVUSDT', 'COMBOUSDT', 'COMPUSDT', 'COSUSDT', 'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CTXCUSDT',
                 'CVCUSDT', 'CVPUSDT', 'CVXUSDT', 'CYBERUSDT', 'DARUSDT', 'DASHUSDT', 'DATAUSDT', 'DCRUSDT', 'DEGOUSDT',
                 'DENTUSDT', 'DEXEUSDT', 'DFUSDT', 'DGBUSDT', 'DIAUSDT', 'DOCKUSDT', 'DODOUSDT', 'DOGEUSDT', 'DOTUSDT',
                 'DREPUSDT', 'DUSKUSDT', 'DYDXUSDT', 'EDUUSDT', 'EGLDUSDT', 'ELFUSDT', 'ENJUSDT', 'ENSUSDT', 'EOSUSDT',
                 'EPXUSDT', 'ERNUSDT', 'ETCUSDT', 'EURUSDT', 'FARMUSDT', 'FDUSDUSDT', 'FETUSDT', 'FIDAUSDT', 'FILUSDT',
                 'FIOUSDT', 'FIROUSDT', 'FISUSDT', 'FLMUSDT', 'FLOKIUSDT', 'FLOWUSDT', 'FLUXUSDT', 'FORTHUSDT', 'FORUSDT',
                 'FRONTUSDT', 'FTMUSDT', 'FUNUSDT', 'FXSUSDT', 'GALAUSDT', 'GALUSDT', 'GASUSDT', 'GBPUSDT', 'GHSTUSDT',
                 'GLMRUSDT', 'GLMUSDT', 'GMTUSDT', 'GMXUSDT', 'GNOUSDT', 'GNSUSDT', 'GRTUSDT', 'GTCUSDT', 'HARDUSDT',
                 'HBARUSDT', 'HFTUSDT', 'HIFIUSDT', 'HIGHUSDT', 'HIVEUSDT', 'HOOKUSDT', 'HOTUSDT', 'ICPUSDT', 'ICXUSDT',
                 'IDEXUSDT', 'IDUSDT', 'ILVUSDT', 'IMXUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IRISUSDT',
                 'JASMYUSDT', 'JOEUSDT', 'JSTUSDT', 'JUVUSDT', 'KAVAUSDT', 'KDAUSDT', 'KEYUSDT', 'KLAYUSDT', 'KMDUSDT',
                 'KNCUSDT', 'KP3RUSDT', 'KSMUSDT', 'LAZIOUSDT', 'LDOUSDT', 'LEVERUSDT', 'LINAUSDT', 'LINKUSDT', 'LITUSDT',
                 'LOKAUSDT', 'LOOMUSDT', 'LPTUSDT', 'LQTYUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCUSDT', 'LTOUSDT', 'LUNAUSDT',
                 'LUNCUSDT', 'MAGICUSDT', 'MANAUSDT', 'MASKUSDT', 'MATICUSDT', 'MAVUSDT', 'MBLUSDT', 'MBOXUSDT', 'MCUSDT',
                 'MDTUSDT', 'MDXUSDT', 'MINAUSDT', 'MKRUSDT', 'MLNUSDT', 'MOBUSDT', 'MOVRUSDT', 'MTLUSDT', 'MULTIUSDT',
                 'NEARUSDT', 'NEOUSDT', 'NEXOUSDT', 'NKNUSDT', 'NMRUSDT', 'NULSUSDT', 'OAXUSDT', 'OCEANUSDT', 'OGNUSDT',
                 'OGUSDT', 'OMGUSDT', 'OMUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'OOKIUSDT', 'OPUSDT', 'ORNUSDT', 'OSMOUSDT',
                 'OXTUSDT', 'PAXGUSDT', 'PENDLEUSDT', 'PEOPLEUSDT', 'PEPEUSDT', 'PERLUSDT', 'PERPUSDT', 'PHAUSDT', 'PHBUSDT',
                 'PLAUSDT', 'PNTUSDT', 'POLSUSDT', 'POLYXUSDT', 'PONDUSDT', 'PORTOUSDT', 'POWRUSDT', 'PROMUSDT', 'PROSUSDT',
                 'PSGUSDT', 'PUNDIXUSDT', 'PYRUSDT', 'QIUSDT', 'QKCUSDT', 'QNTUSDT', 'QTUMUSDT', 'QUICKUSDT', 'RADUSDT',
                 'RAREUSDT', 'RAYUSDT', 'RDNTUSDT', 'REEFUSDT', 'REIUSDT', 'RENUSDT', 'REQUSDT', 'RIFUSDT', 'RLCUSDT',
                 'RNDRUSDT', 'ROSEUSDT', 'RPLUSDT', 'RSRUSDT', 'RUNEUSDT', 'RVNUSDT', 'SANDUSDT', 'SANTOSUSDT', 'SCRTUSDT',
                 'SCUSDT', 'SEIUSDT', 'SFPUSDT', 'SHIBUSDT', 'SKLUSDT', 'SLPUSDT', 'SNTUSDT', 'SNXUSDT', 'SOLUSDT',
                 'SPELLUSDT', 'SSVUSDT', 'STEEMUSDT', 'STGUSDT', 'STMXUSDT', 'STORJUSDT', 'STPTUSDT', 'STRAXUSDT', 'STXUSDT',
                 'SUIUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSHIUSDT', 'SXPUSDT', 'SYNUSDT', 'SYSUSDT', 'TFUELUSDT', 'THETAUSDT',
                 'TKOUSDT', 'TLMUSDT', 'TOMOUSDT', 'TRBUSDT', 'TROYUSDT', 'TRUUSDT', 'TRXUSDT', 'TUSDT', 'TUSDUSDT', 'TVKUSDT',
                 'TWTUSDT', 'UFTUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIUSDT', 'USDCUSDT', 'USDPUSDT', 'USTCUSDT', 'UTKUSDT',
                 'VETUSDT', 'VGXUSDT', 'VIBUSDT', 'VIDTUSDT', 'VITEUSDT', 'VOXELUSDT', 'VTHOUSDT', 'WANUSDT', 'WAVESUSDT',
                 'WAXPUSDT', 'WBETHUSDT', 'WBTCUSDT', 'WINGUSDT', 'WINUSDT', 'WLDUSDT', 'WNXMUSDT', 'WOOUSDT', 'WRXUSDT',
                 'WTCUSDT', 'XECUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XNOUSDT', 'XRPUSDT', 'XTZUSDT', 'XVGUSDT', 'XVSUSDT',
                 'YFIUSDT', 'YGGUSDT', 'ZECUSDT', 'ZENUSDT', 'ZILUSDT', 'ZRXUSDT']
ex = []

def top_coin():
    for i in trading_pairs:
        if i not in ex:
            try:
                # print(i)
                # print(last_data(i, "3m", "300"))
                data_token_price = last_data(i, "1m", "1440")
                d = data_token_price[1][900:]
                prices_token = data_token_price[0][300:]
                volumes_token = [round(d[i] + d[i + 1] + d[i + 2], 2) for i in range(0, len(d), 3)]
                price_change_in_5min = 100 - (prices_token[-5] / prices_token[-1]) * 100

                price_change_percent_10h = 100 - ((data_token_price[0][600] / data_token_price[0][-22]) * 100)

                # if price_change_percent_24h > 100:
                #     price_change_percent_24h = round(price_change_percent_24h - 100, 2)
                # elif price_change_percent_24h < 100:
                #     price_change_percent_24h = round(100 - price_change_percent_24h, 2)
                # else:
                #     price_change_percent_24h = 0
                #print(i)
                if price_change_in_5min > 2.4 \
                        and prices_token[-3:] == sorted(prices_token[-3:]) \
                        and sum(volumes_token[:-5]) / len(volumes_token[:-5]) * 9.5 < volumes_token[-2] \
                        and prices_token[-1] > sum(prices_token[:-5]) / len(prices_token[:-5]) \
                        and price_change_percent_10h < 7:

                    buy_qty = round(11 / prices_token[-1], 1)

                    telebot.TeleBot(telega_token).send_message(chat_id, f"RABOTAEM - {i}\n"
                                                                        f"Количество покупаемого - {buy_qty}, Цена - {prices_token[-1]}, Изменение цены за 5 мин - {round(price_change_in_5min, 2)}%\n"
                                                                        f"Изменение цены за 10ч - {price_change_percent_10h}")

                    try:
                        order_buy = client.create_order(symbol=i, side='BUY', type='MARKET', quantity=buy_qty)
                        ex.append(i)
                    except BinanceAPIException as e:
                        if e.message == "Filter failure: LOT_SIZE":
                            buy_qty = int(round(11 / prices_token[-1], 1))
                            order_buy = client.create_order(symbol=i, side='BUY', type='MARKET', quantity=buy_qty)
                            ex.append(i)
                        else:
                            telebot.TeleBot(telega_token).send_message(chat_id, f"BUY ERROR: {e.message}\n"
                                                                               f"Количество покупаемого - {buy_qty}, Цена - {prices_token[-1]}")
                            time.sleep(30)
                            break

                    try:
                        buyprice = float(order_buy["fills"][0]["price"])
                        open_position = True
                        # if "." in str(buy_qty):
                        #     x = str(buy_qty).split(".")
                        #     okr = "0." + "0" * len(x[1])
                        # else:
                        #     okr = "0"
                    except Exception as e:
                        telebot.TeleBot(telega_token).send_message(chat_id, f"ERROR: {e}\n")
                        time.sleep(30)
                        break

                    start_time = time.time()

                    while open_position:
                        last_time = time.time()
                        all_orders = pd.DataFrame(client.get_all_orders(symbol=i),
                                                  columns=["orderId", "type", "side", "price", "status"])
                        balance = client.get_asset_balance(asset=i[:-4])
                        sell_qty = float(balance["free"])
                        #sell_qty = Decimal(sell_qty).quantize(Decimal(okr), ROUND_FLOOR)

                        if sell_qty > 0.05 and len(all_orders[all_orders.isin(["NEW"]).any(axis=1)]) == 0 and int(last_time-start_time) < 2500:
                            try:
                                order_sell = client.order_limit_sell(symbol=i, quantity=sell_qty, price=Decimal(str(round((buyprice / 100) * 101, max([len(str(i).split(".")[1]) for i in data_token_price[0][-5:]])))))

                            except Exception as e:
                                telebot.TeleBot(telega_token).send_message(chat_id, f"SELL ERROR: {e}\n"
                                                                                       f"Количество продаваемого - {sell_qty}, Цена - {round((buyprice / 100) * 101, len(str(prices_token[-1]).split('.')[1]))}\n"
                                                                                       f"Монеты в кошельке - {float(sell_qty)}, Количество открытых ордеров - {len(all_orders[all_orders.isin(['NEW']).any(axis=1)])}")
                                time.sleep(30)
                        sell_qty = float(balance["free"])
                        #sell_qty = Decimal(sell_qty).quantize(Decimal(okr), ROUND_FLOOR)
                        if float(sell_qty) < 0.05 and len(all_orders[all_orders.isin(["NEW"]).any(axis=1)]) == 0 and int(last_time-start_time) < 2500:
                            open_position = False

                            bot = telebot.TeleBot(telega_token)
                            message = f"СДЕЛКА ЗАВЕРШЕНА - {i}\n" \
                                      f"{prices_token[-3:]}\n" \
                                      f"ЗАСЕК НА РОСТЕ ЦЕНЫ В {round(price_change_in_5min, 2)}%\n" \
                                      f"\n" \
                                      f"https://www.binance.com/ru/trade/{i[:-4]}_USDT?_from=markets&theme=dark&type=grid"
                            bot.send_message(chat_id, message)

                        if int(last_time-start_time) > 2500:
                            orders = client.get_open_orders(symbol=i)
                            for order in orders:
                                ordId = order["orderId"]
                                client.cancel_order(symbol=i, orderId=ordId)

                            try:
                                sell_qty = float(balance["free"])
                                order_sell = client.create_order(symbol=i, side='SELL', type='MARKET', quantity=sell_qty)
                                telebot.TeleBot(telega_token).send_message(-695765690,
                                                                           f"Продажа в минус, за {order_sell['price']}\n"
                                                                           f"Покупал за {buyprice}")
                                open_position = False
                            except:
                                telebot.TeleBot(telega_token).send_message(-695765690,
                                                                           "Ошибка продажи в минус, Нужен хелп!")
                                time.sleep(30)
                                break

                        time.sleep(5)
                    sql_req(i)
            except:
                pass


def last_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    # frame.to_csv('file1.csv')
    # print(frame["Volume"].sum())
    return [i.High for i in frame.itertuples()], [i.Volume for i in frame.itertuples()]


def btc_anal(data):
    if round(data[0][-1] / (sum(data[0][:-1]) / len(data[0][:-1])) - 1, 3) > 0.5:
        bot = telebot.TeleBot(telega_token)
        message = f"БИТОК РАСТЕТ НА {round((sum(data[0][:-1]) / len(data[0][:-1])) / data[0][-1] - 1, 3)}%"
        bot.send_message(chat_id, message)
        return True
    elif round(data[0][-1] / (sum(data[0][:-1]) / len(data[0][:-1])) - 1, 3) < -0.5:
        bot = telebot.TeleBot(telega_token)
        message = f"БИТОК ПАДАЕТ НА {abs(round((sum(data[0][:-1]) / len(data[0][:-1])) / data[0][-1] - 1, 3))}%"
        bot.send_message(chat_id, message)
        return False
    # print(data)
    # print(sum(data[0][:-1])/len(data[0][:-1]))
    # print(data[0][-1])
    return True

# def get_recommend(i):
#     interval = Interval.INTERVAL_1_MINUTE
#     output = TA_Handler(symbol=i, screener="Crypto", exchange="Binance", interval=interval)
#
#     activiti = output.get_analysis().summary
#     return activiti


while True:
    #btc_differ = btc_anal(last_data('BTCUSDT', "15m", "300"))

    top_coin()
