# -*- coding: utf-8 -*-
#!/usr/bin/env python

import logging
import batchcompute
from const import *

class BCS:
    def __init__(self, config, pool_name, logger):
        # 获取bcs配置
        logger.info("ReadConfig. pool:%s" % pool_name)
        self.access_key_id = config.Get(SECTION_COMMON, 'access_key_id')
        self.access_key_secret = config.Get(SECTION_COMMON, 'access_key_secret')
        self.region = config.Get(pool_name, 'region')
        self.cluster_id = config.Get(pool_name, 'cluster_id')
        self.group_name = config.Get(pool_name, 'group_name')
        self.max_instance_count = config.GetInt(pool_name, 'max_instance_count')
        self.min_instance_count = config.GetInt(pool_name, 'min_instance_count')
        self.hostname_prefix = config.TryGet(pool_name, 'hostname_prefix')
        self.logger = logger
        logger.info("ReadConfig. pool:%s, access_key_id:%s" % (pool_name, self.access_key_id))
        logger.info("ReadConfig. pool:%s, access_key_secret:%s" % (pool_name, self.access_key_secret))
        logger.info("ReadConfig. pool:%s, region:%s" % (pool_name, self.region))
        logger.info("ReadConfig. pool:%s, cluster_id:%s" % (pool_name, self.cluster_id))
        logger.info("ReadConfig. pool:%s, group_name:%s" % (pool_name, self.group_name))
        logger.info("ReadConfig. pool:%s, max_instance_count:%d" % (pool_name, self.max_instance_count))
        logger.info("ReadConfig. pool:%s, min_instance_count:%d" % (pool_name, self.min_instance_count))
        logger.info("ReadConfig. pool:%s, hostname_prefix:%s" % (pool_name, self.hostname_prefix))

        #创建bcs client
        ENDPOINT = "batchcompute.%s.aliyuncs.com" % self.region
        self.logger.info("ReadConfig, pool:%s, endpoint:%s" % (pool_name, ENDPOINT))
        batchcompute.Client.register_region(self.region, ENDPOINT)
        self.client = batchcompute.Client(ENDPOINT, self.access_key_id, self.access_key_secret)
        
    def GetCluster(self):
        rsp = self.client.get_cluster(self.cluster_id)
        try:
            rsp = self.client.get_cluster(self.cluster_id)
            self.logger.debug("Id:%s, Name:%s, State:%s" % (rsp.Id, rsp.Name, rsp.State))
            return rsp
        except batchcompute.ClientError, e:
            self.logger.error("%s, %s, %s, %s" % (e.get_status_code(), e.get_code(), e.get_requestid(), e.get_msg()))
            raise Exception("GetCluster Failed")


    def ListClusterInstances(self):
        try:
            all_instance = {}
            marker = ""
            max_item = 10
            instances_cnt = 0
            while 1:
                response = self.client.list_cluster_instances(self.cluster_id, self.group_name, marker, max_item)
                marker = response.NextMarker
                instances_cnt += len(response.Items)
                for cluster_instance in response.Items:
                    self.logger.debug("Id:%s, Ip:%s" % (cluster_instance.Id, cluster_instance.IpAddress))
                    all_instance[cluster_instance.HostName] = cluster_instance
                if marker.strip() == '':
                    break
            self.logger.debug('Total instances: %s' % instances_cnt)
            return all_instance
        except batchcompute.ClientError, e:
            self.logger.error("%s, %s, %s, %s" % (e.get_status_code(), e.get_code(), e.get_requestid(), e.get_msg()))
            raise Exception("ListClusterInstancesFailed!", self.cluster_id, self.group_name)

    def GetClusterInstanceCount(self):
        #获取集群
        cluster = self.GetCluster()
        
        #取group中的实例信息
        for name in cluster.Groups:
            group_info = cluster.Groups[name]
            if self.group_name != name:
                continue
            self.logger.info("Cluster:%s, Group:%s, DesiredVMCount:%s, ActualVMCount:%s" % (self.cluster_id, self.group_name, group_info.DesiredVMCount, group_info.ActualVMCount))
            return group_info.DesiredVMCount, group_info.ActualVMCount

        self.logger.error("Notfound Cluster:%s, Group:%s" % (self.cluster_id, self.group_name))
        raise Exception("NotFoundCLusterGroup", self.cluster_id, self.group_name)
    
    def ChangeClusterInstanceCount(self, count):
        try:
            #self.client.change_cluster_desired_vm_count(self.cluster_id, AlluxioWoker=count)
            modify_desc = batchcompute.resources.ModifyClusterDescription()
            group_desc = batchcompute.resources.ModifyGroupDescription()
            group_desc.DesiredVMCount = count
            modify_desc.add_group(self.group_name, group_desc)
            rsp = self.client.modify_cluster(self.cluster_id, modify_desc)
            self.logger.info("ChangeInstanceCountDone, Cluster:%s, Group:%s, Count:%s" % (self.cluster_id, self.group_name, count))
        except batchcompute.ClientError, e:
            self.logger.error("%s, %s, %s, %s" % (e.get_status_code(), e.get_code(), e.get_requestid(), e.get_msg()))
            raise Exception("ChangeInstanceCountFailed", self.cluster_id, self.group_name, count)

    def DeleteInstance(self, instance_id):
        try:
            self.client.delete_cluster_instance(self.cluster_id, self.group_name, instance_id)
            self.logger.info("DeleteInstance Cluster:%s, Group:%s, InstanceId:%s" % (self.cluster_id, self.group_name, instance_id))
        except batchcompute.ClientError, e:
            self.logger.error("%s, %s, %s, %s" % (e.get_status_code(), e.get_code(), e.get_requestid(), e.get_msg()))
            raise Exception("DeleteInstanceFailed", self.cluster_id, self.group_name, instance_id)
