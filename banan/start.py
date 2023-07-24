from binance.client import Client
import keys
import pandas as pd
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

client = Client(keys.api_key, keys.api_secret)
#futures_exchange_info = client.futures_exchange_info()
#trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols'] if info['symbol'][-4:] == "USDT"]
trading_pairs = ['BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'IOTXUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT', 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'WOOUSDT', 'FTTUSDT', 'JASMYUSDT', 'DARUSDT', 'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT', 'FOOTBALLUSDT', 'SPELLUSDT', 'LDOUSDT', 'CVXUSDT', 'ICPUSDT', 'APTUSDT', 'QNTUSDT', 'BLUEBIRDUSDT', 'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT', 'TUSDT', 'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT', 'COCOSUSDT', 'BNXUSDT', 'ACHUSDT', 'SSVUSDT', 'CKBUSDT', 'PERPUSDT', 'TRUUSDT', 'LQTYUSDT', 'USDCUSDT', 'IDUSDT', 'ARBUSDT', 'JOEUSDT', 'TLMUSDT', 'AMBUSDT', 'LEVERUSDT', 'RDNTUSDT', 'HFTUSDT', 'XVSUSDT', 'BLURUSDT', 'EDUUSDT', 'IDEXUSDT', 'SUIUSDT', 'UMAUSDT', 'RADUSDT', 'KEYUSDT', 'COMBOUSDT', 'NMRUSDT', 'MAVUSDT', 'MDTUSDT', 'XVGUSDT']


def top_coin():

    for i in trading_pairs:
        try:
            print(i)
            print(last_data(i, "3m", "300"))
            data_token = last_data(i, "3m", "300")
            if data_token[0][-3:] == sorted(data_token[0][-3:]) and sum(data_token[1][:-3])/len(data_token[1][:-3]) * 7 < sum(data_token[1][-3:-1])/3 and 100-(data_token[0][-3]/data_token[0][-1])*100 > 2.4:
                chat_id = -695765690
                bot = telebot.TeleBot(telega_token)
                message = "ALARM - " + i
                bot.send_message(chat_id, message)
            if 100-(data_token[0][-3]/data_token[0][-1])*100 > 2.4 and data_token[0][-1] > sum(data_token[0][80:-3])/len(data_token[0][80:-3]):
                chat_id = -695765690
                bot = telebot.TeleBot(telega_token)
                message = f"PUMP {i}\n{data_token[0][-3:], data_token[1][-3:]}\nРОСТ ЦЕНЫ НА {round(100-(data_token[0][-3]/data_token[0][-1])*100, 2)}%\nСРЕДНИЙ ОБЪЕМ ТОРГОВ - {int(sum(data_token[1][:-3])/len(data_token[1][:-3]))}"
                bot.send_message(chat_id, message)
        except:
            pass


    #top_coin = work[int(work.priceChangePercent.values[0]) > 8]
    #top_coin = top_coin.symbol.values[0]
    #return bebra


#print(top_coin())

def last_data(symbol, interval, lookback):

    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    #frame.to_csv('file1.csv')
    #print(frame["Volume"].sum())
    return [i.Open for i in frame.itertuples()], [i.Volume for i in frame.itertuples()]


def btc_anal(data):
    if round(sum(data[0][:-1])/28 / data[0][-1] - 1, 3) > 0.28:
        chat_id = -695765690
        bot = telebot.TeleBot(telega_token)
        message = f"БИТОК РАСТЕТ НА {round(sum(data[0][:-1])/28 / data[0][-1] - 1, 3)}%"
        bot.send_message(chat_id, message)

    print(round((data[0][-1] / (sum(data[0][:-1])/len(data[0][:-1])))-1, 3))
    print(data[0][-1], sum(data[0][:-1])/len(data[0][:-1]))
    print(round(data[0][-1] / (sum(data[0][:-1])/len(data[0][:-1]))-1, 1))



while True:
    btc_anal(last_data('BTCUSDT', "5m", "150"))
    top_coin()