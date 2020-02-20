
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.rdbms.mysql import MySQLManagementClient
from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient
from azure.mgmt.sql import SqlManagementClient

def getVmDetails(credentials, subscription, rgName, vmName ):
 """
 Retrieve dict containing VM details
 """
 print(("== Start of getVmDetails for "+subscription['name']+" "+rgName+" "+vmName+"=="))
 client = ComputeManagementClient(credentials, subscription['id'])
 result=client.virtual_machines.get(rgName,vmName)
 StopHour = ''
 EnableWe = ''
 myOs = ''
 if result.tags:
  if 'StopHour' in result.tags:
    StopHour = str(result.tags['StopHour'])
  if 'EnableWe' in result.tags:
    EnableWe = str(result.tags['EnableWe'])
 if result.storage_profile:
   myOs = str(result.storage_profile.image_reference.publisher)+"="\
         +str(result.storage_profile.image_reference.offer)+"="\
         +str(result.storage_profile.image_reference.sku)
 vmDetail = {
 'subscription':subscription['name'],
 'rgName':rgName,
 'vmName':vmName,
 'Type':result.hardware_profile.vm_size,
 'os': myOs,
 'osDiskSizeGb':result.storage_profile.os_disk.disk_size_gb,
 'nbDataDisk':len(result.storage_profile.data_disks),
 'nbNic':len(result.network_profile.network_interfaces),
 'StopHour':StopHour,
 'EnableWe':EnableWe
         }
 print(("== End of getVmDetails for "+subscription['name']+" "+rgName+" "+vmName+"=="))
 return vmDetail

def getSqlDetails(credentials, subscription, rgName, serverName ):
 """
 Retrieve dict containing Db details
 """
 print(("== Start of getSqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 client = SqlManagementClient(credentials, subscription['id'])
 result = client.servers.get(rgName, serverName)
 resultdb = client.databases.list_by_server(rgName, serverName)
 nb = 0
 listDb=''
 for db in resultdb:
  nb+=1
  listDb += db.name+", "
 dbDetail={
 'subscription':subscription['name'],
 'rgName':rgName,
 'serverName':serverName,
 'type':result.sku.name,
 'version':"Mysql "+result.version,
 'nbDb': nb,
 'listDb': listDb,
 'backup_retention_days': result.storage_profile.backup_retention_days,
 'geo_redundant_backup': result.storage_profile.geo_redundant_backup,
 'storage_mb': result.storage_profile.storage_mb
         }
 print(("== End of getSqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 return dbDetail

def getPSqlDetails(credentials, subscription, rgName, serverName ):
 """
 Retrieve dict containing Db details
 """
 print(("== Start of getPSqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 client = PostgreSQLManagementClient(credentials, subscription['id'])
 result = client.servers.get(rgName, serverName)
 resultdb = client.databases.list_by_server(rgName, serverName)
 nb = 0
 listDb=''
 for db in resultdb:
  nb+=1
  listDb += db.name+", "
 dbDetail={
 'subscription':subscription['name'],
 'rgName':rgName,
 'serverName':serverName,
 'type':result.sku.name,
 'version':"Mysql "+result.version,
 'nbDb': nb,
 'listDb': listDb,
 'backup_retention_days': result.storage_profile.backup_retention_days,
 'geo_redundant_backup': result.storage_profile.geo_redundant_backup,
 'storage_mb': result.storage_profile.storage_mb
         }
 print(("== End of getPSqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 return dbDetail

def getMySqlDetails(credentials, subscription, rgName, serverName ):
 """
 Retrieve dict containing Db details
 """
 print(("== Start of getMySqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 client = MySQLManagementClient(credentials, subscription['id'])
 result = client.servers.get(rgName, serverName)
 resultdb = client.databases.list_by_server(rgName, serverName)
 nb = 0
 listDb=''
 for db in resultdb:
  nb+=1
  listDb += db.name+", "
 dbDetail={
 'subscription':subscription['name'],
 'rgName':rgName,
 'serverName':serverName,
 'type':result.sku.name,
 'version':"Mysql "+result.version,
 'nbDb': nb,
 'listDb': listDb,
 'backup_retention_days': result.storage_profile.backup_retention_days,
 'geo_redundant_backup': result.storage_profile.geo_redundant_backup,
 'storage_mb': result.storage_profile.storage_mb
         }
 print(("== End of getMySqlDbDetails for "+subscription['name']+" "+rgName+" "+serverName+"=="))
 return dbDetail

def getResourcesFromAppName(credentials, subscription, AppName):
 """
 Retrieves a list of resources in Azure that contain a specific tag with a certain value.
 :param credentials: Credential to login.
 :param subscription_id: Subscription id.
 :param AppName: The AppName in CMDB.
 :return: A list of resources matching the tag criteria
 """
 print(("== Start of getResourcesFromAppName for "+subscription['name']+"=="))
 listResources=[]
 listVmsDetail=[]
 listMySqlDetail=[]
 listPSqlDetail=[]
 listSqlDetail=[]
 client = ResourceManagementClient(credentials, subscription['id'])
 myFilter="tagName eq 'AppName' and TagValue eq '"+AppName+"'"
 for rg in  client.resource_groups.list(filter=myFilter):
  for resource in client.resources.list_by_resource_group(rg.name):
   line = rg.name+" ;"+resource.name+" ;"+resource.type+" ;"+resource.location+" ;"\
           +str(resource.kind)+" ;"
   skuName = ''
   skuTier = ''
   skuCapacity = ''
   if resource.sku:
    skuName = str(resource.sku.name)
    skuTier = str(resource.sku.tier)
    skuCapacity = str(resource.sku.capacity)
 #  if str(resource.type) == 'Microsoft.Sql/servers/databases':
 #   listSqlDetail.append(getSqlDetails(credentials,subscription,rg.name,resource.name))
   if str(resource.type) == 'Microsoft.Compute/virtualMachines':
    listVmsDetail.append(getVmDetails(credentials,subscription,rg.name,resource.name))
   if str(resource.type) == 'Microsoft.DBforMySQL/servers':
    listMySqlDetail.append(getMySqlDetails(credentials,subscription,rg.name,resource.name))
   listResources.append({'subcription':subscription['name'],'rgName':rg.name,\
           'name':resource.name,'type':str(resource.type),'location':str(resource.location),\
           'kind':str(resource.kind),'skuName':skuName,'skuTier':skuTier,\
           'skuCapacity':skuCapacity})
 print ("== End of gerResourcesFromAppName==")
 return [listResources,listVmsDetail, listMySqlDetail]
