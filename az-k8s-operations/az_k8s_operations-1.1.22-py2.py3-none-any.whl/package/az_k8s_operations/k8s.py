from azure.mgmt.containerservice  import ContainerServiceClient
from azure.common.credentials import ServicePrincipalCredentials

def upgradetolatestversion(azure_credential,subscription,resource_group_name,resource_name):
    print("===Start : upgradetolatestversion===")
    print((subscription+'/'+resource_group_name+'/'+resource_name))
    k8sclient = ContainerServiceClient(azure_credential,subscription)
    upgradeprofile = k8sclient.managed_clusters.get_upgrade_profile(resource_group_name,resource_name)
    currentmanagedcluster = k8sclient.managed_clusters.get(resource_group_name, resource_name)
    currentversion=currentmanagedcluster.kubernetes_version
    version=currentmanagedcluster.kubernetes_version
    if upgradeprofile.control_plane_profile.upgrades :
     for upversion in upgradeprofile.control_plane_profile.upgrades:
      if not upversion.is_preview:
       if upversion.kubernetes_version > version:
        version = upversion.kubernetes_version
        currentmanagedcluster.kubernetes_version = upversion.kubernetes_version
     if currentmanagedcluster.provisioning_state == 'Succeeded' and version > currentversion :
      # Needs to be contributor on K8S cluster and on log analytics workspace linked to k8s 
      print((subscription+'/'+resource_group_name+'/'+resource_name+'Upgrade from '+str(currentversion)+' to '+str(version)))  
      try:
          upgradedmanagedcluster = k8sclient.managed_clusters.create_or_update(resource_group_name, resource_name,currentmanagedcluster )
          result={'subscription':subscription,'resourceGroup':resource_group_name,
             'cluster':resource_name,'initialVersion':str(currentversion),'targetVersion':str(version),'status':'OK'}
          print("done")
      except  Exception as e: 
          print(("WARNING: - " +subscription+'/'+resource_group_name+'/'+resource_name+'Upgrade from '+str(currentversion)+' to '+str(version)+': '+str(e)))
          result={'subscription':subscription,'resourceGroup':resource_group_name,
             'cluster':resource_name,'initialVersion':str(currentversion),'targetVersion':str(version),'status':'KO'+str(e)}
     else:
        print(('NO UPGRADE POSSIBLE '+currentversion+' = '+version))
        result={'subscription':subscription,'resourceGroup':resource_group_name,
             'cluster':resource_name,'initialVersion':str(currentversion),'targetVersion':str(version),'status':'NO'}
    else:
     print(('NO UPGRADE POSSIBLE for '+subscription+'/'+resource_group_name+'/'+resource_name))
     result={'subscription':subscription,'resourceGroup':resource_group_name,
             'cluster':resource_name,'initialVersion':str(currentversion),'targetVersion':str(version),'status':'NO'}
     print((upgradeprofile.control_plane_profile.kubernetes_version))
    print("===End : upgradetolatestversion===")
    return result


