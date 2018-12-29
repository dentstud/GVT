
from binance.client import Client
from binance.websockets import BinanceSocketManager
import pymongo



client = Client("a","b")

bm = BinanceSocketManager(client)


myclient_1 = pymongo.MongoClient("mongodb://poya1:Muhammad00.@ds243254.mlab.com:43254/gvtbtc")
mydb_1 = myclient_1 ["gvtbtc"]
mycol_1 = mydb_1 ["data"]     # collection is mongo is same as a Table 


myclient_2 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds243254.mlab.com:43254/adabtc")
mydb_2 = myclient_2 ["adabtc"]
mycol_2 = mydb_2 ["data"] 



##############################################################################
##############################################################################

def process_message1(a1):

    mydict_1 = [a1]
    mycol_1.insert_many(mydict_1)
    print(a1['k']['c'])

def process_message2(a2):

    mydict_2 = [a2]
    mycol_2.insert_many(mydict_2)
    print(a2['k']['c'])
# 

conn_key = bm.start_kline_socket('GVTBTC', process_message1, interval='15m')


conn_key = bm.start_kline_socket('ADABTC', process_message2, interval = '15m')

bm.start()