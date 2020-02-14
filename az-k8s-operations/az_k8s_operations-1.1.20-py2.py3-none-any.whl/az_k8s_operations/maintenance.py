from azure.mgmt.containerservice  import ContainerServiceClient
from azure.graphrbac import GraphRbacManagementClient
from azure.identity import ClientSecretCredential
from az_k8s_operations import spn 
from az_k8s_operations import common as cn
from time import sleep 
from az_k8s_operations import azdevops
from msrest.authentication import BasicAuthentication
import credential
import re


def get_kv_infra(azure_credential, subscription_id, resource_group_name):
    """ try to find kv infra in rg """
    list_kv = cn.getResource(azure_credential,subscription_id,resource_group_name,  'Microsoft.KeyVault/vaults')
    if  len(list_kv) == 1 :
        print(('We found : https://'+list_kv[0]+'.vault.azure.net'))
        return 'https://'+list_kv[0]+'.vault.azure.net'
    elif len(list_kv) == 0 :
        print('we need to create one')
        return ''
    else:
        for kv in list_kv:
            if re.search('infra', kv):
              print(('We found: https://'+kv+'.vault.azure.net'))
              return 'https://'+kv+'.vault.azure.net'
        print('ERROR: Several kv founds but no kv infra found')
        return ''


def update_service_connection_projects(credential, organization_url,spn_id,spn_key):
    """ Update all service connection of project which have spn_id as user"""
    list_projects=azdevops.list_projects(credential,organization_url)
    for project in list_projects :
        list_service_connection=azdevops.getserviceendpoint(credential,organization_url, project)
        for service_connection in list_service_connection:
            if service_connection.type == 'azurerm' :
                if  service_connection.authorization.parameters != None :
                 if service_connection.authorization.scheme == 'ServicePrincipal':
                  if service_connection.authorization.parameters['serviceprincipalid'] == spn_id :
                   print(("We update service connection "+service_connection.name+" in "+project))
                   azdevops.updateserviceendpointazurermcredential(credential,organization_url, project, spn_id,spn_key)





def rotateKeysForK8sCluster( azure_credential,graph_credential,azdevops_credential,TENANT_ID, subscription,resource_group_name,cluster_name,nbDays,organization_url):
    """ Rotate spn key of cluster and spn key for server rbac spn
        Find kv in Rg of cluster (if only one we take it if several we take one which contains 'infra'
        Update kv infra in rg
        Update service connection of linked azure devops project
        Delete old keys """

    print(("==Start of rotateKeysForK8sCluster for cluster "+subscription+" "+resource_group_name+" "+cluster_name))
    list_keys_name=[]
    vaultUrl =  get_kv_infra(azure_credential,subscription, resource_group_name)
    if vaultUrl == '':
        print('ERROR KV')
        return 99
    graphrbac_client = GraphRbacManagementClient(graph_credential, TENANT_ID)
    K8sClient = ContainerServiceClient(azure_credential,subscription)
    cluster = K8sClient.managed_clusters.get(resource_group_name,cluster_name)
    listKeys = graphrbac_client.applications.list_password_credentials(spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.service_principal_profile.client_id ))
    for key in listKeys:
        if key.custom_key_identifier:
            list_keys_name.append(key.custom_key_identifier.decode("utf8"))
    newKeyValueCluster = spn.update_password_key(graph_credential,TENANT_ID,
             spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.service_principal_profile.client_id ), nbDays,'Cluster',"create")
    update_service_connection_projects(azdevops_credential, organization_url,cluster.service_principal_profile.client_id,newKeyValueCluster['value'])
    sleep(60)
    while not spn.checkKeyCreation(graph_credential,TENANT_ID,cluster.service_principal_profile.client_id, newKeyValueCluster['key_custom_name']):
        sleep(3)

    client_secret_credential = ClientSecretCredential(TENANT_ID, cluster.service_principal_profile.client_id,newKeyValueCluster['value'])
    result=cn.setKeyvaultSecret(client_secret_credential,vaultUrl,'spappid',cluster.service_principal_profile.client_id)
    result=cn.setKeyvaultSecret(client_secret_credential,vaultUrl,'sppasswd',newKeyValueCluster['value'])
    print(("We reset service principale of  K8s cluster "+cluster.service_principal_profile.client_id))
    try:
        K8sClient.managed_clusters.reset_service_principal_profile(resource_group_name, cluster_name, cluster.service_principal_profile.client_id,secret=newKeyValueCluster['value'])
        print("Reset sp of K8s: OK")
    except Exception as e:
        print(("WARNING: "+str(e)))
    print('Launch cleaning')
    for key in list_keys_name:
     KeyValueCluster = spn.update_password_key(graph_credential,TENANT_ID,
             spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.service_principal_profile.client_id),0,key,'delete' )
    if cluster.aad_profile:
     listKeys = graphrbac_client.applications.list_password_credentials(spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.aad_profile.server_app_id ))
     for key in listKeys:
        if key.custom_key_identifier:
            list_keys_name.append(key.custom_key_identifier.decode("utf8"))
     newKeyValueServer = spn.update_password_key(graph_credential,TENANT_ID,spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.aad_profile.server_app_id ), nbDays,'rbacServer',"create")
     result=cn.setKeyvaultSecret(client_secret_credential,vaultUrl,'servappid',cluster.aad_profile.server_app_id)
     result=cn.setKeyvaultSecret(client_secret_credential,vaultUrl,'servpasswd',newKeyValueServer['value'])
     sleep(60)
     while not spn.checkKeyCreation(graph_credential,TENANT_ID,cluster.aad_profile.server_app_id, newKeyValueServer['key_custom_name']):
        sleep(3)
     print(("We reset aad profile of  K8s cluster "+cluster.aad_profile.server_app_id))
     parameters = cluster.aad_profile
     parameters.server_app_secret = newKeyValueServer['value']
     try:
         K8sClient.managed_clusters.reset_aad_profile(resource_group_name, cluster_name,parameters) 
         print("Reset aad profile of K8s: OK")
     except Exception as e:
        print(("WARNING: "+str(e)))
     print('Launch cleaning')
     for key in list_keys_name:
      KeyValueCluster = spn.update_password_key(graph_credential,TENANT_ID,
             spn.getObjectIdFromAppId(TENANT_ID,graph_credential,cluster.aad_profile.server_app_id),0,key,'delete' )
    print(("==End of rotateKeysForK8sCluster for cluster "+subscription+" "+resource_group_name+" "+cluster_name))
