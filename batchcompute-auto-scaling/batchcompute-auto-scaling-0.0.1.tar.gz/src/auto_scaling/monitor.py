#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
import bcs
import deadline
import config as cfg
import time
from const import *

class Moniter:
    def __init__(self, conf):
        # config
        self.config = cfg.Config(conf)

        # Logger 
        logName = self.config.TryGet(SECTION_COMMON, 'log_name', 'deadline_bcs.log')
        logging.basicConfig(filename=logName, level = logging.DEBUG,format = '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d:%(funcName)s] : %(message)s')
        self.logger = logging.getLogger(logName)

        # common config
        self.logger.info('GetCommonConfig')
        self.server_type = self.config.Get(SECTION_COMMON, 'server_type')
        self.instance_add_step = self.config.TryGetInt(SECTION_COMMON, 'instance_add_step', 10)
        self.moniter_interval = self.config.TryGetInt(SECTION_COMMON, 'moniter_interval', 30)
        self.create_instance_threshold = self.config.TryGetFloat(SECTION_COMMON, 'create_instance_threshold', 1.0)
        self.release_instance_waiting_time = self.config.TryGetInt(SECTION_COMMON, 'release_instance_waiting_time', 60)
        self.logger.info("ReadConfig, server_type:%r" % self.server_type)
        self.logger.info("ReadConfig, instance_add_step:%r" % self.instance_add_step)
        self.logger.info("ReadConfig, moniter_interval:%r" % self.moniter_interval)
        self.logger.info("ReadConfig, create_instance_threshold:%r" % self.create_instance_threshold)
        self.logger.info("ReadConfig, release_instance_waiting_time:%r" % self.release_instance_waiting_time)

        # 查找所有pool
        self.logger.info('GetAllPoolFromConfig')
        self.bcs_pools = {}
        sections = self.config.GetAllSections()
        pool_count = 0
        for s in sections:
            if s == SECTION_COMMON or s == SECTION_DEADLINE_CONFIG or s == SECTION_QUBE_CONFIG:
                continue
            if s == DEFAULT_POOL:
                self.logger.info('UseDefaultPool')
            # bcs
            self.logger.info("Init Pool %r" % s)
            self.bcs_pools[s] = bcs.BCS(self.config, s, self.logger)

        if self.server_type == DEADLINE_POOL_TYPE:
            self.logger.info("InitDeadlinePoolType")
            self.server = deadline.DeadLineImpl(self.config, self.logger, True)
        elif self.server_type == DEADLINE_GROUP_TYPE:
            self.logger.info("InitDeadlineGroupType")
            self.server = deadline.DeadLineImpl(self.config, self.logger, False)
        elif self.server_type == QUBE_TYPE:
            self.logger.info("InitQube")
            self.server = '' #TODO
        else:
            self.logger.error("InvalidType")
            raise Exception("InvalidType")

    def ToDeleteInstance(self, bcs_pool, to_delete_host, deleting_host, count):
        to_delete_count = count
        for k, v in to_delete_host.items():
            self.logger.info("DeleteInstance, InstanceId:%r, Host:%r" % (v['Id'], k))
            bcs_pool.DeleteInstance(v['Id'])
            to_delete_count -= 1
            deleting_host[k] = v
            if to_delete_count == 0:
                return

    def DeleteInstances(self, pool_name, bcs_pool, pool_hosts, instances, count):
        deleting_host = {}
        notpool_host = {}
        unknow_host = {}
        offline_host = {}
        idle_host = {}
        self.logger.debug("DeleteInstances, Pool：%r, HostCount:%r, InstanceCount:%r" % (pool_name, len(pool_hosts), len(instances)))
        # TODO::unkown是否包含被锁定的实例，如果包含是否要释放
        # pool中释放先后顺序为: deleting/deleted -> 不在pool中-> OFFLINE->IDLE->UNKNOWN
        for k,v in instances.items():
            self.logger.debug("Instance: %r, State:%r" % (k, v['State']))
            if v['State'] == 'Deleting' or v['State'] == 'Deleted':
                self.logger.debug("deleting_host: %r, State:%r" % (k, v['State']))
                deleting_host[k] = v

            if k in pool_hosts:
                if pool_hosts[k]['State'] == HOST_STAT_UNKNOWN:
                    self.logger.debug("unknow_host: %r, State:%r" % (k, v['State']))
                    unknow_host[k] = v
                elif pool_hosts[k]['State'] == HOST_STAT_OFFLINE:
                    self.logger.debug("offline_host: %r, State:%r" % (k, v['State']))
                    offline_host[k] = v
                elif pool_hosts[k]['State'] == HOST_STAT_IDLE:
                    self.logger.debug("idle_host: %r, State:%r" % (k, v['State']))
                    idle_host[k] = v
            else:
                self.logger.debug("notpool_host: %r, State:%r" % (k, v['State']))
                notpool_host[k] = v
        
        #deleting/dedelted 的实例
        if len(deleting_host) >= count:
            self.logger.debug("DeleteDone: Deleteting: %r, count:%r" % (len(deleting_host), count))
            return
        # not in pool 的实例
        self.ToDeleteInstance(bcs_pool, notpool_host, deleting_host, count - len(deleting_host))
        if len(deleting_host) >= count:
            self.logger.debug("DeleteDone: Deleteting: %r, count:%r" % (len(deleting_host), count))
            return

        # OFFLINE的实例
        self.ToDeleteInstance(bcs_pool, offline_host, deleting_host, count - len(deleting_host))
        if len(deleting_host) >= count:
            self.logger.debug("DeleteDone: Deleteting: %r, count:%r" % (len(deleting_host), count))
            return

        # IDLE的实例
        self.ToDeleteInstance(bcs_pool, idle_host, deleting_host, count - len(deleting_host))
        if len(deleting_host) >= count:
            self.logger.debug("DeleteDone: Deleteting: %r, count:%r" % (len(deleting_host), count))
            return

        # UNKNOWN的实例
        self.ToDeleteInstance(bcs_pool, unknow_host, deleting_host, count - len(deleting_host))
        if len(deleting_host) >= count:
            self.logger.debug("DeleteDone: Deleteting: %r, count:%r" % (len(deleting_host), count))
            return


    def AddNewHostToPool(self, pool_name, pool_hosts, instances):
        self.logger.debug("AddNewHostToPool: %r" % pool_name)
        for k,v in instances.items():
            if v["State"] != "Running":
                self.logger.info("Instance not ready: Pool:%r, Host:%r, State:%r" % (pool_name, k, v["State"]))
                continue

            if k in pool_hosts.keys():
                self.logger.debug("InstanceAdded: Pool:%r, Host:%r, State:%r" % (pool_name, k, v["State"]))
                continue
            
            #接入了处于非idel，未接入也加进去?? TODO::not_register_host_timeout

            self.logger.info("AddHost: Pool:%r, Host:%r" % (pool_name, k))
            try: 
                self.server.AddHostToPool(k, pool_name)
            except:
                self.logger.debug("AddHostFailed: %s, %s" % (pool_name, k))

    def RemoveReleasedHost(self, pool_name, pool_hosts, instances, host_name_prefix):
        self.logger.debug("RemoveReleasedHost: Pool:%r, HostPrefix:%r" % (pool_name, host_name_prefix))
        for host in pool_hosts:
            if host in instances:
                # 长时间offline的如何处理？？TODO
                self.logger.debug("IgnoreHost: Pool:%r, Host:%r" % (pool_name, host))
                continue

            if host_name_prefix != '' and not host.startswith(host_name_prefix):
                #非云上机器
                self.logger.debug("NotThisPoolHost: Pool:%r, Host:%r" % (pool_name, host))
                continue
            
            # 不指定hostname，那么认为都属于本pool的
            self.logger.info("RemoveHostFromPool: Pool:%r, Host:%r" % (pool_name, host))
            try: 
                self.server.RemoveHostFromPool(host, pool_name)
                if pool_name != DEFAULT_POOL:
                    self.server.RemoveHostFromPool(host, DEFAULT_POOL)
            except:
                self.logger.debug("RemoveHostFromPoolFailed: Pool:%r, Host:%s" % (pool_name, host))

    def HandlePool(self, pool_name, bcs_pool):
        self.logger.debug("handler Pool: %s" % pool_name)

        # 从server获取pool的host
        self.logger.debug("ListHostsInPool: %s" % pool_name)
        pool_hosts = self.server.ListHostsInPool(pool_name)

        # 从bcs获取所有实例
        self.logger.debug("ListClusterInstances: %s" % pool_name)
        instances = bcs_pool.ListClusterInstances()
        
        # 把残留的host从pool中移除
        self.logger.debug("RemoveReleasedHost: %s" % pool_name)
        self.RemoveReleasedHost(pool_name, pool_hosts, instances, bcs_pool.hostname_prefix)

        # 把新加入instance加入到pool
        self.logger.debug("AddNewHostToPool: %s" % pool_name)
        self.AddNewHostToPool(pool_name, pool_hosts, instances)
        
        # 获取bcs实例数量
        VMCount, actualVMCount = bcs_pool.GetClusterInstanceCount()
        self.logger.debug("GetClusterInstanceCount: %s, %d, %d" % (pool_name, VMCount, actualVMCount))

        # 期望机器数,并根据用户期望调整
        desiredHostCount = self.server.GetPoolDesiredHostCount(pool_name)
        self.logger.debug("GetPoolDesiredHostCount: %s, %d" % (pool_name, desiredHostCount))

        # 删除实例
        if VMCount > desiredHostCount and VMCount > bcs_pool.min_instance_count:
            deleteCount = VMCount - desiredHostCount
            if desiredHostCount < bcs_pool.min_instance_count:
                self.logger.debug("ChangeToMinCount: %s, %d, %d, %d" % (pool_name, VMCount, desiredHostCount, bcs_pool.min_instance_count))
                deleteCount = VMCount - bcs_pool.min_instance_count

            self.logger.debug("DeleteHost: %s, %d, %d, %d, %d" % (pool_name, VMCount, desiredHostCount, bcs_pool.min_instance_count, deleteCount))
            self.DeleteInstances(pool_name, bcs_pool, pool_hosts, instances, deleteCount)
            return
        
        desiredHostCount = float(desiredHostCount)
        if desiredHostCount < float(bcs_pool.min_instance_count) * self.create_instance_threshold:
            self.logger.debug("ChangeToMinCount: %s, %f, %d" % (pool_name, desiredHostCount, bcs_pool.min_instance_count))
            desiredHostCount = bcs_pool.min_instance_count * self.create_instance_threshold

        # 创建实例
        if self.create_instance_threshold * float(VMCount) < float(desiredHostCount):
            count = int(float(desiredHostCount) / self.create_instance_threshold)
            if count > bcs_pool.max_instance_count:
                count = bcs_pool.max_instance_count
                self.logger.debug("ChangeToMaxCount: %s, %d" % (pool_name, count))
            
            if VMCount == count:
                self.logger.debug("NotChangeCluster: %s, %d, %d" % (pool_name, count, VMCount))
                return

            self.logger.debug("ChangeClusterInstanceCount: %s, %d, %d, %f, %d" % (pool_name, VMCount, desiredHostCount, self.create_instance_threshold, count))
            bcs_pool.ChangeClusterInstanceCount(count)
            return

    def OneRound(self):
        self.logger.debug("StartOneRound")
        for pool_name, bcs_pool in self.bcs_pools.items():
            try:
                self.HandlePool(pool_name, bcs_pool)
            except:
                self.logger.error("Handler Pool  %s Failed. " % pool_name)


    def Loop(self):
        self.logger.debug("Loop...")
        while 1:
            try:
                self.OneRound()
            except:
                self.logger.info("Error")

            self.logger.debug("Sleep,wait next round")
            time.sleep(self.moniter_interval)

