# -*- coding: utf-8 -*-
#!/usr/bin/env python

from Deadline import DeadlineConnect
from const import *

class DeadLineImpl:
    def __init__(self, config, logger, pool_mode):
        # 获取deadline 配置
        logger.info("ReadConfig. pool_mode:%r" % pool_mode)
        self.server_ip = config.TryGet(SECTION_DEADLINE_CONFIG, 'server_ip', '127.0.0.1')
        self.server_port = config.TryGetInt(SECTION_DEADLINE_CONFIG, 'server_port', 8082)
        self.remove_offline = config.TryGetBoolean(SECTION_DEADLINE_CONFIG, 'remove_offline_slave', False)
        self.pool_mode = pool_mode
        self.logger = logger
        logger.info("ReadConfig. server_ip:%r" % self.server_ip)
        logger.info("ReadConfig. server_port:%r" % self.server_port)
        logger.info("ReadConfig. remove_offline:%r" % self.remove_offline)

        # 创建dealine client
        logger.info("InitConnet")
        self.con = DeadlineConnect.DeadlineCon(self.server_ip, self.server_port)
    '''
    def ListHostsInfo(self):
        slave_list = self.con.Slaves.GetSlaveInfos()
        slaves = {}
        #转换为字典
        for slave in slave_list:
            slaves[slave["Host"]] = slave
        return slaves

    def GetSlaveInfo(self, slave):
        slave = self.con.Slaves.GetSlaveInfo(slave)
        return slave

    def DeleteSlave(self, slave):
        return self.con.Slaves.DeleteSlave(slave)
    '''

    def ListHostsInPool(self, pool_name):
        # 获取所有slaveinfo, 转换为dict
        infos = self.con.Slaves.GetSlaveInfos()
        self.logger.debug("StaveInfos, Pool:%r, Count:%r" % (pool_name, len(infos)))
        #[{},{},{}]
        slave_infos = {}
        for info in infos:
            if info["Host"] != '':
                self.logger.debug("Host:%r" % info["Host"])
                slave_infos[info["Host"]] = info

        #获取poo的所有slave,如果是默认pool，获取所有的slave
        if pool_name == DEFAULT_POOL:
            self.logger.debug("DefaultPool")
            slave_list = slave_infos
        else:
            if self.pool_mode:
                self.logger.debug("PoolMode, Pool:%r" % pool_name)
                slave_list = self.con.Slaves.GetSlaveNamesInPool(pool_name)
            else:
                self.logger.debug("GroupMode, Pool:%r" % pool_name)
                slave_list = self.con.Slaves.GetSlaveNamesInGroup(pool_name)
            #[u'dd1', u'iZ8vb9vizxz6w5Z', u'iZ8vbceyb0d6ysZ']
        self.logger.debug("SlaveList, Pool:%r, Count:%r" % (pool_name, len(slave_list)))

        # 转换到内部状态
        slaves = {}
        for s in slave_list:
            if s in slave_infos:
                #deadline host stat 0 = Unknown, 1 = Rendering, 2 = Idle, 3 = Offline, 4 = Stalled, 8 = StartingJob
                info = slave_infos[s]
                stat = info['Stat']
                inner_stat = 0
                if  stat == 1 or stat == 8:
                    inner_stat = HOST_STAT_RENDERING
                elif stat == 2:
                    inner_stat = HOST_STAT_IDLE
                elif stat == 3:
                    inner_stat = HOST_STAT_OFFLINE
                else:
                    inner_stat = HOST_STAT_UNKNOWN
                slaves[s] = {
                        'State': inner_stat,
                        'IP': info['IP'],
                    }
                self.logger.debug("Host:%r, State:%r, InnerState:%r, IP:%r" % (s, info["Stat"], inner_stat, info["IP"]))
        self.logger.debug("Slaves, Pool:%r, Count:%r" % (pool_name, len(slaves)))
        return slaves 

    def AddHostToPool(self, host, pool_name):
        if pool_name == DEFAULT_POOL:
            self.logger.debug("DefaultPool")
            return
        if self.pool_mode:
            self.logger.debug("AddHostToPool, Pool:%r, Host:%r" % (pool_name, host))
            return self.con.Slaves.AddPoolToSlave(host, pool_name)
        else:
            self.logger.debug("AddHostToGroup, Group:%r, Host:%r" % (pool_name, host))
            return self.con.Slaves.AddGroupToSlave(host, pool_name)
        
    def RemoveHostFromPool(self, host, pool_name):
        if pool_name == DEFAULT_POOL:
            self.logger.debug("DefaultPool")
            return
        if self.pool_mode:
            self.logger.debug("RemoveHostFromPool, Pool:%r, Host:%r" % (pool_name, host))
            self.con.Slaves.RemovePoolFromSlave(host, pool_name)
            self.con.Slaves.DeleteSlave(host)
            self.logger.debug("RemoveHostFromPoolDone, Pool:%r, Host:%r" % (pool_name, host))
        else:
            self.logger.debug("RemoveHostFromGroup, Pool:%r, Host:%r" % (pool_name, host))
            return self.con.Slaves.RemoveGroupFromSlave(host, pool_name)

    def GetPoolDesiredHostCount(self, pool_name):
        #获取所有的active jobs, TODO::是否需要获取Pending的job 
        jobs = self.con.Jobs.GetJobsInState('Active')

        #获取每个host的task数
        active_task_count = 0
        for job in jobs:
            if job['Props']['Pool'] != pool_name:  #TODO::这样判断是否正确
                self.logger.debug("NotThePool. %r, %r" % (pool_name, job['Props']['Pool']))
                continue
            tasks = self.con.Tasks.GetJobTasks(job['_id'])
            self.logger.debug("Pool:%r, Job:%r, TaskCount: %r" % (pool_name, job['_id'], len(tasks["Tasks"])))
            for task in tasks["Tasks"]:
                self.logger.debug("Pool:%r, Job:%r, Task: %r, State:%r" % (pool_name, job['_id'], task['_id'], task['Stat']))
                if task['Stat'] == 2 or task['Stat'] == 4:
                    active_task_count += 1

        self.logger.debug("TotalTaskCount: %r" % active_task_count)
        return active_task_count

'''
    def GetJobsInState(self):
        return self.con.Jobs.GetJobsInState('Active')
        
    def GetJobTasks(self, job_id):
        #GetJobTaskIds
        return self.con.Tasks.GetJobTasks(job_id)
'''

'''
    Values for some Task properties are represented by numbers. Those properties and their possible values are listed below.
    Stat (Status)
    1 = Unknown
    2 = Queued
    3 = Suspended
    4 = Rendering
    5 = Completed
    6 = Failed
    8 = Pending
'''
