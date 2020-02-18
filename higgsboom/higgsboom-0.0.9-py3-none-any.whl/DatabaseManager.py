import sqlalchemy
import sqlalchemy.orm
import pandas as pd

def EngineConfigToCreateStr(config):
	createStr = config['dbEngine']
	if 'dbDriver' in config:
		createStr += '+%s' % config['dbDriver']
	createStr += '://%s' % config['user']
	if 'passwd' in config:
		createStr += ':%s' % config['passwd']
	createStr += '@%s' % config['host']
	if 'port' in config:
		createStr += ':%d' % config['port']
	if 'dbName' in config:
		createStr += '/%s' % config['dbName']
	return createStr

def DataSourceToDatabaseName(dataSource):
	if dataSource in ['cffex-l1', 'shfe-l1', 'ine-l1', 'dce-l1', 'czce-l1']:
		return 'Level1Md'
	elif dataSource in ['cffex-l2', 'shfe-l2', 'ine-l2', 'dce-l2', 'czce-l2']:
		return 'Level2Md'
	elif dataSource == 'astock-daily':
		return 'ASTOCK-DAILY'
	elif dataSource == 'astock-minute':
		return 'ASTOCK-MINUTE'
	elif dataSource == 'astock-tick':
		return 'ASTOCK-TICK'
	else:
		return 'UknownDB'


class DatabaseManager(object):
	dbList = ['Level1Md', 'Level2Md', 'ASTOCK-DAILY', 'ASTOCK-MINUTE', 'ASTOCK-TICK']

	def __init__(self):
		self.dbEngines = dict()
		self.dbSessions = dict()

	def InitDataEngine(self, dbName):
		dbConfig = dict()
		dbConfig['dbEngine'] = 'mysql'
		dbConfig['passwd'] = 'Higgs1401'
		dbConfig['user'] = 'mdreader'
		dbConfig['host'] = '10.214.0.21'
		dbConfig['dbName'] = dbName
		self.dbEngines[dbName] = sqlalchemy.create_engine(EngineConfigToCreateStr(dbConfig), echo=False)
		self.dbSessions[dbName] = sqlalchemy.orm.sessionmaker(bind=self.dbEngines[dbName])()

	def GetTableColumns(self, dataSource, tableName):
		dbName = DataSourceToDatabaseName(dataSource)
		if not dbName in DatabaseManager.dbList:
			print('error, no corresponding database for %s' % dataSource)
			return None
		if not dbName in self.dbEngines.keys():
			self.InitDataEngine(dbName)
		return [x['name'] for x in sqlalchemy.inspect(self.dbEngines[dbName]).get_columns(tableName)]

	def GetQueryResult(self, dataSource, sql):
		dbName = DataSourceToDatabaseName(dataSource)
		if not dbName in DatabaseManager.dbList:
			print('error, no corresponding database for %s' % dataSource)
			return None
		if not dbName in self.dbEngines.keys():
			self.InitDataEngine(dbName)
		return self.dbSessions[dbName].execute(sql).fetchall()

