import time
from decimal import Decimal, ROUND_FLOOR
from binance.client import Client
from binance.exceptions import BinanceAPIException
from sql_request import sql_req
import keys
import pandas as pd
import telebot
import re
telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

client = Client(keys.api_key, keys.api_secret)

trading_pairs = ['1INCHUSDT', 'AAVEUSDT', 'ACAUSDT', 'ACHUSDT', 'ACMUSDT', 'ADAUSDT', 'ADXUSDT', 'AERGOUSDT', 'AGIXUSDT',
                 'AGLDUSDT', 'AKROUSDT', 'ALCXUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPACAUSDT', 'ALPHAUSDT', 'ALPINEUSDT',
                 'AMBUSDT', 'AMPUSDT', 'ANKRUSDT', 'ANTUSDT', 'APEUSDT', 'API3USDT', 'APTUSDT', 'ARBUSDT', 'ARDRUSDT',
                 'ARKMUSDT', 'ARPAUSDT', 'ARUSDT', 'ASRUSDT', 'ASTRUSDT', 'ASTUSDT', 'ATAUSDT', 'ATMUSDT', 'ATOMUSDT',
                 'AUCTIONUSDT', 'AUDIOUSDT', 'AVAUSDT', 'AVAXUSDT', 'AXSUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANDUSDT',
                 'BARUSDT', 'BATUSDT', 'BCHUSDT', 'BELUSDT', 'BETAUSDT', 'BETHUSDT', 'BICOUSDT', 'BIFIUSDT', 'BLZUSDT',
                 'BNTUSDT', 'BNXUSDT', 'BONDUSDT', 'BSWUSDT', 'BTSUSDT', 'BTTCUSDT', 'BURGERUSDT', 'BUSDUSDT', 'C98USDT',
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




# for i in trading_pairs:
#     if i == "WANUSDT":
#         print("yes")
# futures_exchange_info = client.get_exchange_info()
# trading_pairs2 = [info['symbol'] for info in futures_exchange_info['symbols'] if info['symbol'][-4:] == "USDT"]

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

i = "KDAUSDT"

data_token = last_data(i, "3m", "1440")
data_token_price = last_data(i, "1m", "1440")

price_change_percent_10h = 100 - ((data_token[0][200] / data_token[0][-7]) * 100)

price_change_percent_10h_new = 100 - ((data_token_price[0][600] / data_token_price[0][-22]) * 100)

print(price_change_percent_10h)
print(price_change_percent_10h_new)