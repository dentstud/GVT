
from binance.client import Client
from binance.websockets import BinanceSocketManager
import pymongo



client = Client("a","b")

bm = BinanceSocketManager(client)


    # collection is mongo is same as a Table 


myclient_2 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/mdabtc")
mydb_2 = myclient_2 ["mdabtc"]
mycol_2 = mydb_2 ["data"]
 
myclient_1 = pymongo.MongoClient("mongodb://poya1:Muhammad00.@ds243254.mlab.com:43254/gvtbtc")
mydb_1 = myclient_1 ["gvtbtc"]
mycol_1 = mydb_1 ["data"] 

myclient_3 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds243254.mlab.com:43254/eosbtc")
mydb_3 = myclient_3 ["eosbtc"]
mycol_3 = mydb_3 ["data"] 

myclient_4 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds243254.mlab.com:43254/adabtc")
mydb_4 = myclient_4 ["adabtc"]
mycol_4 = mydb_4 ["data"]     # collection is mongo is same as a Table 


myclient_5 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/dcrbtc")
mydb_5 = myclient_5 ["dcrbtc"]
mycol_5 = mydb_5 ["data"]
 
myclient_6 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/bqxbtc")
mydb_6 = myclient_6 ["bqxbtc"]
mycol_6 = mydb_6 ["data"] 

myclient_7 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/dashbtc")
mydb_7 = myclient_7 ["dashbtc"]
mycol_7 = mydb_7 ["data"]     # collection is mongo is same as a Table 


myclient_8 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/icxbtc")
mydb_8 = myclient_8 ["icxbtc"]
mycol_8 = mydb_8 ["data"]
 
myclient_9 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/iotabtc")
mydb_9 = myclient_9 ["iotabtc"]
mycol_9 = mydb_9 ["data"] 

myclient_10 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/kmdbtc")
mydb_10 = myclient_10 ["kmdbtc"]
mycol_10 = mydb_10 ["data"]     # collection is mongo is same as a Table 


myclient_11 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/manabtc")
mydb_11 = myclient_11 ["manabtc"]
mycol_11 = mydb_11 ["data"]
 
myclient_12 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/mtlbtc")
mydb_12 = myclient_12 ["mtlbtc"]
mycol_12 = mydb_12 ["data"] 


myclient_13 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/ontbtc")
mydb_13 = myclient_13 ["ontbtc"]
mycol_13 = mydb_13 ["data"]     # collection is mongo is same as a Table 


myclient_14 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/qkcbtc")
mydb_14 = myclient_14 ["qkcbtc"]
mycol_14 = mydb_14 ["data"]
 
myclient_15 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/rvnbtc")
mydb_15 = myclient_15 ["rvnbtc"]
mycol_15 = mydb_15 ["data"] 

myclient_16 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/thetabtc")
mydb_16 = myclient_16 ["thetabtc"]
mycol_16 = mydb_16 ["data"]     # collection is mongo is same as a Table 


myclient_17 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/xmrbtc")
mydb_17 = myclient_17 ["xmrbtc"]
mycol_17 = mydb_17 ["data"]
 
myclient_18 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds245234.mlab.com:45234/zecbtc")
mydb_18 = myclient_18 ["zecbtc"]
mycol_18 = mydb_18 ["data"] 

myclient_19 = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds145304.mlab.com:45304/zrxbtc")
mydb_19 = myclient_19 ["zrxbtc"]
mycol_19 = mydb_19 ["data"]     # collection is mongo is same as a Table 



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

def process_message3(a3):
    mydict_3 = [a3]
    mycol_3.insert_many(mydict_3)
    print(a3['k']['c'])

def process_message4(a4):
    mydict_4 = [a4]
    mycol_4.insert_many(mydict_4)
    print(a4['k']['c'])

def process_message5(a5):
    mydict_5 = [a5]
    mycol_5.insert_many(mydict_5)
    print(a5['k']['c'])

def process_message6(a6):
    mydict_6 = [a6]
    mycol_6.insert_many(mydict_6)
    print(a6['k']['c'])

def process_message7(a7):
    mydict_7 = [a7]
    mycol_7.insert_many(mydict_7)
    print(a7['k']['c'])

def process_message8(a8):
    mydict_8 = [a8]
    mycol_8.insert_many(mydict_8)
    print(a8['k']['c'])

def process_message9(a9):
    mydict_9 = [a9]
    mycol_9.insert_many(mydict_9)
    print(a9['k']['c'])

def process_message10(a10):
    mydict_10 = [a10]
    mycol_10.insert_many(mydict_10)
    print(a10['k']['c'])

def process_message11(a11):
    mydict_11 = [a11]
    mycol_11.insert_many(mydict_11)
    print(a11['k']['c'])

def process_message12(a12):
    mydict_12 = [a12]
    mycol_12.insert_many(mydict_12)
    print(a12['k']['c'])

def process_message13(a13):
    mydict_13 = [a13]
    mycol_13.insert_many(mydict_13)
    print(a13['k']['c'])

def process_message14(a14):
    mydict_14 = [a14]
    mycol_14.insert_many(mydict_14)
    print(a14['k']['c'])

def process_message15(a15):
    mydict_15 = [a15]
    mycol_15.insert_many(mydict_15)
    print(a15['k']['c'])

def process_message16(a16):
    mydict_16 = [a16]
    mycol_16.insert_many(mydict_16)
    print(a16['k']['c'])

def process_message17(a17):
    mydict_17 = [a17]
    mycol_17.insert_many(mydict_17)
    print(a17['k']['c'])

def process_message18(a18):
    mydict_18 = [a18]
    mycol_18.insert_many(mydict_18)
    print(a18['k']['c'])

def process_message19(a19):
    mydict_19 = [a19]
    mycol_19.insert_many(mydict_19)
    print(a19['k']['c'])



# 
    
    

conn_key = bm.start_kline_socket('MDABTC', process_message1, interval='15m')
conn_key = bm.start_kline_socket('GVTBTC', process_message2, interval = '15m')
conn_key = bm.start_kline_socket('EOSBTC', process_message3, interval='15m')
conn_key = bm.start_kline_socket('ADABTC', process_message4, interval = '15m')
conn_key = bm.start_kline_socket('DCRBTC', process_message5, interval = '15m')
conn_key = bm.start_kline_socket('BQXBTC', process_message6, interval='15m')
conn_key = bm.start_kline_socket('DASHBTC', process_message7, interval = '15m')
conn_key = bm.start_kline_socket('ICXBTC', process_message8, interval='15m')
conn_key = bm.start_kline_socket('IOTABTC', process_message9, interval = '15m')
conn_key = bm.start_kline_socket('KMDBTC', process_message10, interval='15m')
conn_key = bm.start_kline_socket('MANABTC', process_message11, interval = '15m')
conn_key = bm.start_kline_socket('MTLBTC', process_message12, interval='15m')
conn_key = bm.start_kline_socket('ONTBTC', process_message13, interval = '15m')
conn_key = bm.start_kline_socket('QKCBTC', process_message14, interval='15m')
conn_key = bm.start_kline_socket('RVNBTC', process_message15, interval = '15m')
conn_key = bm.start_kline_socket('THETABTC', process_message16, interval='15m')
conn_key = bm.start_kline_socket('XMRBTC', process_message17, interval = '15m')
conn_key = bm.start_kline_socket('ZECBTC', process_message18, interval='15m')
conn_key = bm.start_kline_socket('ZRXBTC', process_message19, interval = '15m')


bm.start()