#!/usr/bin/python
# -*- coding: utf-8 -*
# #############################################################################
#
#  Copyright (c) Baidu.com,  Inc. All Rights Reserved
#
# #############################################################################
"""
该模块提供机器运维层面的一些操作.例如:

* 当前机器属于那个服务节点
* 当前机器一段时间内的报警和监控想的趋势图

:author:
    pankai01
:description:
    该模块提供机器运维层面的一些操作
"""
from __future__ import print_function
from cup.bidu.noah.lib.meta import meta_query_m as metaquery
from cup.bidu.noah.lib.moni import monquery_m as monquery
from cup.bidu.noah.lib.moni  import alert_m as alert


class InvalidParamException(Exception):
    """自定义异常类 InvalidParamException"""
    def __init__(self, msg):
        """InvalidParamException"""
        Exception.__init__(self)
        self.msg = msg

class Host(object):
    """
    :param host_name:
        想要操作的机器名

    使用这个类获取机器相关的运维信息

    *实例*

    ::

        a = Host("cp01-yxtocp021.vm.baidu.com")
        services = a.get_services_of_the_host()
        for service in services:
            print(serivce)

    """

    def __init__(self, host_name):
        """
        """
        self._host_name = host_name

    def get_services_of_the_host(self):
        """
        获取当前机器上运行了哪些服务, 我们返回bns服务

        :return:
            数组
            例如
            [u'cassandra-dtrace.aqueducts.hd',  u'online.aqueducts.all']

        :raise:
            MetaQueryCrashException. 通过err.msg获取异常细节.
        """
        mq = metaquery.MetaQuery()
        return mq.do_get_relation_by_name(self._host_name, "service")

    def get_noah_paths_of_the_host(self):
        """获取当前机器所在的noah服务树路径

        :return:
            返回结果以数组展示

        *实例*

        ::

            [
                u'BAIDU_OPED_aqueducts_dtrace_cassandra',
                u'BAIDU_OPED_aqueducts_dtrace_cassandra_cassandra-dtrace.aqueducts.hd',
                u'BAIDU',
                u'BAIDU_OPED_aqueducts_aqueducts_online.aqueducts.all',
                u'BAIDU_OPED',
                u'BAIDU_OPED_aqueducts_dtrace',
                u'BAIDU_OPED_aqueducts',
                u'BAIDU_OPED_aqueducts_aqueducts'
            ]

        :raise:
            MetaQueryCrashException. See detail by err.msg.
        """
        mq = metaquery.MetaQuery()
        return mq.do_get_relation_by_name(self._host_name, "path")

    def get_products_of_the_host(self):
        """获取当前机器属于哪个产品线

        :return:
            [u'BAIDU_OPED_aqueducts']

        :raise:
            出错抛出MetaQueryCrashException. 获取异常信息err.msg.
        """
        mq = metaquery.MetaQuery()
        return mq.do_get_relation_by_name(self._host_name, "product")

    def get_host_monitor_items(self):
        """
        获取当前机器所有机器监控项

        :return:
            返回如下数组,每个监控项的含义参考argus文档
            http://wiki.babel.baidu.com/twiki/bin/view/Ps/OP/Argus_si

        *示例*

        ::

            [
               {'item_name': u'CPU_CONTEXT_SWITCH',  'cycle': 10},
               {'item_name': u'CPU_CPU0_IDLE',  'cycle': 10},
               {...}
            ]

        :Raises:
            MonQueryCrashException. See detail by err.msg
        """
        mq = monquery.MonQuery()
        return mq.get_namespace_items(self._host_name)

    def get_host_monitor_item_latest_value(self, item_name):
        """返回某个监控项的最新监控数据

        :param item_name:
            监控项名称

        :return:
            返回如下格式的数组(总是只有一项):

        *示例*
        ::

            [{'timestamp': u'20141205134011',  'value': 97.86}]

        :raise:
            MonQueryCrashException. See detail by err.msg
        """
        mq = monquery.MonQuery()
        return mq.get_item_value(self._host_name, item_name, None, None)

    def get_host_monitor_item_values(self, item_name, start_time=None, end_time=None):
        """
        获取某个监控项一段时间内的监控数据
        如果不指定开始时间则返回最新的数据

        :param item_name:
            监控项名称
        :param start_time:
            开始时间.格式为 YYYYmmddHHMMSS.如果start_time不指定则返回最新的监控值
        :param end_time:
            结束时间,格式为YYYYmmddHHMMSS.

        :return:
            返回如下的数组

        ::

            [
                {'timestamp': u'20141204000001',  'value': 98.55},
                {'timestamp': u'20141204000011',  'value': 98.34},
                {...}
            ]

        :raise:
            出错raise MonQueryCrashException. See detail by err.msg
        """
        mq = monquery.MonQuery()
        return mq.get_item_value(self._host_name, item_name, start_time, end_time)

    def get_host_monitor_sampling_values(self, item_name, span, start_time, end_time):
        """
        获取一段时间内的平均值监控数据,例如平均值等
        注意结束时间-开始时间必须大于span这个值

        :param span:
            聚合周期,以秒为单位.例如10, 60, 3600.
        :param start_time:
            开始时间,格式为YYYYmmddHHMMSS.
        :param end_time:
            开始时间,格式为YYYYmmddHHMMSS.

        """
        mq = monquery.MonQuery()
        return mq.get_item_value_avg(self._host_name, item_name, span, start_time, end_time)

    def get_host_monitor_rules(self):
        """返回一个机器的所有监控策略.

        :return:
            返回如下格式的数组:

        ::

            [
                {
                    'rule_name': 'cluster.dtrace.aqueducts.hd: host: cpu_fatal',
                    'blocked': 'unblocked'
                },
                {
                    ...
                }
            ]

        :raise:
            出错, AlertException:see the e.msg to get error message.
        """
        mq = alert.Alerts()
        return mq.get_all_rules(self._host_name)

    def get_host_raw_alerts(self, start_time, end_time):
        """
        返回一段时间内的报警信息.

        注意结束时间-开始时间必须大于span这个值

        :param start_time:
            格式为YYYYmmddHHMMSS, 不能为空
        :param end_time:
            格式为 YYYYmmddHHMMSS, 不能为空.

        :return:
            返回数组如下

        ::

            [
                {
                    alert_id: "",
                    alert_time: "",
                    mail_receiver: "",
                    mail_title: "",
                    message_content: "",
                    sms_receiver: "",
                    tracker_idc: "",
                    warning_list: [
                        {
                            duration: "",
                            item_values: "",
                            judge_expression: "",
                            namespace: "",
                            rule_name: "",
                            warning_status: "",
                            warning_time: ""
                        },
                        {
                            ...
                        }
                    ]
                },
                {
                    ...
                }
            ]

        :raise:
            InvalidParamException:input params not valid.
            AlertException:see the e.msg to get error message.
        """
        if (start_time == "" or end_time == ""):
            raise InvalidParamException("start time or end time must not be empty")
        mq = alert.Alerts()
        return mq.get_raw_alerts(self._host_name, start_time, end_time)


if __name__ == "__main__":
    h = Host("sh01-aqueducts-dtrace-cassandra02.sh01")
    try:
        print(h.get_services_of_the_host())
        print(h.get_noah_paths_of_the_host())
        print(h.get_products_of_the_host())
        print(h.get_host_monitor_items())
        print(h.get_host_monitor_item_latest_value("CPU_IDLE"))
        print(
            h.get_host_monitor_item_values("CPU_IDLE", "20141204000000",
                "20141204010000")
        )
        print(
            (h.get_host_monitor_sampling_values("CPU_IDLE", 86400,
              "20141201000000", "20141209000000")
            )
        )
        print(h.get_host_monitor_rules())
        print(h.get_host_raw_alerts("20141205100000", "20141205110000"))
    except metaquery.MetaQueryCrashException as e:
        print(e.msg)
    except monquery.MonQueryCrashException as e:
        print(e.msg)
    except alert.AlertException as e:
        print(e.msg)
