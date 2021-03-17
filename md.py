#coding=utf-8
import thostmduserapi as mdapi
import os
import csv
import json
import time
from dbfactory import DbFactory
subid=["cu2102","cu2103","cu2104","cu2101"]
class mymdspi(mdapi.CThostFtdcMdSpi):

    def __init__(self,tapi:mdapi.CThostFtdcMdApi):

        mdapi.CThostFtdcMdSpi.__init__(self)
        self.tapi=tapi
     
    def Savedatatocsv(self,InstrumentID,mdlist):
        if(os.path.exists(os.getcwd()+'\\data\\')==False):
            os.mkdir(os.getcwd()+'\\data\\')
        filepath=os.getcwd()+f'\data\{InstrumentID}.csv'
        if os.path.exists(path=filepath)==False:
            head=(['交易日','合约代码','交易所代码','合约在交易所的代码','最新价','上次结算价','昨收盘价','昨持仓量','今开盘价','最高价','最低价','数量','成交金额','持仓量','今收盘价',
                  '本次结算价','涨停板价','跌停板价','昨虚实度','今虚实度','最后修改时间','最后修改毫秒','申买价一','申买量一','申卖价一','申卖量一','当日均价','业务日期'])
            with open(file=filepath,mode='w') as f:
                writer=csv.writer(f,dialect='excel')
                writer.writerow(head)
                writer.writerow(mdlist)
                
        else:
            with open(file=filepath,mode='a') as f:
                writer=csv.writer(f,dialect='excel')
                writer.writerow(mdlist)

    def saveredis(self,mdlist):
        fielddic=[
        'TradingDay',
        'InstrumentID',
        'ExchangeID',
        'ExchangeInstID',
        'LastPrice',
        'PreSettlementPrice',
        'PreClosePrice',
        'PreOpenInterest',
        'OpenPrice',
        'HighestPrice',
        'LowestPrice',
        'Volume',
        'Turnover',
        'OpenInterest',
        'ClosePrice',
        'SettlementPrice',
        'UpperLimitPrice',
        'LowerLimitPrice',
        'PreDelta',
        'CurrDelta',
        'UpdateTime',
        'UpdateMillisec',
        'BidVolume1',
        'AskPrice1',
        'AskVolume1',
        'AveragePrice',
        'ActionDay'
        ]
        dbf=DbFactory('redis')
        redis=dbf.createdb()
        i=0
        dic={}
        sore=mdlist[0]
        datakey=f'{mdlist[1]}.data.{sore}'
        sorekey=f'{mdlist[1]}.sore'
        redis.zadd(name=sorekey,mapping={datakey:sore})
        for field in fielddic:
            v=mdlist[i]
            if not v:
                v=""
            redis.hset(name=datakey,key=field,value=v)
            i+=1
        #redis.hmset(name=mdlist[1],mapping=dic)
        #redis.hset(name=mdlist[0],mapping=dic)
        redis.close()


    def OnFrontConnected(self) ->"void":

        #print("建立连接前执行初始化登陆字段\n")
        myfield=mdapi.CThostFtdcReqUserLoginField()
        myfield.BrokerID="8000"
        myfield.UserID="000005"
        myfield.Password="123456"
        myfield.InterfaceProductInfo="python dll"
        self.tapi.ReqUserLogin(myfield,0)
        
        
    
      


    def OnRspUserLogin(self, pRspUserLogin: 'CThostFtdcRspUserLoginField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
        #print("登陆成功后执行\n")
        print("登陆成功\n")
        ret=self.tapi.SubscribeMarketData([id.encode('utf-8') for id in subid],len(subid))#订阅行情
        if ret==-1:
            raise Exception('网络连接失败')
        elif ret==-2:
            raise Exception('未请求数超过许可数')
        elif ret==-3:
            raise Exception('每秒发送请求超过许可数')
        
        
        


    def OnRtnDepthMarketData(self, pDepthMarketData: mdapi.CThostFtdcDepthMarketDataField) -> "void":
        #print("响应行情订阅，开始推送行情\n")
        
        print('合约代码|最新价|最高价|最低价|数量|成交金额|业务日期|最后修改时间|昨天结算价')
        print("----------------------------------------------------------------------------\n")
        print(f"{pDepthMarketData.InstrumentID}|{pDepthMarketData.LastPrice}|{pDepthMarketData.HighestPrice}+|{pDepthMarketData.LowestPrice}|{pDepthMarketData.Volume}|{pDepthMarketData.Turnover}|{pDepthMarketData.ActionDay}|{pDepthMarketData.UpdateTime}|{pDepthMarketData.PreSettlementPrice}\n")
        mdlist=([pDepthMarketData.TradingDay,\
        pDepthMarketData.InstrumentID,\
        pDepthMarketData.ExchangeID,\
        pDepthMarketData.ExchangeInstID,\
        pDepthMarketData.LastPrice,\
        pDepthMarketData.PreSettlementPrice,\
        pDepthMarketData.PreClosePrice,\
        pDepthMarketData.PreOpenInterest,\
        pDepthMarketData.OpenPrice,\
        pDepthMarketData.HighestPrice,\
        pDepthMarketData.LowestPrice,\
        pDepthMarketData.Volume,\
        pDepthMarketData.Turnover,\
        pDepthMarketData.OpenInterest,\
        pDepthMarketData.ClosePrice,\
        pDepthMarketData.SettlementPrice,\
        pDepthMarketData.UpperLimitPrice,\
        pDepthMarketData.LowerLimitPrice,\
        pDepthMarketData.PreDelta,\
        pDepthMarketData.CurrDelta,\
        pDepthMarketData.UpdateTime,\
        pDepthMarketData.UpdateMillisec,\
        pDepthMarketData.BidPrice1,\
        pDepthMarketData.BidVolume1,\
        pDepthMarketData.AskPrice1,\
        pDepthMarketData.AskVolume1,\
        pDepthMarketData.AveragePrice,\
        pDepthMarketData.ActionDay])
        self.Savedatatocsv(pDepthMarketData.InstrumentID,mdlist)
        try:
            self.saveredis(mdlist)
        except Exception as e:
            print('%s' %e)
        
       

    def OnRspSubMarketData(self, pSpecificInstrument: 'CThostFtdcSpecificInstrumentField', pRspInfo:mdapi.CThostFtdcRspInfoField, nRequestID: 'int', bIsLast: 'bool') -> "void":
        #print("订阅行情后进行应答\n")
        pass
        
def run(qzip:str):
    mapi=mdapi.CThostFtdcMdApi_CreateFtdcMdApi()
    mspi=mymdspi(mapi)
    print(qzip)
    mapi.RegisterFront(f'tcp://{qzip}')
    mapi.RegisterSpi(mspi)
    mapi.Init()
    mapi.Join()

def getipcount():
    with open(os.getcwd()+'\\前置机地址.txt','r')as f:
        return len(f.readlines())
         
def getipmachine(i):
    
    with open(os.getcwd()+'\\前置机地址.txt','r')as f:
        res=f.readlines()
        return res[i]
    
def testnetword():
    result=os.system('@ping www.baidu.com>nul')
    return result
def main():
    os.system('chcp 65001')
    os.system('color 9F')
    os.system('mode con cols=107 lines=34')
    os.system('title=CTP行情数据收集系统')
    os.system('cls')
    nres=testnetword()
    print('CTP行情数据收集系统\n'.center(100))
    dbf=DbFactory('redis')
    db=dbf.createdb()
    for key in db.keys():
        db.delete(key)
    if nres==1:
        print('网络连接失败，请检查网络连接！')
        while testnetword():
            pass
    ic=iter(list(range(getipcount())))
    try:
        
        run(getipmachine(next(ic)))
    except:
        print('正在切换前置机地址进行尝试。。')
        run(getipmachine(next(ic)))
            

if __name__=="__main__":
    main()





        
       



        


