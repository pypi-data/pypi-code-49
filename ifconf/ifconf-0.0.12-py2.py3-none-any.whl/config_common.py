# -*- coding: utf-8 -*-

import os
import sys

import logging
import logging.config
from logging.handlers import RotatingFileHandler

logging.NOTICE = 25
logging.NOTICE_LEVEL_NAME = "NOTICE"

logging.addLevelName(logging.NOTICE, logging.NOTICE_LEVEL_NAME)
def notice(self, message, *args, **kws):
    self._log(logging.NOTICE, message, args, **kws) 
logging.Logger.notice = notice

def configure_logging(conf
                      , log_level=logging.INFO
                      , log_file=""
                      , log_max_bytes = 1024*1024*16
                      , log_backup_count = 99
                      , log_encoding = 'UTF-8'
                      , fmt = '%(asctime)s [%(name)s] [%(levelname)s] %(message)s'):
    conf.verbose = conf.args.verbose if hasattr(conf.args, 'verbose') else False
    conf.log_level = log_level
    conf.log_level_name = logging.getLevelName(log_level)
    conf.log_file = log_file
    conf.log_max_bytes = log_max_bytes
    conf.log_backup_count = log_backup_count
    conf.log_encoding = log_encoding
    conf.formatter = logging.Formatter(fmt)

    if [s for s in ('loggers', 'handlers', 'formatters') if conf.parser.has_section(s)]:
        logging.config.fileConfig(conf.parser, disable_existing_loggers=False)
        conf.logger = logging.getLogger()
    elif conf.parser.has_section('logging'):
        logging.config.dictConfig({'version': 1, 'disable_existing_loggers' : False})
        section = conf.parser['logging']
        conf.verbose = section.get('verbose', conf.verbose)
        conf.log_level_name = section.get('level', 'INFO')
        conf.log_level = getattr(logging, conf.log_level_name.upper(), conf.log_level)
        conf.log_file = section.get('log_file', conf.log_file)
        conf.err_file = section.get('err_file', '')
        conf.log_encoding = section.get('encoding', conf.log_encoding)
        bytes_str = section.get("max_bytes", '').replace('(','').replace(')','').replace('=','')
        conf.log_max_bytes = eval(bytes_str) if bytes_str else conf.log_max_bytes
        conf.log_backup_count = int(section.get('backup_count', conf.log_backup_count))
        conf.logger = load_logging(conf)
    else:
        conf.logger = load_logging(conf)


def load_logging(conf, name=None):
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()
    logger.setLevel(conf.log_level)


    if hasattr(conf, 'debug') and conf.debug:
        handler = logging.StreamHandler()
        handler.setFormatter(conf.formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
            
    if hasattr(conf, 'debug_file') and conf.debug_file:
        try:
            handler = FileHandler(conf.debug_file, encoding = conf.log_encoding)
            handler.setFormatter(conf.formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
        except Exception as e:
            conf.err.append('DEBUG FILEログ設定に失敗しました。ファイル：[{}] エラー：[{}]'.format(conf.debug_file, e))
    if hasattr(conf, 'log_file') and conf.log_file:
        try:
            handler = RotatingFileHandler(conf.log_file, maxBytes = conf.log_max_bytes, backupCount = conf.log_backup_count, encoding = conf.log_encoding)
            handler.setFormatter(conf.formatter)
            logger.addHandler(handler)
        except Exception as e:
            conf.err.append('ログ設定に失敗しました。ファイル：[{}] エラー：[{}]'.format(conf.log_file, e))
    if hasattr(conf, 'err_file') and conf.err_file and conf.err_file != conf.log_file:
        try:
            handler = RotatingFileHandler(conf.err_file, maxBytes = conf.log_max_bytes, backupCount = conf.log_backup_count, encoding = conf.log_encoding)
            handler.setFormatter(conf.formatter)
            handler.setLevel(logging.ERROR)
            logger.addHandler(handler)
        except Exception as e:
            conf.err.append('エラーログ設定に失敗しました。ファイル：[{}] エラー：[{}]'.format(conf.err_file, e))
    if len(logger.handlers) == 0:
        handler = logging.StreamHandler()
        handler.setFormatter(conf.formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.warning("ログの出力先が標準エラー出力に設定されました。")
        
    if conf.verbose:
        logger.setLevel(logging.DEBUG)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("DEBUGモードが有効になりました。")
    elif logger.isEnabledFor(logging.INFO):
        logger.info("ログ設定が有効になりました。INFOログが出力されます。")
    elif logger.isEnabledFor(logging.NOTICE):
        logger.notice("ログ設定が有効になりました。NOTICEログが出力されます。")
    elif logger.isEnabledFor(logging.WARN):
        logger.warning("ログ設定が有効になりました。WARNINGログが出力されます。")
        
    return logger

def get_module_name_for(obj):
    if obj.__module__  == '__main__':
        try:
            return os.path.splitext(os.path.basename(sys.modules['__main__'].__file__))[0]
        except:
            return os.path.splitext(os.path.basename(sys.executable))[0]
    else:
        return obj.__module__
    
    

