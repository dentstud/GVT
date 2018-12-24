
from binance.client import Client
from binance.websockets import BinanceSocketManager
import pymongo



client = Client("a","b")

bm = BinanceSocketManager(client)


myclient = pymongo.MongoClient("mongodb://poya1:Muhammad00.@ds243254.mlab.com:43254/gvtbtc")

mydb = myclient ["gvtbtc"]

mycol = mydb ["data"]     # collection is mongo is same as a Table 


def process_message(a):

    mydict = [a]
    mycol.insert_many(mydict)
    print(a['k']['c'])
# 
    
#    if c >= 1:
#        print ('BUY')
#    else:
#        print( "dont BUYY")
conn_key = bm.start_kline_socket('GVTBTC', process_message, interval='15m')
bm.start()



