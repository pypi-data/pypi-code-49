# -*- coding: utf-8 -*-
import sqlalchemy, sys
import numpy as np
import pandas as pd
from dateutil.parser import parse
from .DatabaseManager import *

def ProductIdFromInstrumentId(instrumentId):
    return instrumentId[:re.search("\d", instrumentId).start()]

def StockIdToTableName(stockId):
	parts = stockId.lower().split(".")
	return parts[1] +  parts[0]

def IsValidDate(strdate):
    try:
        if "-" in strdate:
            datetime.datetime.strptime(strdate, "%Y-%m-%d")
        else:
            datetime.datetime.strptime(strdate, "%Y%m%d")
        return True
    except:
        return False

#将列表拆分成长度尽可能平均的子列表
def Chunks(arr, m):
	n = int(np.ceil(len(arr) / float(m)))
	return [arr[i:i + n] for i in range(0, len(arr), n)]

def TimestampToSecondsCount(timestamp):
	return 3600*timestamp.hour + 60*timestamp.minute + timestamp.second

def TimeOfDayToSecondsCount(todStr):
	todParts = todStr.split(":")
	return 3600*int(todParts[0]) + 60*int(todParts[1]) + int(todParts[2])

def TickOfSecond(millisec):
	if millisec < 500:
		return 0
	else:
		return 1

#每秒2次的Tick数据时间戳转化为对齐字段TickLabel
def T2TimeStampToTickLabel(todStr, millisec):
	return 2*TimeOfDayToSecondsCount(todStr) + TickOfSecond(millisec)

def TimeStampToT2TickLabel(todStr, millisec):
	return 2*TimeOfDayToSecondsCount(todStr) + TickOfSecond(millisec)

#N秒一次的Tick数据时间戳转化为对齐字段TickLabel
def TimeStampToNSecTickLabel(timestamp, n):
	return n*int((TimestampToSecondsCount(timestamp)+n-1)/n)

#N秒一次的Tick数据时间字符串转化为对齐字段TickLabel
def TimeOfDayToNSecTickLabel(todStr, n):
	return n*int((TimeOfDayToSecondsCount(todStr)+n-1)/n)

def VolumeWeighedPrice(bidPrice1, bidVolume1, askPrice1, askVolume1):
	return (bidPrice1*askVolume1 + askPrice1*bidVolume1)/(bidVolume1 + askVolume1)

class DataUtils(object):
	dbManager = DatabaseManager()

#期货数据接口
class FuturesDataUtils(DataUtils):
	def __init__(self, dataSource):
		if not dataSource in ['cffex-l1', 'shfe-l1', 'ine-l1', 'dce-l1', 'czce-l1', 'cffex-l2', 'shfe-l2', 'ine-l2', 'dce-l2', 'czce-l2']:
			print('HiggsBoom FuturesDataUtils: error, unknown data source %s' % dataSource)
			sys.exit(-1)
		self.dataSource = dataSource
		self.exchangeId = dataSource.split('-')[0].upper()
		print('HiggsBoom: initializing futures data engine for %s' % self.dataSource)

	def TickDataFrame(self, instrument, tradingDate):
		try:
			tradingDate = str(parse(tradingDate).date()).replace('-', '')
			instrumentId = instrument
			if '_V' in instrument:
				parts = instrument.split('_V')
				summaryDf = self.DailySummaryFrame(parts[0], tradingDate).sort_values(by=['TotalVolume'], ascending=False)
				instrumentId = list(summaryDf['InstrumentId'])[int(parts[1])]
			tableName = '%s_%s' % (self.exchangeId, tradingDate)
			selectSql = "SELECT * FROM %s WHERE instrumentId='%s'" % (tableName, instrumentId)
			tickFrame = pd.DataFrame(DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql), columns=[x[0].upper() + x[1:] for x in DataUtils.dbManager.GetTableColumns(self.dataSource, tableName)])
			return tickFrame
		except:
			print("error, failed to get tick data for %s on %s" % (instrument, tradingDate))

	def DailySummaryFrame(self, productId, tradingDate):
		tradingDate = str(parse(tradingDate).date()).replace('-', '')
		selectSql = "SELECT * FROM %s_summary WHERE ProductId='%s' AND ProductType='FUT' AND TradingDate='%s'" % (self.exchangeId, productId, tradingDate)
		return pd.DataFrame(DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql), columns=DataUtils.dbManager.GetTableColumns(self.dataSource, '%s_summary' % self.exchangeId))

	def TradingDays(self, productId):
		selectSql = "SELECT DISTINCT TradingDate FROM %s_summary WHERE ProductId='%s' AND ProductType='FUT'" % (self.exchangeId, productId)
		tdList = [x[0] for x in DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql)]
		tdList.sort()
		return tdList

#A股Tick级数据接口
class AStockTickDataUtils(DataUtils):
	def __init__(self):
		self.dataSource = 'astock-tick'
		print('HiggsBoom: initializing tick data engine for A-stocks')

	def InstrumentList(self, instType, tradingDate):
		selectSql = "SELECT InstrumentId FROM tick_summary WHERE InstrumentType='%s' AND TradingDate='%s'" % (instType, str(parse(tradingDate).date()))
		return [x[0] for x in DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql)]

	def TradingDays(self):
		selectSql = "SELECT DISTINCT TradingDate FROM tick_summary"
		tdList = [str(x[0]) for x in DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql)]
		tdList.sort()
		return tdList

	def TickDataFrame(self, instrument, tradingDate):
		try:
			tableName = StockIdToTableName(instrument)
			selectSql = "SELECT * FROM %s WHERE DATE(Timestamp)='%s'" % (tableName, str(parse(tradingDate).date()))
			return pd.DataFrame(DataUtils.dbManager.GetQueryResult(self.dataSource, selectSql), columns=[x[0].upper() + x[1:] for x in DataUtils.dbManager.GetTableColumns(self.dataSource, tableName)])
		except:
			print("error, failed to get tick data for %s on %s" % (instrument, tradingDate))
