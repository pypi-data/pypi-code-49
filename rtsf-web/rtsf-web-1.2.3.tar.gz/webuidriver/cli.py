#! python3
# -*- encoding: utf-8 -*-
'''
Current module: webuidriver.cli

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      webuidriver.cli,v 1.0 2018年8月19日
    FROM:   2018年8月19日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''


import argparse
from rtsf.p_applog import color_print,logger
from rtsf.p_executer import TestRunner
from webuidriver.driver import LocalDriver, RemoteDriver
from webuidriver.remote.SeleniumHatch import SeleniumHatch
from webuidriver.remote.SeleniumJar import SeleniumJar
from webuidriver.__about__ import __version__
    

def hub_main_run():
    parser = argparse.ArgumentParser(description="selenium server jar with hub mode.")
                
    parser.add_argument(
        '--java-path', default='java',
        help="path of java. default is `java` if JAVA_HOME is configured. ")
        
    parser.add_argument(
        '--port', type = int, default = 4444,
        help="listen port for hub mode. default port: 4444")
                
    parser.add_argument(
        'server_jar', 
        help="selenium server jar path for selenium grid mode")
    
    
    color_print("webuidriver {}".format(__version__), "GREEN")
    args = parser.parse_args()
    SeleniumJar(args.server_jar, args.java_path).hub(args.port).start_server()
    
def node_main_run():
    parser = argparse.ArgumentParser(description="selenium server jar with node mode.")
                
    parser.add_argument(
        '--java-path', default='java',
        help="path of java. default is `java` if JAVA_HOME is configured. ")
        
    parser.add_argument(
        '--port', type = int, default = 5555,
        help="listen port for node mode. default port: 5555")
    
    parser.add_argument(
        '--hub-ip', default = "localhost",
        help="hub host or hub ip which need to connect. default host: localhost")
    
    parser.add_argument(
        '--hub-port', type = int, default = 4444,
        help="hub port which need to connect. default: 4444")
    
                
    parser.add_argument(
        'server_jar', 
        help="selenium server jar path for selenium grid mode")
    
    
    color_print("webuidriver {}".format(__version__), "GREEN")
    args = parser.parse_args()
    SeleniumJar(args.server_jar, args.java_path).node(args.port,(args.hub_ip, args.hub_port)).start_server()
    
    

def local_main_run():
    
    parser = argparse.ArgumentParser(description="Tools for web ui test. Base on rtsf.")
            
    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    
    parser.add_argument(
        '--log-file',
        help="Write logs to specified file path.")
    
    parser.add_argument(
        '--browser',default = "chrome",
        help="set browser, only chrome or firefox. default: chrome")
    
    parser.add_argument(
        '--download-path',default = None,
        help="set the path where to save download file from browser. default: None")
    
    parser.add_argument(
        '--marionette', action = 'store_true', default = False,
        help="use firefox driver `geckodriver.exe` if True. default: False")
    
    parser.add_argument(
        'case_file', 
        help="yaml testcase file")
    
    color_print("webuidriver {}".format(__version__), "GREEN")
    args = parser.parse_args()
    logger.setup_logger(args.log_level, args.log_file)    
    
    LocalDriver._browser = args.browser
    LocalDriver._download_path = args.download_path
    LocalDriver._marionette = args.marionette
    runner = TestRunner(runner = LocalDriver).run(args.case_file)
    html_report = runner.gen_html_report()
    color_print("report: {}".format(html_report))
    
def remote_main_run():
    
    parser = argparse.ArgumentParser(description="Tools for web ui test. Base on rtsf.")
            
    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    
    parser.add_argument(
        '--log-file',
        help="Write logs to specified file path.")
    
    parser.add_argument(
        '--browser',default = "chrome",
        help="set browser, only chrome or firefox. default: chrome")
    
    parser.add_argument(
        '--download-path',default = None,
        help="set the path where to save download file from browser. default: None")
    
    parser.add_argument(
        '--marionette', action = 'store_true', default = False,
        help="use firefox driver `geckodriver.exe` if True. default: False")
    
    parser.add_argument(
        '--ip',default = "localhost",
        help="remote hub ip. default: localhost")
    
    parser.add_argument(
        '--port', type = int, default = 4444,
        help="remote hub port. default: 4444")
    
    parser.add_argument(
        'case_file', 
        help="yaml testcase file")
    
    color_print("webuidriver {}".format(__version__), "GREEN")
    args = parser.parse_args()
    logger.setup_logger(args.log_level, args.log_file)    
    
    RemoteDriver._browser = args.browser
    RemoteDriver._download_path = args.download_path
    RemoteDriver._marionette = args.marionette
    RemoteDriver._remote_ip = args.ip
    RemoteDriver._remote_port = args.port
    
    runner = TestRunner(runner = RemoteDriver).run(args.case_file)
    html_report = runner.gen_html_report()
    color_print("report: {}".format(html_report))
    
    
    
    
